# Agent guide — UofT ASIC course repos

You are working in a **course repository** for the UofT ASIC Team (`uoftasic`): pedagogical materials for IC / RTL / FPGA / open-source ASIC flows. The site under `docs/` is published on GitHub Pages (Docsify, zero build). Runnable work lives outside `docs/`.

Optimize for **clear student learning paths**, not template maintenance. Prefer concrete labs and notes students can follow end-to-end over meta documentation.

## Goals

- Teach IC development skills: RTL (SystemVerilog/Verilog), simulation, synthesis, FPGA bring-up, and/or open ASIC flows (e.g. Yosys, LibreLane, SKY130) as the course requires.
- Keep each lab **self-contained**: what you'll build → before you start → time → numbered parts with "You should see" checks → Finishing (You're done when, Questions, Submit) → Going further (optional) → the "Next on the Course path" line.
- Separate **reading** from **doing**. Guide pages (`docs/guide/`) explain; lab writeups (`docs/labs/`) hold every step a student performs. Runnable files live in `labs/`, `scripts/` and `notebooks/`, or, for IC101, in the shared `workspace` repo.
- Keep the **Course path** table on `docs/README.md` (alternating Read and Do rows, with times that add up to the course total on the home page) and `docs/_sidebar.md` in the same order. The table format is in "Adding a lab" below.
- Never publish grades, solution keys, or PII under `docs/`. Put keys in `labs/**/solutions/` and gitignore them on student forks when policy requires.

## Layout (do not fight this)

| Path | Published? | Put here |
|------|------------|----------|
| `docs/` | Yes | Guides, lab writeups, figures for the site |
| `docs/guide/` | Yes | Conceptual notes (flows, tools, theory); reading only |
| `docs/labs/` | Yes | Lab writeups only (`lab-NN-*-overview.md`) |
| `docs/assets/img/` | Yes | Small diagrams / waveforms for docs |
| `labs/<lab-id>/` | No | HDL, Python, testbenches, local data, graders (IC101 has none: its labs run the `workspace` repo's scripts) |
| `scripts/` | No | Course utilities / automation |
| `notebooks/` | No | Exploratory or assignment notebooks |
| `data/`, `figures/` | No | Shared datasets / source figures |

Site wiring: `docs/index.html`, `docs/_sidebar.md`, `docs/_navbar.md`. Math: `$inline$`, `$$display$$`.

## Adding a lab (preferred unit of coursework)

Lab IDs: `lab-NN-short-name` (e.g. `lab-02-counter-sv`).

1. Create `labs/<lab-id>/` with at least (skip this when the lab only runs `workspace` scripts, as IC101's labs do):
   - `README.md`: link to the Docsify writeup, how to run, the make targets (if any) and the file list. No teaching that repeats the writeup.
   - `src/`: HDL / Python / entrypoints
   - `data/`: small inputs (large binaries → Git LFS or external)
   - `requirements.txt` or tool notes when needed
2. Add `docs/labs/<lab-id>-overview.md`, titled `# Lab NN: Title`, with: what you'll build or measure (2–3 lines); Before you start (guide pages to read, setup); a time estimate; numbered parts, each with numbered steps and a closing "You should see …" check. Put each question at the step where it comes up, with its answer in a collapsed `<details><summary>Answer</summary>` block directly under it (leave a blank line after `</summary>` and before `</details>` so the Markdown inside renders). End the writeup with, in this order:
   1. `## Finishing`, opening with one "You're done when …" line that checks the student's own work, not a `PASS` the shipped files already give.
   2. `### Questions`, if there are any. Each one gets a collapsed answer or a pointer to the step that answers it.
   3. `### Submit`: what to submit, or "Nothing to submit."
   4. `## Going further (optional)`, if the lab has one.
   5. A last line, "Next on the Course path: read … / do …", naming the next row of the table.
3. Add a Do row to the Course path table in `docs/README.md` and link the writeup from `docs/_sidebar.md` in the same position, as `Lab NN: Title` (and `_navbar.md` only if it belongs in top nav). Every course uses the same table format. Read and Do are plain text, lab titles use a colon, and every Do row ends with one sentence on what the student will do:

   ```
   | # | | What | Time |
   |---|---|---|---|
   | 1 | Read | [Page](guide/page.md) · [Page](guide/page.md) | 45 min |
   | 2 | Do | [Lab 01: Title](labs/lab-01-...-overview.md). One sentence on what you'll do. | 1.5 h |
   ```
4. Cross-link: writeup → GitHub `labs/<lab-id>/`; package README → `docs/labs/<lab-id>-overview.md`.

Do not paste long HDL into Docsify pages. Reference the files under `labs/` instead.

## Adding a guide page

1. Add kebab-case Markdown under `docs/guide/` (e.g. `yosys-synth.md`).
2. Add it to a Read row of the Course path table in `docs/README.md`, and link it from `docs/_sidebar.md` in the same position.
3. Keep it reading only. When it needs the student to run something, put the steps in the matching lab writeup and leave a one-line pointer on the guide page.
4. Images under `docs/assets/img/` with paths relative to `docs/`.
5. Prefer relative Docsify links between pages; use GitHub URLs for `labs/` and `scripts/`.

## Pedagogy checklist (use when authoring)

- State **learning objectives** in student language (“You will synthesize a counter and inspect the netlist”).
- Assume a clone of this repo and the course’s documented workbench; do not bundle Docker in every lab unless the course already does.
- For EDA-heavy work (LibreLane / SKY130 / IIC-OSIC-TOOLS), document the **team workbench** steps in-course rather than inventing a one-off container story.
- Keep procedures copy-pasteable (`cd`, install, simulate/synth, check artifact).
- Define **expected results** (printout, waveform check, area/timing ballpark, golden hash) so students know they succeeded.
- Progress difficulty across labs; reuse naming and directory conventions so later labs feel familiar.
- Prefer small, inspectable designs over opaque blobs; when using IP or PDK artifacts, keep secrets and huge binaries out of git.

## Tooling norms

- Python helpers and graders: under `labs/<id>/src/` or `scripts/`; list entry points in the nearest `README.md`.
- SystemVerilog/Verilog: under `labs/<id>/src/` (or `rtl/` and `tb/` if you split them; stay consistent within the course).
- Heavy outputs (GDS, large FSDB/VCD, PDK caches): local `results/` or LFS, never under `docs/`.
- Preview docs locally: `npx docsify-cli serve docs` → http://localhost:3000

## What not to do

- Do not add maintainer-only pages to the published site (contributing guides, template notes, notation stubs “for debugging”).
- Do not put solution keys or rubrics in `docs/`.
- Do not replace student-facing content with template/bootstrap instructions; point humans at `CONTRIBUTING.md` / `TEMPLATE.md` only when they are bootstrapping or changing repo conventions.
- Do not change org assumptions: GitHub org is `uoftasic`; course id matches the repo name.

## Quick references

- Repo conventions: `CONTRIBUTING.md`
- Bootstrap tokens / Pages checklist: `TEMPLATE.md`
- Sample lab shape: `docs/labs/lab-03-launch-the-workbench-overview.md`
