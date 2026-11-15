# IC101 — Onboarding onto Tools

In IC101 you set up the containerized open-source toolchain that later courses build on. By
the end you'll have a Linux desktop with the team's chip design (EDA) tools running in a browser
tab on your laptop, a setup the course calls the workbench. A short check script called
the smoke test then confirms that the tools and the SKY130 PDK work. The PDK (process design kit)
is the set of files that describes the manufacturing process the tools design against.

IC101 is part of the UofT ASIC Team education materials, published at
<https://uoftasic.com/ic101/>. The runnable tooling lives in the shared
[`workspace`](https://github.com/uoftasic/workspace) repo rather than in this course repo.

## At a glance

| | |
|---|---|
| **Track** | Core (intro): IC101 comes before both the analog and the digital track. |
| **Who it's for** | Everyone starting the UofT ASIC courses |
| **Prerequisites** | None; Lab 01 starts from opening a terminal. |
| **Tools** | git, Docker, IIC-OSIC-TOOLS (the container image with the EDA tools), noVNC (shows the container's desktop in your browser) |
| **Time** | About 2–3 hours, much of it waiting for installs and the first image download |
| **Machine** | A laptop with roughly 15 GB of free disk space and permission to install software, and a stable network connection, because the toolchain image is several GB. On a Mac you'll also give Docker Desktop at least 4 GB of RAM in its settings (Lab 02, Part 1). |
| **Shared workspace** | The `workspace` repo, which you clone once in Lab 03 and reuse in every course that uses the tools. |

## Course path

Work down this table in order; the course ends with row 7. A Read row points you to guide pages,
which explain things and have nothing to run. A Do row is one lab, and every hands-on step in the
course is in a lab. Each lab's "Before you start" section lists the pages it expects you to have
read.

| # | | What | Time |
|---|---|---|---|
| 1 | Read | [Getting started](guide/getting-started.md) · [Terminal and git](guide/prerequisites.md) | 10 min |
| 2 | Do | [Lab 01: Terminal and git](labs/lab-01-terminal-and-git-overview.md). Open a terminal, install git and check that `git --version` prints a version. | 15 min |
| 3 | Read | [Why a containerized toolchain](guide/why-containers.md) · [What Docker needs](guide/install-docker.md) | 10 min |
| 4 | Do | [Lab 02: Install Docker](labs/lab-02-install-docker-overview.md). Install Docker and run its `hello-world` test. | 30 min–1 h |
| 5 | Read | [The workbench desktop](guide/launch-novnc.md) · [What the smoke test checks](guide/smoke-test.md) | 15 min |
| 6 | Do | [Lab 03: Launch the workbench](labs/lab-03-launch-the-workbench-overview.md). Clone `workspace`, open the desktop in your browser, pass the smoke test, then restart the container and check which of your files survived. | 30 min–1 h |
| 7 | Read | [Where each tool sits in the tapeout flow](guide/tapeout-flow.md) | 10 min |

If a step fails, look it up in [Troubleshooting](reference/troubleshooting.md).

## After IC101

[AD101](https://uoftasic.com/ad101/) starts the analog track and
[DD101](https://uoftasic.com/dd101/) starts the digital track. You'll find every course listed on
the portal at [edu.uoftasic.com](https://edu.uoftasic.com/).
