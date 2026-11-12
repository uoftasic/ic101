# The workbench desktop (noVNC)

> To launch the desktop, follow [Lab 03](labs/lab-03-launch-the-workbench-overview.md), Parts 1–3.
> This page explains what those steps do.

The workbench is the [IIC-OSIC-TOOLS](https://github.com/iic-jku/IIC-OSIC-TOOLS) container, the
toolchain image maintained by IIC-JKU. A script from the team's `workspace` repo starts it, and
**noVNC** shows its Linux desktop in your browser.

## The workspace repo

You clone the `workspace` repo once, into a folder named `workspace`, and keep that clone for
every later course. These are the parts IC101 uses:

| Path in `workspace` | Purpose |
|---------------------|---------|
| `scripts/start_vnc.sh` / `.bat` | Launch IIC-OSIC-TOOLS with noVNC |
| `scripts/smoke_test.sh` | Health-check the tools inside the container |
| `common/.designinit` | Environment and SKY130 setup |
| `modules/ic101_setup/` | Scratch space for this course |
| `pdk/` | `volare.lock`, which records the PDK version the team uses. The PDK itself ships inside the image, at `/foss/pdks/sky130A`. |

Later courses add their own folders under `modules/` with `mod add <course>`, described in
[What the smoke test checks](guide/smoke-test.md#course-modules-and-mod).

## What `start_vnc` does

`start_vnc.sh` (macOS and Linux) and `start_vnc.bat` (Windows) do the same three things:

1. Pull `hpretl/iic-osic-tools:2026.08`. The first run downloads several GB and can take several
   minutes. Later runs reuse the copy already on your computer.
2. Run the container, named `asic-edu-osic`, with your `workspace` folder mounted at
   `/foss/designs`. Anything you save under `/foss/designs` is a file in your `workspace` folder
   on your laptop, so it survives when the container is stopped or removed.
3. Expose the desktop at <http://localhost/>, on port 80 by default.

Stopping the container is one command, `docker rm -f asic-edu-osic`, run on your laptop. Running
`start_vnc` again brings it back. Lab 03, Part 5 has you try it.

## Settings you can change

The script reads these environment variables. You don't need any of them for Lab 03.

| Variable | Default | What it changes |
|----------|---------|-----------------|
| `HOST_PORT` | `80` | The port on your laptop. With `HOST_PORT=8080` the desktop is at `http://localhost:8080/`. Use it when something else already has port 80. |
| `VNC_PW` | `abc123` | The desktop password |
| `VNC_RESOLUTION` | `1280x800` | The desktop size, for example `1920x1080` |
| `DOCKER_TAG` | `2026.08` | Which image tag to pull |

On macOS and Linux you set them in front of the command, for example:

```bash
VNC_RESOLUTION=1920x1080 ./scripts/start_vnc.sh
VNC_PW='your-password' HOST_PORT=8080 ./scripts/start_vnc.sh
```

## The desktop in your browser

noVNC serves a full Linux desktop in Chrome, Firefox or Edge. The password is `abc123` unless you
set `VNC_PW`. From the desktop you open terminals, XSchem, Magic and the other tools, without installing any
EDA package on your own operating system.

Pasting from your laptop into the desktop needs a different key: plain `Ctrl+V` doesn't paste
there. Press **Ctrl+Shift+V** to paste into the desktop, or use the clipboard icon in the noVNC
sidebar.

## X11 instead of noVNC

On Linux, or on macOS with XQuartz, `./scripts/start_x.sh` shows the tools in windows on your own
desktop over X11, which can be faster than streaming a whole desktop to the browser. IC101 uses
noVNC so that everyone has the same interface.

Next: [What the smoke test checks](guide/smoke-test.md).
