# IC101 — Onboarding onto Tools

Set up the containerized open-source toolchain that every later course builds on.

Part of the **UofT ASIC Team** education materials. Published at **https://uoftasic.com/ic101/**. Runnable tooling lives in the shared **workspace** repo (not in this course repo).

## At a glance

| | |
|---|---|
| **Track** | Core (intro) |
| **Prerequisites** | None |
| **Tools** | Docker, IIC-OSIC-TOOLS, noVNC |
| **Shared workspace** | Yes — clone once, reuse every course |

## What you'll do

1. Understand why we use a containerized EDA toolchain
2. Install Docker Desktop
3. Clone **workspace** and launch the IIC-OSIC-TOOLS desktop (noVNC)
4. Run the smoke test
5. See where each tool sits in a tapeout flow

Start here: **[Getting started](guide/getting-started.md)**.

## Quick links

| What | Where |
|------|--------|
| Getting started | [guide/getting-started.md](guide/getting-started.md) |
| Workspace (tools) | sibling `workspace/` folder locally; GitHub: [uoftasic/workspace](https://github.com/uoftasic/workspace) |
| Portal hub | [edu.uoftasic.com](https://edu.uoftasic.com/) |

## Local preview

```bash
npx docsify-cli serve docs
# → http://localhost:3000
```
