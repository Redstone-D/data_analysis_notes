# LaTeX Authoring and Reference Guide

This repository is the AP30019 template for **Data Analysis Techniques for
Scientists**. It compiles with pdfLaTeX and does not require Python, JSON
reference indexes, or remote AUX files.

## Start a document

Copy the nearest template and keep two-digit filenames:

```text
lec01.tex  -> latex_target/lec01.pdf
tut01.tex  -> latex_target/tut01.pdf
```

Each source begins with:

```tex
\documentclass[12pt]{article}
\usepackage{notes-project}
```

Build from VS Code with **Build LaTeX project**, or run:

```sh
latexmk -pdf lec01.tex
```

The project configuration sends auxiliary files to `.build/` and the
finished PDF to `latex_target/`.

## Numbered environments

Ordinary `\section` headings provide the first number. Every content type
has its own counter, so a section may contain both Definition 2.1 and
Proposition 2.1.

| Short form | Full form | Reference kind |
|---|---|---|
| `dfn` | `definition` | `def` |
| `thm` | `theorem` | `thm` |
| `prop` | `proposition` | `prop` |
| `lem` | `lemma` | `lem` |
| `cor` | `corollary` | `cor` |
| `rem` | `remark` | `rem` |
| `ex` | `example` | `ex` |
| `exc` | `exercise` | `exc` |
| `conv` | `convention` | `conv` |

Use an optional printed title followed by a stable semantic ID:

```tex
\begin{dfn}[Sample Mean]{sample-mean}
  Definition text.
\end{dfn}
```

This creates `def:sample-mean`. If the ID is omitted, a plain-text title is
converted to lowercase kebab-case automatically. Use an explicit ID when the
title contains LaTeX markup or when a shorter identifier is clearer.

IDs appear as small gray monospace text by default. Put
`\notesHideIDs` in the preamble to hide them, or `\notesShowIDs` to
show them.

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

## References within one PDF

Reference an item by its semantic ID:

```tex
See \xref{def:sample-mean}.
```

Use custom clickable words when they read more naturally:

```tex
Apply the \xref[sample-mean definition]{def:sample-mean}.
```

The starred form, `\xref*{def:sample-mean}`, prints the reference without a
link.

## References to another PDF

The forms progress from the current project to an explicit server:

| Scope | Syntax |
|---|---|
| Current project | `\xref{lec01::def:sample-mean}` |
| Another project on the same server | `\xref{real-analysis::lec01::def:field}` |
| Another server and project | `\xref{https://other.example::project::lec01::def:item}` |

If many short references use one document, declare it once:

```tex
\xrefuse{lec01}
See \xref{def:sample-mean}.
```

A local reference displays its live number through `cleveref`. A link to
another PDF displays the semantic name because no remote metadata is required;
the stable PDF destination still remains valid if numbering changes.

## Exercises and copyright-conscious notes

For a published tutorial, cite the source exercise and write your own answer
without reproducing the full question:

```tex
\begin{exc}{author-book-exercise-id}
  \emph{Source:} Author, \emph{Book Title}, edition, Exercise 1.2.3.
\end{exc}

% Write your own answer below.
```

## Project-specific values

`notes-project.sty` defines:

```tex
\notesServerRoot  = https://notes.rua.rs
\notesProjectName = data-analysis
```

Cross-PDF URLs therefore use the base
`https://notes.rua.rs/data-analysis/`. Only the flat files in
`latex_target/` are intended for publication.
