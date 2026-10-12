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

The shared Core is synchronized from `notes_server/latex-course-repo/`.
When updating it, preserve the course identity in `notes-project.sty`, the
lecture and tutorial content, and the private-folder rules in `.gitignore`.

## Deployment

Only `latex_target/` is published. Its `manifest.json` declares schema version
1, project ID `data-analysis`, and this course's title. Keep the project ID
consistent with `notes-project.sty` and the deployment workflow. Build PDFs
locally before pushing; the deployment workflow does not compile LaTeX.

Pushing a change beneath `latex_target/` to `master` runs the
GitHub Actions workflow in `.github/workflows/deploy.yml`. It sends the
`NOTES_DEPLOY_KEY` secret to
`https://notes.rua.rs/deploy/data-analysis` in the `x-api-key`
header, then verifies that `lec01.pdf` appears on the course page and
can be downloaded.

Before the first push, configure the repository Actions secret
`NOTES_DEPLOY_KEY`. Its value must match the notes server's
`NOTES_DEPLOY_KEY` environment variable. The notes server must also
have the `data-analysis` project registered.
