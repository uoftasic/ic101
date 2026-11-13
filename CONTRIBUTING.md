# Contributing

Thanks for improving materials for the **UofT ASIC Team**.

## After creating a course from this template

1. Run `scripts/init-template.py` with `--id`, `--title`, and `--description` (org is always `uoftasic`).
2. Enable GitHub Pages: branch `main`, folder `/docs`.
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
| Adding a doc page | add `.md` under `docs/`, link in `docs/_sidebar.md` |
| Adding a lab | `labs/<id>/` (if the lab has files to run) + `docs/labs/<id>-overview.md` + a row in the Course path table on `docs/README.md` + sidebar entry in the same order |
| Course path table | Columns `# \| \| What \| Time`. Read and Do in plain text. A Do row is `[Lab 01: Title](labs/<id>-overview.md)` followed by one sentence on what you'll do. Row times add up to the course total on the home page |
| Lab titles | `# Lab 01: Title` on the writeup, and the same text in the sidebar and the Course path |
| End of a lab writeup | `## Finishing` (one "You're done when" line about the student's own work), `### Questions` if any (each with a collapsed answer or a pointer to its step), `### Submit` (or "Nothing to submit."), then `## Going further (optional)` if any, then a "Next on the Course path" line |
| Binaries | small images in `docs/assets/`; large data → Git LFS or external |

## Docs vs labs

- **`docs/`**: the published site. Guide pages in `docs/guide/` are reading only; every hands-on step lives in a lab *writeup* in `docs/labs/`.
- **`labs/`**: runnable HDL / Python / data. Each `labs/<id>/README.md` links to its Docsify writeup. IC101 has no lab packages; its labs run the shared `workspace` repo's scripts.
- **`scripts/`**: utilities; list entry points in `scripts/README.md`.

Do not put grades, solution keys, or PII under `docs/`. Prefer `labs/**/solutions/` and gitignore them on student forks when needed.

## Local docs preview

```bash
npx docsify-cli serve docs
```

## Pull requests

Keep changes focused. For doc-only PRs, check navigation and math locally when practical. Optional CI may link-check `docs/**`.
