# What Docker needs

**Docker** is the program that downloads and runs the container described in
[Why a containerized toolchain](../guide/why-containers.md). Nothing else in this course works
until Docker is installed and running. You'll install it in
[Lab 02](../labs/lab-02-install-docker-overview.md). This page explains what the installer asks of
your computer, and why.

## Disk, memory and permission

- Roughly 15 GB of free disk: the image, the PDK, and room to work.
- Permission to install Docker Desktop, or Docker Engine on Linux. On a school- or work-managed
  laptop this may need admin or IT permission.
- On a Mac, Docker Desktop needs at least 4 GB of RAM, which you set under
  **Settings → Resources**. Apple Silicon Macs (M1/M2/M3) work, because the IIC-OSIC-TOOLS image
  is multi-arch.

## Windows: WSL2 and virtualization

**WSL2** is a compatibility layer that lets Windows run a lightweight Linux environment behind the
scenes. Docker Desktop needs it, uses it by default, and offers to set it up for you. Keep that
default: the installer's **Use WSL2 instead of Hyper-V** option stays checked.

Docker also needs your processor's virtualization support switched on in the BIOS/UEFI setup, the
settings screen your computer shows before Windows starts. The setting is usually called
Virtualization, Intel VT-x or AMD-V. If it's off, Docker shows a window asking you to enable it,
and Lab 02 walks you through it.

## Linux: the docker group

On Linux, your user has to be in the `docker` group to talk to Docker without `sudo`. Without it,
`docker` commands fail with `permission denied`. A group change only applies after you log out
and back in. Terminals that were already open don't pick it up.

## Pulling the image

**Pulling** an image means downloading it. The first time you start the workbench in Lab 03, the
launch script pulls `hpretl/iic-osic-tools:<tag>`, where the tag is currently `2026.08` in the
workspace scripts. The image is several GB, so use a stable network connection and expect it to
take a few minutes. The [IIC-OSIC-TOOLS releases](https://github.com/iic-jku/IIC-OSIC-TOOLS/releases)
page lists the tags.

## The hello-world check

Lab 02 ends with `docker run --rm hello-world`. When Docker is working, that command prints a
message starting with `Hello from Docker!`.

Next: [Lab 02: Install Docker](../labs/lab-02-install-docker-overview.md).
