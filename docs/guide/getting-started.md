# Getting started

IC101 is the first course in the UofT ASIC Team's Internal Education Initiative, and it has no
prerequisites. By the end of it, the team's open-source EDA toolchain runs in a browser tab on
your own laptop, and a smoke test has confirmed that the tools and the SKY130 PDK work. Every
later course that uses the tools starts from this same setup.

## What you need

- A laptop with roughly 15 GB of free disk space. On a Mac, Docker also needs at least 4 GB of
  RAM.
- Permission to install software: Docker Desktop, and git if you don't already have it. On a
  school- or work-managed laptop this may need admin or IT permission.
- A stable network connection, because the toolchain image you download is several GB.

You don't need to have used a terminal before, since
[Lab 01](../labs/lab-01-terminal-and-git-overview.md) starts by opening one.

## What you'll set up

The setup has three layers, and each lab adds one:

1. git (Lab 01), to copy the team's `workspace` repo onto your laptop.
2. Docker (Lab 02), to download and run the toolchain container.
3. The `workspace` repo (Lab 03), whose launch script starts the IIC-OSIC-TOOLS container with
   your `workspace` folder mounted inside it, so that you can open the container's Linux desktop
   in your browser.

[Why a containerized toolchain](../guide/why-containers.md) explains why the team ships the tools
this way instead of asking you to install each one.

## This repo and the workspace repo

This `ic101` repo holds only the course pages you're reading. The Docker launch scripts, the file
that pins the PDK version, and the helper commands you use inside the container live in a
separate, shared repo called [`workspace`](https://github.com/uoftasic/workspace). You clone it
once in Lab 03 and keep the same clone for every later course.

## How the course works

The [home page](../index.md) has a Course path table. Work down it in order:

- A **Read** row is one or two guide pages, which explain the concepts and give you nothing to
  run.
- A **Do** row is one lab. Labs hold every hands-on step, in numbered parts, and each part ends
  with a "You should see" check so you know it worked before you move on.

When a step fails, look it up in [Troubleshooting](../reference/troubleshooting.md), which is
organized by the error you see.

Next: [Terminal and git](../guide/prerequisites.md).
