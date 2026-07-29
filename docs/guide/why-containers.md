# Why a containerized toolchain

Open-source ASIC flows bundle dozens of tools (schematic capture, SPICE, layout, DRC/LVS, synthesis, P&R). Installing each natively on Windows, macOS, and Linux is fragile: versions drift, PDKs disagree, and “works on my machine” becomes the course.

## What we standardize

We use the **[IIC-OSIC-TOOLS](https://github.com/iic-jku/IIC-OSIC-TOOLS)** Docker image (IIC-JKU). The team’s **workspace** repo wraps that image with:

- Launch scripts for **noVNC** (browser desktop) and optional X11
- A pinned **SKY130** PDK (`pdk/volare.lock`)
- Shared shell helpers (`common/.designinit`)
- Per-course starter folders under `modules/`

You install **only Docker**. Everything else runs inside one container, mounted so your files on the host appear at `/foss/designs` in the VM.

## What you get in the browser

noVNC serves a full Linux desktop in Chrome/Firefox/Edge. From there you can open terminals, XSchem, Magic, and the rest without installing EDA packages on the host OS.

Default login for the noVNC session uses password `abc123` (overridable via `VNC_PW` when you start the container).

## What this course is not

- Not a theory-heavy intro to semiconductors (later courses cover that)
- Not a substitute for ECE curriculum
- Not a per-course Docker image — **one workspace for every tool-heavy course**

Next: [Install Docker](install-docker.md).
