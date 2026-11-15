# Why a containerized toolchain

A **container** is a self-contained bundle of software that runs the same way on every computer,
whether it runs Windows, macOS or Linux, without you installing each program separately. Think of
it as one pre-built package that holds an entire toolchain, ready to run.

Open-source ASIC flows use dozens of tools: schematic capture, SPICE, layout, DRC/LVS, synthesis,
and place and route (P&R). Installing each one natively on Windows, macOS and Linux is fragile.
Versions drift, PDKs disagree, and "works on my machine" becomes the course.

## What the team standardizes

The team uses the [IIC-OSIC-TOOLS](https://github.com/iic-jku/IIC-OSIC-TOOLS) Docker image,
maintained by IIC-JKU. The team's `workspace` repo wraps that image with:

- launch scripts for noVNC (a Linux desktop in your browser) and, optionally, X11
- a pinned SKY130 PDK (`pdk/volare.lock`)
- shared shell helpers (`common/.designinit`)
- a starter folder for each course, under `modules/`

You install only Docker. Everything else runs inside one container, and your `workspace` folder
on your laptop appears inside the container at `/foss/designs`. noVNC shows the container's
desktop in Chrome, Firefox or Edge, so you can open terminals, XSchem, Magic and the other tools
without installing any EDA package on your own operating system.
[The workbench desktop](../guide/launch-novnc.md) covers how it starts.

## What IC101 doesn't cover

- It isn't a theory-heavy introduction to semiconductors. Later courses cover that.
- It isn't a substitute for the ECE curriculum.
- It doesn't give each course its own Docker image. One workspace serves every tool-heavy course.

Next: [What Docker needs](../guide/install-docker.md).
