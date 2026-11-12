# IC101 — Onboarding onto Tools

Set up the containerized open-source toolchain that every later course builds on.

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

The course home page, [`docs/README.md`](docs/README.md), has a numbered Course path that
alternates guide pages (`docs/guide/`, reading only) with labs (`docs/labs/`, where all the
hands-on steps are). `docs/_sidebar.md` lists the pages in the same order. IC101's labs have no
packages under `labs/`: everything they run comes from the `workspace` repo.

## Quick links

| What | Where |
|------|-------|
| Course home and Course path | [docs/README.md](docs/README.md) |
| Workspace (tools) | a sibling `workspace/` folder locally; GitHub: [uoftasic/workspace](https://github.com/uoftasic/workspace) |
| Portal hub | [edu.uoftasic.com](https://edu.uoftasic.com/) |

## Local preview

```bash
npx docsify-cli serve docs
# → http://localhost:3000
```
