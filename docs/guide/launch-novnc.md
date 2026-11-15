# The workbench desktop (noVNC)

> To launch the desktop, follow [Lab 03](../labs/lab-03-launch-the-workbench-overview.md), Parts 1–3.
> This page explains what those steps do. If the desktop page is blank or port 80 is taken, see
> [Troubleshooting](../reference/troubleshooting.md).

The workbench is the [IIC-OSIC-TOOLS](https://github.com/iic-jku/IIC-OSIC-TOOLS) container, a
toolchain image maintained by IIC-JKU. You start it with a script from the team's `workspace`
repo, and **noVNC** shows the container's Linux desktop in your browser.

## The workspace repo

You clone the `workspace` repo once, into a folder named `workspace`, and keep that clone for
every later course. These are the parts IC101 uses:

| Path in `workspace` | Purpose |
|---------------------|---------|
| `scripts/start_vnc.sh` / `.bat` | Launches IIC-OSIC-TOOLS with noVNC |
| `scripts/smoke_test.sh` | Checks that the tools inside the container work |
| `common/.designinit` | Sets up the environment and SKY130 |
| `modules/ic101_setup/` | Scratch space for this course |
| `pdk/` | `volare.lock`, which records the PDK version the team uses. The PDK itself ships inside the image, at `/foss/pdks/sky130A`. |

Later courses add their own folders under `modules/` with `mod add <course>`, a command described in
[What the smoke test checks](../guide/smoke-test.md#course-modules-and-mod).

## What `start_vnc` does

`start_vnc.sh` (macOS and Linux) and `start_vnc.bat` (Windows) do the same three things:

1. Pull the image `hpretl/iic-osic-tools:2026.08`. The first run downloads several GB, which can
   take several minutes, and later runs reuse the copy already on your computer.
2. Run the container, named `asic-edu-osic`, with your `workspace` folder mounted at
   `/foss/designs`. Anything you save under `/foss/designs` is a file in your `workspace` folder
   on your laptop, so it survives when the container is stopped or removed.
3. Expose the desktop at <http://localhost/>, on port 80 by default.

Running `docker rm -f asic-edu-osic` on your laptop stops and removes the container, and running
`start_vnc` again brings it back. You'll try both in Lab 03, Part 5.

## Settings you can change

The script reads the environment variables below, though you don't need any of them for Lab 03.

| Variable | Default | What it changes |
|----------|---------|-----------------|
| `HOST_PORT` | `80` | The port on your laptop. With `HOST_PORT=8080` the desktop is at `http://localhost:8080/`. Use it when something else is already using port 80. |
| `VNC_PW` | `abc123` | The desktop password |
| `VNC_RESOLUTION` | `1280x800` | The desktop size, for example `1920x1080` |
| `DOCKER_TAG` | `2026.08` | Which image tag to pull |

On macOS and Linux you set them by putting them in front of the command, for example
`VNC_PW='your-password' HOST_PORT=8080 ./scripts/start_vnc.sh`.

## The desktop in your browser

noVNC serves a full Linux desktop in Chrome, Firefox or Edge. The password is `abc123` unless you
set `VNC_PW`. From that desktop you can open terminals, XSchem, Magic and the other tools, so you
never have to install an EDA package on your own operating system.

Plain `Ctrl+V` doesn't paste text from your laptop into the desktop. To paste there, press
**Ctrl+Shift+V**, or use the clipboard icon in the noVNC sidebar.

## X11 instead of noVNC

On Linux, or on macOS with XQuartz, `./scripts/start_x.sh` shows the tools in windows on your own
desktop over X11, which can be faster than streaming a whole desktop to the browser. We use
noVNC in IC101 so that everyone sees the same interface.

Next: [What the smoke test checks](../guide/smoke-test.md).
