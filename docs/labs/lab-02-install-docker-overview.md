# Lab 02: Install Docker

In this lab you'll install Docker Desktop (or Docker Engine on Linux) and run Docker's
`hello-world` test to show that it works. Lab 03 runs the course workbench in Docker, so it needs
Docker installed and running.

## Before you start

- Finish [Lab 01](../labs/lab-01-terminal-and-git-overview.md), so that you know how to open a
  terminal.
- Read [Why a containerized toolchain](../guide/why-containers.md) and
  [What Docker needs](../guide/install-docker.md).
- Check that you have roughly 15 GB of free disk and permission to install software. On a
  school- or work-managed laptop you may need admin or IT permission.

Time: 30 minutes to 1 hour. Allow longer on Windows if you have to change a BIOS setting.

## Part 1: Install Docker

Follow the steps for your operating system.

### macOS

1. Download [Docker Desktop for Mac](https://www.docker.com/products/docker-desktop/).
2. Open the downloaded file, drag Docker into Applications, then launch it.
3. Wait until the Docker icon in the menu bar stops animating, then click the icon. Its status
   should read **Engine running**.
4. In Docker Desktop, open **Settings → Resources** and allocate at least 4 GB of RAM.

### Windows

1. Install [Docker Desktop for Windows](https://www.docker.com/products/docker-desktop/). During
   setup, leave the default **Use WSL2 instead of Hyper-V** option checked.
2. If a window asks you to enable virtualization in BIOS/UEFI:
   1. Restart your computer and enter the BIOS/UEFI setup. You get there by pressing a key right
      after the computer powers on, usually `F2`, `Del` or `Esc`; the exact key is shown briefly
      on screen as it starts.
   2. Find the setting called **Virtualization**, **Intel VT-x** or **AMD-V**, and enable it.
   3. Save and exit. The computer boots back into Windows.
3. Open Docker Desktop and wait until it shows **Engine running** in the bottom-left corner.

### Linux

1. Install Docker Engine or Docker Desktop for your distro, from your distro's package manager or
   following [docs.docker.com](https://docs.docker.com/engine/install/).
2. Add your user to the `docker` group, so you don't need `sudo` for every `docker` command:

   ```bash
   sudo usermod -aG docker $USER
   ```

3. Log out and log back in, or restart. A group change only takes effect when you log in, so it
   doesn't apply to the session you're already in.

You should see **Engine running** in Docker Desktop. If you're on Linux with Docker Engine, run
`groups` after you log back in, and you should see `docker` in the list.

## Part 2: Run hello-world

1. Open a terminal. On Windows, use Windows Terminal or PowerShell.
2. Run:

   ```bash
   docker version
   docker run --rm hello-world
   ```

You should see version information from `docker version`, with a `Client` section and a `Server`
section, and then `hello-world` prints a paragraph starting with `Hello from Docker!`. If the
`Server` section is missing or shows an error, the Docker engine hasn't started yet, so wait for
**Engine running** and try again. On Linux, an error that mentions `permission denied` means the
`docker` group change from Part 1 hasn't applied yet, and logging out and back in will fix it.

If `hello-world` fails, fix Docker before you go on, because every later step in the course
depends on it. Start with the
[Troubleshooting](../reference/troubleshooting.md#docker-wont-start-or-hello-world-fails) page.

## Finishing

You're done when `docker run --rm hello-world` prints `Hello from Docker!` on your own computer,
you have roughly 15 GB of free disk for an image several gigabytes in size, and, on a Mac, Docker
Desktop has at least 4 GB of RAM.

### Submit

Nothing to submit.

Next on the Course path: read [The workbench desktop](../guide/launch-novnc.md) and
[What the smoke test checks](../guide/smoke-test.md), then do
[Lab 03: Launch the workbench](../labs/lab-03-launch-the-workbench-overview.md).
