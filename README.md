# AP30019 — Data Analysis Techniques for Scientists

LaTeX source and built course notes for AP30019, **Data Analysis Techniques
for Scientists**.

## Compile

Open `lec01.tex` or `tut01.tex` in VS Code and run **Build LaTeX
project**, or use:

```sh
latexmk -pdf lec01.tex
latexmk -pdf tut01.tex
```

Finished PDFs are written to `latex_target/`; intermediate files stay in the
ignored `.build/` directory.

## Naming

Use two-digit, zero-padded filenames:

| Material | Source | Output |
|---|---|---|
| Lecture 1 | `lec01.tex` | `latex_target/lec01.pdf` |
| Tutorial 1 | `tut01.tex` | `latex_target/tut01.pdf` |

The shared formatting and reference macros live in `notes-common.sty`.
Course-specific server information lives in `notes-project.sty`. See
`LATEX_AUTHORING_GUIDE.md` for the complete authoring and reference guide.
