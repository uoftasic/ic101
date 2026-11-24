# Apple silicon Macs: Apple's container and the TigerVNC viewer

This page is an optional alternative to Docker Desktop and the browser desktop, for students on
an Apple silicon Mac. Instead of Docker Desktop you install Apple's own container runtime,
[`container`](https://github.com/apple/container), and instead of a browser tab the workbench
desktop opens in the TigerVNC viewer, a free app for your Mac. The workbench itself is the same:
the same IIC-OSIC-TOOLS image, the same container name, `asic-edu-osic`, and your `workspace`
folder at `/foss/designs`.

If you follow this page, it replaces [Lab 02](../labs/lab-02-install-docker-overview.md) and
Parts 2 and 3 of [Lab 03](../labs/lab-03-launch-the-workbench-overview.md). The order is:

1. Install Apple's container (this page), instead of Lab 02.
2. Install the TigerVNC viewer (this page).
3. Clone the workspace (Lab 03 Part 1).
4. Start the workbench and connect (this page), instead of Lab 03 Parts 2 and 3.
5. Run the smoke test (Lab 03 Part 4), which is the same as in the lab.
6. Restart the container (Lab 03 Part 5), using the commands under
   [Stopping and restarting](#stopping-and-restarting) on this page.
7. Edit a file from your Mac (Lab 03 Part 6), which is the same as in the lab.
8. Finish with Lab 03's Finishing section.

## Can your Mac use it?

You need a Mac with an Apple silicon chip (M1 or later) running macOS 26 or later. Apple doesn't
support `container` on older versions of macOS. To check, open **Apple menu → About This Mac**:
the **Chip** line should name an Apple M-series chip, and the **macOS** line should show version
26 or later. If your Mac doesn't qualify, use Docker Desktop and follow the labs as written.
Apple lists the requirements in the
[`container` README](https://github.com/apple/container#requirements).

Apple's `container` runs each container in a lightweight virtual machine of its own, where Docker
Desktop runs all of them inside one shared Linux virtual machine. TigerVNC is a VNC viewer: it
connects straight to the VNC server that runs the desktop inside the container, with no browser
in between. It comes from the same open-source project as that server. macOS has a VNC viewer of
its own, Screen Sharing, but it can't paste from your Mac into this desktop, so this page uses
TigerVNC.

## Before you start

- You need git, from [Lab 01](../labs/lab-01-terminal-and-git-overview.md). Lab 01 also shows you
  how to open a terminal on your Mac, which is where every command on this page runs until the
  desktop is up.
- Have roughly 15 GB of free disk and a stable network connection.
- Skip the Docker checks in Lab 03's "Before you start". They don't apply to this path.

## Install Apple's container

1. Go to the [`container` releases page](https://github.com/apple/container/releases) and, under
   the newest release, download the file whose name ends in `-installer-signed.pkg`.
2. Open the downloaded file and follow the installer. It asks for your Mac's password.
3. Open a new terminal on your Mac and run:

   ```bash
   container --version
   ```

You should see a version number, such as `container CLI version 1.7.1`.

You don't need to start anything else yourself. The first time the launch script runs, it starts
the `container` services and downloads the Linux kernel that containers run on. You'll see it
print `Starting Apple container services...` and `Installing kernel...`, and it doesn't ask you
anything.

## Install the TigerVNC viewer

1. Go to the [TigerVNC downloads](https://sourceforge.net/projects/tigervnc/files/stable/) on
   SourceForge and open the folder with the highest version number (1.16.2 when this page was
   written).
2. Download the file named `TigerVNC-<version>.dmg`, for example `TigerVNC-1.16.2.dmg`. The other
   files in the folder are for Windows and Linux.
3. Open the downloaded `.dmg`. In the window that appears, drag **TigerVNC** into your
   **Applications** folder (in the Finder sidebar).
4. Open **TigerVNC** from Applications once. macOS may ask you to confirm that you want to open
   an app downloaded from the internet; choose **Open**. Then quit it again.

You should see a small TigerVNC window asking for a **VNC server**. You'll connect to the
workbench in the next section, so you can close it for now.

## Start the workbench and connect

This replaces Lab 03 Parts 2 and 3. Clone the `workspace` repo first, as in
[Lab 03 Part 1](../labs/lab-03-launch-the-workbench-overview.md#part-1-clone-the-workspace), then
come back here. The launch script, `start_vnc_apple.sh`, is in that repo's `scripts` folder. If
`scripts/start_vnc_apple.sh` isn't there, your clone is older than the script, so run `git pull`
inside `workspace` to update it.

1. From inside your `workspace` folder, run:

   ```bash
   ./scripts/start_vnc_apple.sh
   ```

   The first run downloads the IIC-OSIC-TOOLS image, about 7 GB, which takes up about 11 GB once
   it's unpacked, so expect it to take several minutes. Later runs reuse the copy on your Mac.

   You should see the script end with these lines:

   ```text
   Opening the TigerVNC viewer on localhost::5901 (password: abc123)
   Stop it (frees its RAM):   container stop asic-edu-osic
   Shell into it:             container exec -it asic-edu-osic bash -l
   ```

2. A TigerVNC window opens and asks for a password. Enter `abc123`.

   If no TigerVNC window opened, open **TigerVNC** from Applications yourself, enter
   `localhost::5901` as the VNC server and click **Connect**. The two colons matter: they tell
   TigerVNC that `5901` is a port number.

You should see the same Linux desktop as in Lab 03 Part 3, with a column of icons down the left,
including **Terminal**, **XSchem** and **Magic**.

Now go on with
[Lab 03 Part 4](../labs/lab-03-launch-the-workbench-overview.md#part-4-run-the-smoke-test), and come
back to [Stopping and restarting](#stopping-and-restarting) when you reach Part 5.

## Copy and paste

TigerVNC passes text between your Mac's clipboard and the desktop's clipboard.

- To paste a command from a course page into the desktop, copy it on your Mac as usual, click in
  the TigerVNC window, then press **Ctrl+Shift+V** in a desktop terminal, as Lab 03 Part 4 says.
  Ignore Lab 03's mention of the noVNC sidebar, which TigerVNC doesn't have.
- Text you copy on the desktop lands on your Mac's clipboard, ready for **Cmd+V**.

## Stopping and restarting

Run these in a terminal on your Mac, not on the desktop.

- In [Lab 03 Part 5](../labs/lab-03-launch-the-workbench-overview.md#part-5-restart-the-container),
  use `container rm -f asic-edu-osic` in step 3 in place of `docker rm -f asic-edu-osic`, and
  `./scripts/start_vnc_apple.sh` in step 4. TigerVNC loses its connection when the container is
  removed. The script closes that window and opens a new one, so in step 5 enter the password in
  the new TigerVNC window instead of reloading `http://localhost/`.
- When you're done for the day, `container stop asic-edu-osic` stops the container and gives its
  memory back to your Mac.
- To start working again, run `./scripts/start_vnc_apple.sh`. As with `start_vnc.sh`, every run
  gives you a fresh container, and only your files under `/foss/designs` carry over.

## Settings you can change

`start_vnc_apple.sh` reads these environment variables. Set them in front of the command, for
example `CONTAINER_MEMORY=12g ./scripts/start_vnc_apple.sh`.

| Variable | Default | What it changes |
|----------|---------|-----------------|
| `CONTAINER_MEMORY` | Half of your Mac's RAM, between 4 and 16 GB | The container's RAM. Apple's default is 1 GB, which is too little for KLayout, Magic or LibreLane, so the script always sets it. |
| `CONTAINER_CPUS` | All but two of your Mac's CPU cores, and at least 2 | The container's CPU cores |
| `VNC_PW` | `abc123` | The desktop password |
| `VNC_RESOLUTION` | `1280x800` | The desktop size, for example `1920x1080` |
| `VNC_CLIENT` | `tigervnc` | `tigervnc` opens the TigerVNC viewer, `browser` opens the browser desktop instead, and `none` opens neither |
| `HOST_PORT` | `8080` | The port for the browser desktop, `http://localhost:8080/`. It isn't 80 as with Docker, because Apple's `container` can't use ports below 1024 without administrator rights. |
| `VNC_PORT` | `5901` | The port TigerVNC connects to |

## Common problems

- If the script stops with `ERROR: the 'container' command is not installed`, go back to
  [Install Apple's container](#install-apples-container).
- If the script prints `TigerVNC viewer not found in /Applications`, go back to
  [Install the TigerVNC viewer](#install-the-tigervnc-viewer). Until then, the same desktop is in
  your browser at <http://localhost:8080/>.
- If TigerVNC can't connect, run `container ls` and check that it lists `asic-edu-osic` with the
  state `running`. If it doesn't, `container logs asic-edu-osic` shows why the container stopped.
  Run `./scripts/start_vnc_apple.sh` again to start a fresh one.
- For problems inside the desktop, such as the smoke test or the `mod` command, the
  [Troubleshooting](troubleshooting.md) page applies as it is.
