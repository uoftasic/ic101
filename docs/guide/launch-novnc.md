# The workbench desktop (noVNC)

> To launch the desktop, follow [Lab 03](../labs/lab-03-launch-the-workbench-overview.md), Parts 1–3.
> This page explains what those steps do. If the desktop page is blank or port 80 is taken, see
> [Troubleshooting](../reference/troubleshooting.md).

The workbench is a container started from
[IIC-OSIC-TOOLS](https://github.com/iic-jku/IIC-OSIC-TOOLS), a toolchain image that IIC-JKU
maintains. You start it with a script from the team's `workspace` repo, and **noVNC** shows the
container's Linux desktop in your browser.

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

## Your files on your laptop and in the desktop

Mounting the folder means the container uses your `workspace` folder where it is, on your
laptop's disk, and doesn't copy it. Each file exists once: a file you save in the desktop is in
your `workspace` folder on your laptop, and a file you save in `workspace` on your laptop is under
`/foss/designs` in the desktop. The table shows the same two folders from each side:

| | Your `workspace` folder | AD101's Lab 01 folder, once you've added AD101 |
|---|---|---|
| On your laptop | Inside the folder where you ran `git clone` in Lab 03, Part 1 | `workspace/modules/ad101/labs/lab-01-signal-explorer` |
| In the desktop | `/foss/designs` | `/foss/designs/modules/ad101/labs/lab-01-signal-explorer` |

Each course you add with `mod add <course>` gets its own folder, `modules/<course>`, inside
`workspace`, as AD101's does in the table.

Since both sides work on the same files, you can edit course files in an editor on your laptop,
such as VS Code, and keep the desktop open beside it for the terminal and the GUI tools. Lab 03,
Part 6 sets this up, and shows you how to print the full path of `workspace` on your laptop.

On Windows, VS Code saves new files with Windows line endings (CRLF) unless you change its
`files.eol` setting. Python files run either way, but a shell script saved like that fails in the
desktop with `/usr/bin/env: ‘bash\r’: No such file or directory`. To fix it, run
`/foss/designs/scripts/fix_line_endings.sh` in a desktop terminal, which converts every `.sh`,
`.designinit`, `.magicrc` and `xschemrc` file under `/foss/designs` to Linux line endings (LF).

## Settings you can change

The script reads the environment variables below. You won't need any of them in Lab 03 unless
something else on your laptop is already using port 80.

| Variable | Default | What it changes |
|----------|---------|-----------------|
| `HOST_PORT` | `80` | The port on your laptop. With `HOST_PORT=8080` the desktop is at `http://localhost:8080/`. Use it when something else is already using port 80. |
| `VNC_PW` | `abc123` | The desktop password |
| `VNC_RESOLUTION` | `1280x800` | The desktop size, for example `1920x1080` |
| `DOCKER_TAG` | `2026.08` | Which image tag to pull |

On macOS and Linux you set them by putting them in front of the command, for example
`VNC_PW='your-password' HOST_PORT=8080 ./scripts/start_vnc.sh`.

## The desktop in your browser

noVNC serves a full Linux desktop in Chrome, Firefox or Edge, and the password is `abc123` unless
you set `VNC_PW`. Terminals, XSchem, Magic and the rest of the tools all open from that desktop,
and they run inside the container rather than on your laptop.

The desktop has its own clipboard, and noVNC can't read your laptop's, so a paste key pressed in
the desktop doesn't paste what you copied on your laptop. You hand text to the desktop through the
clipboard panel in the noVNC sidebar instead:

1. Copy the text on your laptop.
2. Click the small tab with an arrow, halfway down the left edge of the noVNC page, to open the
   sidebar, and click the clipboard icon. Click in the box that opens, press Ctrl+A to select any
   text already in it, then press Ctrl+V to paste your text over it (Cmd+A and Cmd+V on a Mac).
   The desktop gets everything in the box, so old text left in it would be pasted too.
3. Click back in the desktop, which sends the text to the desktop's clipboard. Then press
   **Ctrl+Shift+V** to paste it in a terminal, or **Ctrl+V** to paste it in gedit. Plain Ctrl+V
   doesn't paste in a terminal, and Ctrl+Shift+V doesn't paste in gedit. On a Mac, use the
   Control key for these. Cmd+V doesn't paste in the desktop.

Text you copy in the desktop appears in the panel's box, and you can copy it from there on your
laptop. Selecting text in the desktop, with the mouse or the keyboard, also puts it on the
desktop's clipboard and in the box in place of what was there. Once you've clicked back in the
desktop in step 3, paste before you select anything there.

## X11 instead of noVNC

On Linux, or on macOS with XQuartz, `./scripts/start_x.sh` shows the tools in windows on your own
desktop over X11, which can be faster than streaming a whole desktop to the browser. We use
noVNC in IC101 so that everyone sees the same interface.

Next: [What the smoke test checks](../guide/smoke-test.md).
