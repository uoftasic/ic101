# IC101 — Onboarding onto Tools

Learn how to set up IC tools and workspace on your device.

Part of the UofT ASIC Team education materials, published at <https://uoftasic.com/ic101/>. The
runnable tooling lives in the shared [`workspace`](https://github.com/uoftasic/workspace) repo,
not in this course repo.

## At a glance

| | |
|---|---|
| **Track** | Core (intro) |
| **Prerequisites** | None |
| **Tools** | git, Docker, IIC-OSIC-TOOLS, noVNC |
| **Shared workspace** | Yes: clone it once, reuse it in every course |

## What you'll do

1. Open a terminal and install git (Lab 01)
2. Learn why the team uses a containerized EDA toolchain, and install Docker (Lab 02)
3. Clone `workspace`, open the IIC-OSIC-TOOLS desktop in your browser with noVNC, and run the
   smoke test (Lab 03)
4. See where each tool sits in a tapeout flow

The course home page, [`docs/index.md`](docs/index.md), has a numbered Course path that
alternates guide pages (`docs/guide/`, reading only) with labs (`docs/labs/`, where all the
hands-on steps are). The sidebar in `docs/_quarto.yml` lists the pages in the same order. IC101's
labs have no packages under `labs/`, because everything they run comes from the `workspace` repo.

## Quick links

| What | Where |
|------|-------|
| Course home and Course path | [docs/index.md](docs/index.md) |
| Workspace (tools) | a sibling `workspace/` folder locally; GitHub: [uoftasic/workspace](https://github.com/uoftasic/workspace) |
| Portal hub | [edu.uoftasic.com](https://edu.uoftasic.com/) |

## Local preview

The site is built with [Quarto](https://quarto.org/docs/get-started/) 1.11:

```bash
quarto preview docs                            # -> http://localhost:4200
quarto render docs --profile pdf --to typst    # whole course as one PDF in docs/_book/
```

## GitHub Pages

| Setting | Value |
|---------|--------|
| Source | GitHub Actions |

`.github/workflows/site.yml` renders `docs/` with Quarto on every push to `main` that touches `docs/`, checks the rendered links with `scripts/check_site.py`, and deploys `docs/_site`, which includes a PDF of every page and the whole-course PDF.
