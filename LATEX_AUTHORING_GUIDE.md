# LaTeX Authoring and Reference Guide

These AP30019 notes for **Data Analysis Techniques for Scientists** compile
with pdfLaTeX. They require no Python, JSON reference index, or remote AUX files.

## Start and build a document

Copy the nearest starter and keep two-digit filenames:

```text
lec01.tex  -> latex_target/lec01.pdf
tut01.tex  -> latex_target/tut01.pdf
```

Every document loads the two-layer library:

```tex
\documentclass[12pt]{article}
\usepackage{notes-project}
```

- `notes-common.sty` is reusable and project-neutral.
- `notes-project.sty` supplies the public server root and project ID.

Build from VS Code with **Build LaTeX project**, or run:

```sh
latexmk -pdf lec01.tex
```

Auxiliary files go to `.build/`; the PDF goes to `latex_target/`.

The shared Core adds an italic, right-aligned `Compiled:` footer to the last
page of every PDF. It uses `datetime2` to render the build-machine timestamp
in ISO format with its timezone offset. The timestamp records compilation,
not the source modification time or deployment time.

## Numbered environments

Ordinary `\section` headings provide the first number. Each content type
has an independent counter, so a section can contain both Definition 2.1 and
Proposition 2.1.

| Short form | Full form | Reference kind |
|---|---|---|
| `dfn` | `definition` | `def` |
| `thm` | `theorem` | `thm` |
| `axm` | `axiom` | `axm` |
| `hypo` | `hypothesis` | `hypo` |
| `prop` | `proposition` | `prop` |
| `lem` | `lemma` | `lem` |
| `cor` | `corollary` | `cor` |
| `rem` | `remark` | `rem` |
| `eg` | `example` | `eg` |
| `ex` | `exercise` | `ex` |
| `conv` | `convention` | `conv` |

Give an item an optional printed title and a stable semantic ID:

```tex
\begin{dfn}[Sample Mean]{sample-mean}
  Definition text.
\end{dfn}
```

This creates `def:sample-mean`. If the ID is omitted, a plain-text title is
converted to lowercase kebab-case. Prefer an explicit ID when the title
contains LaTeX or when a shorter name avoids an overfull heading.

IDs appear as small gray monospace text by default. Use `\notesHideIDs` or
`\notesShowIDs` in the preamble to control them.

Use `axm` for a foundational statement accepted by the course, and `hypo`
for a named assumption whose truth or applicability is being investigated.

## Authoring markers

Use `\todo` for a blue TODO marker, `\todo[short description]` for a marker
with a note, and `\missingprereq{concept, owning subject}` for a purple
prerequisite marker. The current Core takes square brackets for the optional
TODO description.

To suppress these markers for a release build, put this in the preamble:

```tex
\RenewDocumentCommand{\todo}{o}{}
\RenewDocumentCommand{\missingprereq}{m}{}
```

## Proofs

```tex
\begin{proof}
  ...
\end{proof}

\begin{proof}[Uniqueness]
  ...
\end{proof}
```

An untitled proof prints “Proof.” A titled proof prints “Pf. Uniqueness.”
Proof environments do not take semantic IDs.

## References in the current PDF

```tex
See \xref{def:sample-mean}.
Apply the \xref[sample-mean definition]{def:sample-mean}.
```

The optional text makes ordinary words clickable. The starred form,
`\xref*{def:sample-mean}`, prints the same reference without a link.

## References to other PDFs

Reference forms progress from the current project to an explicit server:

| Scope | Syntax |
|---|---|
| Current project | `\xref{lec01::def:sample-mean}` |
| Another project on the same server | `\xref{other-project::lec01::def:item}` |
| Another server and project | `\xref{https://other.example::other-project::lec01::def:item}` |

Declare a frequently used document once:

```tex
\xrefuse{lec01}
See \xref{def:sample-mean}.
```

A local reference displays its current number via `cleveref`. A
cross-PDF reference displays its semantic name because it does not fetch
remote metadata. The link targets the stable semantic destination embedded in
the other PDF.

## Redirects for moved blocks

When a linkable block moves to another document, replace its original site
with a redirect so existing links and subsequent numbering remain valid:

```tex
\redirect[Sample Mean]{def}{sample-mean}{lec03::def:sample-mean}
```

The title is optional. The redirect retains the original `def:sample-mean`
label and `notes.def.sample-mean` PDF destination, advances that kind's
counter, and links to the new location. Every reference kind in the table
above supports redirects; proofs do not. Keep the redirect while other
documents may still cite the original destination.

## Linked notation and operators

Put course-specific symbols in a separate package such as
`subject-notations.sty`, loaded by `notes-project.sty` after `notes-common`.
Use `\xref` as the clickable operator head and leave its arguments outside the
link. This avoids nested links when an argument contains another linked symbol:

```tex
% subject-notations.sty
\providecommand*{\commutatorRef}{subject-project::ch03::def:commutator}
\newcommand{\comm}[2]{%
  \ensuremath{%
    \xref[\operatorname{comm}]{\commutatorRef}\!\left(#1,\, #2\right)%
  }%
}
```

The default renders `\comm{A}{B}` as
\(\operatorname{comm}(A,B)\), with only `comm` clickable. To reuse the
notation when the definition lives elsewhere, override the target before
loading the notation package:

```tex
% notes-project.sty
\RequirePackage{notes-common}
\newcommand*{\commutatorRef}{other-project::ch03::def:commutator}
\RequirePackage{subject-notations}
```

Use the ordinary `\xref` scope syntax in target macros. Prefer a new semantic
command such as `\comm` over redefining a standard LaTeX operator. If an
existing command must be replaced, preserve its argument signature and use an
explicit renewal command so collisions fail visibly.

Subject notation packages are optional. A dependent course may vendor and load
another subject's package; the project-qualified default keeps links pointing
to the owning subject. Do not use a relative path into a sibling repository,
because that path will not be portable to another checkout or build machine.

Existing operators may be intentionally replaced inside a subject package when
their mathematical behavior is preserved. For example, Real Analysis can keep
the normal subscript behavior of `\sup` while linking its operator head:

```tex
\providecommand*{\supremumRef}{real-analysis::lec01::def:supremum}
\let\raPlainSup\sup
\renewcommand*{\sup}{%
  \mathop{\xref[\mathrm{sup}]{\supremumRef}}\nolimits
}
```

Expose the saved command, here `\raPlainSup`, for exceptional contexts that
need the original unlinked operator.

## Exercises and source citations

For publicly hosted tutorial work, cite the source and write the original
answer without reproducing a full copyrighted question:

```tex
\begin{ex}{author-book-exercise-id}
  \emph{Source:} Author, \emph{Book Title}, edition, Exercise 1.2.3.
\end{ex}

% Write your answer below.
```

## Publication contract

Only `latex_target/` is deployable. It must contain a valid
`manifest.json`; built documents may be flat:

```text
latex_target/
├── manifest.json
├── lec01.pdf
└── tut01.pdf
```

The manifest project ID, `\notesProjectName`, repository checkout name,
server registration, and public URL segment must agree. Server-side
configuration is deliberately outside this LaTeX template.

For this course, the project ID is `data-analysis`, and the public server root
is `https://notes.rua.rs`. Cross-PDF URLs therefore use
`https://notes.rua.rs/data-analysis/`.
