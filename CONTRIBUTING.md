# Contributing

Thanks for improving materials for the **UofT ASIC Team**.

## After creating a course from this template

1. Run `scripts/init-template.py` with `--id`, `--title`, and `--description` (org is always `uoftasic`).
2. Enable GitHub Pages with **Settings → Pages → Source: GitHub Actions**, so that `.github/workflows/site.yml` can build and deploy the site.
3. Prefer repo names that match course ids (`dd103`, `ic101`, …).

See [TEMPLATE.md](TEMPLATE.md).

## Placeholders

Only these three are fillable:

| Token | Example |
|-------|---------|
| `ic101` | `dd103` |
| `IC101 - Introduction to IC Tools & Workspace` | `DD103 — RTL on FPGAs & ASICs` |
| `Learn how to setup IC tools and workspace on your device` | `RTL synthesis intro with Yosys` |

## Conventions

| Item | Convention |
|------|------------|
| Org | `uoftasic` |
| Default branch | `main` |
| Docs pages | kebab-case `.md` under `docs/` |
| Lab IDs | `lab-NN-short-name` |
| Adding a doc page | add `.md` under `docs/`, add it to the sidebar in `docs/_quarto.yml` and the chapters in `docs/_quarto-pdf.yml` |
| Adding a lab | `labs/<id>/` (if the lab has files to run) + `docs/labs/<id>-overview.md` + a row in the Course path table on `docs/index.md` + a sidebar entry in `docs/_quarto.yml` and a chapter in `docs/_quarto-pdf.yml`, in the same order |
| Links between pages | relative to the page they are written in (`../guide/x.md` from a lab) |
| Course path table | Columns `# \| \| What \| Time`. Read and Do in plain text. A Do row is `[Lab 01: Title](labs/<id>-overview.md)` followed by one sentence on what you'll do. Row times add up to the course total on the home page |
| Lab titles | `# Lab 01: Title` on the writeup, and the same text in the sidebar and the Course path |
| End of a lab writeup | `## Finishing` (one "You're done when" line about the student's own work), `### Questions` if any (each with a collapsed answer or a pointer to its step), `### Submit` (or "Nothing to submit."), then `## Going further (optional)` if any, then a "Next on the Course path" line |
| Binaries | small images in `docs/assets/`; large data → Git LFS or external |

## Docs vs labs

- **`docs/`**: the published site. Guide pages in `docs/guide/` are reading only; every hands-on step lives in a lab *writeup* in `docs/labs/`.
- **`labs/`**: runnable HDL / Python / data. Each `labs/<id>/README.md` links to its writeup on the site. IC101 has no lab packages; its labs run the shared `workspace` repo's scripts.
- **`scripts/`**: utilities; list entry points in `scripts/README.md`.

Do not put grades, solution keys, or PII under `docs/`. Prefer `labs/**/solutions/` and gitignore them on student forks when needed.

## Local docs preview

```bash
quarto preview docs                            # -> http://localhost:4200
quarto render docs --profile pdf --to typst    # whole course as one PDF in docs/_book/
```

## Pull requests

Keep changes focused. For a doc-only PR, check the navigation and math in a local preview when you can. CI checks links in two places: `.github/workflows/docs-link-check.yml` runs lychee over `docs/**/*.md` and checks that every image a page references exists, and `.github/workflows/site.yml` renders the site and runs `scripts/check_site.py` on it to check every local link and anchor.
