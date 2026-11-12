# IC101 — Onboarding onto Tools

Set up the containerized open-source toolchain that every later course builds on. By the end, a
Linux desktop with the team's chip design (EDA) tools runs in a browser tab on your laptop. The
course calls this setup the workbench. A short check script, the smoke test, then confirms that
the tools and the SKY130 PDK work. The PDK (process design kit) is the set of files that describe
the manufacturing process the tools design against.

Part of the UofT ASIC Team education materials, published at <https://uoftasic.com/ic101/>. The
runnable tooling lives in the shared [`workspace`](https://github.com/uoftasic/workspace) repo,
not in this course repo.

## At a glance

| | |
|---|---|
| **Track** | Core (intro). IC101 comes before both the analog and the digital track. |
| **Who it's for** | Everyone starting the UofT ASIC courses |
| **Prerequisites** | None. Lab 01 starts from opening a terminal. |
| **Tools** | git, Docker, IIC-OSIC-TOOLS (the container image with the EDA tools), noVNC (shows the container's desktop in your browser) |
| **Time** | About 2–3 hours, much of it waiting for installs and the first image download |
| **Machine** | A laptop with roughly 15 GB of free disk space and permission to install software. On a Mac, you give Docker Desktop at least 4 GB of RAM in its settings (Lab 02, Part 1). |
| **Shared workspace** | The `workspace` repo. You clone it once, in Lab 03, and reuse it in every course that uses the tools. |

## Course path

Work down this table in order; the course ends with row 7. A *Read* row is guide pages:
explanations, with nothing to run. A *Do* row is one lab, where all the hands-on steps are. Each
lab's "Before you start" section lists the pages it expects you to have read.

| # | | Pages | Time |
|---|---|---|---|
| 1 | Read | [Getting started](guide/getting-started.md) · [Terminal and git](guide/prerequisites.md) | 10 min |
| 2 | Do | [Lab 01: Terminal and git](labs/lab-01-terminal-and-git-overview.md). Open a terminal, install git, check `git --version`. | 15 min |
| 3 | Read | [Why a containerized toolchain](guide/why-containers.md) · [What Docker needs](guide/install-docker.md) | 10 min |
| 4 | Do | [Lab 02: Install Docker](labs/lab-02-install-docker-overview.md). Install Docker and run `hello-world`. | 30 min–1 h |
| 5 | Read | [The workbench desktop](guide/launch-novnc.md) · [What the smoke test checks](guide/smoke-test.md) | 15 min |
| 6 | Do | [Lab 03: Launch the workbench](labs/lab-03-launch-the-workbench-overview.md). Clone `workspace`, open the desktop in your browser, pass the smoke test. | 30 min–1 h |
| 7 | Read | [Where each tool sits in the tapeout flow](guide/tapeout-flow.md) | 10 min |

When a step fails, look it up in [Troubleshooting](reference/troubleshooting.md).

## After IC101

[AD101](https://uoftasic.com/ad101/) starts the analog track and
[DD101](https://uoftasic.com/dd101/) starts the digital track. Every course is listed on the
portal at [edu.uoftasic.com](https://edu.uoftasic.com/).
