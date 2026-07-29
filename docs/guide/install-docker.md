# Install Docker Desktop

You need Docker so the workspace can pull and run the IIC-OSIC-TOOLS image.

## Requirements

- Roughly **20 GB free** disk (image + PDK + room to work)
- Ability to install Docker Desktop (or Docker Engine on Linux)
- On Windows: WSL2 backend recommended (Docker Desktop default)

## Per OS

### macOS

1. Download [Docker Desktop for Mac](https://www.docker.com/products/docker-desktop/).
2. Install and open Docker Desktop; wait until it reports **Engine running**.
3. In a terminal:

```bash
docker version
docker run --rm hello-world
```

Apple Silicon (M1/M2/M3) works; the IIC image is multi-arch. Prefer allocating at least **4 GB RAM** to Docker in Settings → Resources.

### Windows

1. Install [Docker Desktop for Windows](https://www.docker.com/products/docker-desktop/) with the **WSL2** backend.
2. Enable virtualization in BIOS/UEFI if Docker asks.
3. From PowerShell or WSL:

```bat
docker version
docker run --rm hello-world
```

If `hello-world` fails, fix Docker before cloning the workspace — later steps all depend on it.

### Linux

Install Docker Engine or Docker Desktop for your distro, add your user to the `docker` group (then log out/in), and verify with the same `docker run --rm hello-world` check.

## Disk and first pull

The first `start_vnc` run **pulls** `hpretl/iic-osic-tools:<tag>` (currently `2026.04` in the workspace scripts). That download is large; use a stable network. You can confirm tags on the [IIC-OSIC-TOOLS releases](https://github.com/iic-jku/IIC-OSIC-TOOLS/releases) page.

## Checklist

- [ ] `docker version` works without errors
- [ ] `docker run --rm hello-world` prints a success message
- [ ] Docker has enough disk/RAM for a multi-GB image

Next: [Launch noVNC](launch-novnc.md).
