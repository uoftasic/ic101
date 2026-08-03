# Install Docker Desktop

**Docker** is the program that downloads and runs the container described in
[Why containers](guide/why-containers.md). You need Docker installed and running
before anything else in this course will work.

## Requirements

- Roughly **20 GB free** disk (image + PDK + room to work)
- Ability to install Docker Desktop (or Docker Engine on Linux) — on a
  school- or work-managed laptop, this may require admin/IT permission
- On Windows: WSL2 backend recommended (Docker Desktop default). **WSL2**
  is a compatibility layer that lets Windows run a lightweight Linux
  environment behind the scenes — Docker needs it and will offer to set it
  up for you.

## Per OS

### macOS

1. Download [Docker Desktop for Mac](https://www.docker.com/products/docker-desktop/).
2. Open the downloaded file and drag Docker into Applications, then launch it.
3. Wait until the Docker icon in the menu bar stops animating and its status
   reads **Engine running** (click the icon to check).

   > [Screenshot: Docker Desktop menu bar icon showing "Engine running"]

4. Open a terminal (see [Prerequisites](guide/prerequisites.md) if you're not sure
   how) and run:

```bash
docker version
docker run --rm hello-world
```

You should see version info, then a paragraph starting with
`Hello from Docker!`. That message is your confirmation everything works —
if you see it, move on to the next page.

> [Screenshot: terminal showing the "Hello from Docker!" success message]

Apple Silicon (M1/M2/M3) works; the IIC image is multi-arch. In Docker
Desktop, go to **Settings → Resources** and allocate at least **4 GB RAM**.

### Windows

1. Install [Docker Desktop for Windows](https://www.docker.com/products/docker-desktop/).
   During setup, keep the default **"Use WSL2 instead of Hyper-V"** option
   checked.
2. If a window asks you to enable virtualization in BIOS/UEFI: restart your
   computer, enter BIOS/UEFI setup (usually by pressing `F2`, `Del`, or
   `Esc` right after powering on — the exact key is shown briefly on
   screen), find a setting called **Virtualization** / **Intel VT-x** /
   **AMD-V**, and enable it. Save and exit to boot back into Windows.
3. Open Docker Desktop and wait for it to say **Engine running** in the
   bottom-left corner.

   > [Screenshot: Docker Desktop window showing "Engine running" status]

4. Open **Windows Terminal** (or PowerShell) and run:

```bat
docker version
docker run --rm hello-world
```

You should see version info, then a `Hello from Docker!` message.

> [Screenshot: Windows Terminal showing the "Hello from Docker!" success message]

If `hello-world` fails, fix Docker before continuing — every later step
depends on it. Check [Troubleshooting](reference/troubleshooting.md).

### Linux

1. Install Docker Engine or Docker Desktop for your distro (see your
   distro's package manager or [docs.docker.com](https://docs.docker.com/engine/install/)).
2. Add your user to the `docker` group so you don't need `sudo` for every
   command:

```bash
sudo usermod -aG docker $USER
```

3. **Log out and log back in** (or restart) for the group change to take
   effect — it will not apply to your current terminal session.
4. Verify:

```bash
docker version
docker run --rm hello-world
```

You should see version info, then a `Hello from Docker!` message.

## Disk and first pull

The first `start_vnc` run **pulls** `hpretl/iic-osic-tools:<tag>` (currently
`2026.04` in the workspace scripts). "Pulling" means downloading the
container image — it's several GB, so use a stable network connection and
expect it to take a few minutes. You can confirm tags on the
[IIC-OSIC-TOOLS releases](https://github.com/iic-jku/IIC-OSIC-TOOLS/releases)
page.

## Checklist

- [ ] `docker version` works without errors
- [ ] `docker run --rm hello-world` prints a `Hello from Docker!` message
- [ ] Docker has enough disk/RAM for a multi-GB image

Next: [Launch noVNC](guide/launch-novnc.md).
