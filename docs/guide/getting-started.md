# Getting started

IC101 is the entry point for the UofT ASIC Internal Education Initiative. There are **no prior courses required** — you need a laptop with roughly **20 GB free** and permission to install software (Docker Desktop, and git if you don't already have it). Never used a terminal before? Start at step 1 below; it walks you through it.

## Path through this course

| Step | Guide | Outcome |
|------|--------|---------|
| 1 | [Prerequisites](guide/prerequisites.md) | A terminal you can use, and git installed |
| 2 | [Why containers](guide/why-containers.md) | Know why we ship one Docker image instead of native installs |
| 3 | [Install Docker](guide/install-docker.md) | Docker Desktop running on your OS |
| 4 | [Launch noVNC](guide/launch-novnc.md) | Browser EDA desktop from the **workspace** |
| 5 | [Smoke test](guide/smoke-test.md) | Confirm tools + SKY130 PDK resolve |
| 6 | [Tapeout flow](guide/tapeout-flow.md) | Map tools to RTL → GDSII / analog flow |

## The workspace (not this repo)

This `ic101` repo is **docs**. The Docker scripts, PDK pin, and in-container helpers live in the shared **workspace**:

```bash
# Clone into a folder named workspace (local name we use on the team)
git clone https://github.com/uoftasic/workspace.git
cd workspace
```

| Path in workspace | Purpose |
|-------------------|---------|
| `scripts/start_vnc.sh` / `.bat` | Launch IIC-OSIC-TOOLS with noVNC |
| `scripts/smoke_test.sh` | Health-check tools inside the container |
| `common/.designinit` | Environment + SKY130 setup |
| `modules/ic101_setup/` | Scratch space for this course |
| `pdk/` | Pinned PDK version |

Later courses add their own folders under `modules/` (in the container: `mod add <course>` after sourcing `.designinit`). You keep the same clone.

## After IC101

Pick a track from the [portal](https://edu.uoftasic.com/): Analog (AD101…) or Digital (DD101…). Tool-heavy courses reuse this workspace; early web-sim courses do not need Docker again until their labs say so.
