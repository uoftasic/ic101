# Lab 03: Launch the workbench

You'll clone the team's `workspace` repo, start the IIC-OSIC-TOOLS container, open its desktop in
your browser, and run the smoke test. Then you'll restart the container, check which of your
files survived, and edit one of them from your laptop while the desktop stays open. When the smoke
test prints `=== All checks passed ===` after that restart, your setup is ready for every later
course.

Other courses link here for their workbench setup, so if one of them sent you, do this whole lab
and then go back to that course.

## Before you start

- You need git and Docker on your laptop. In a terminal there, run:

  ```bash
  git --version
  docker run --rm hello-world
  ```

  The first should print a version number, and the second a paragraph starting with
  `Hello from Docker!`. If git is missing, do [Lab 01](../labs/lab-01-terminal-and-git-overview.md)
  first. If Docker isn't installed, do [Lab 02](../labs/lab-02-install-docker-overview.md). If it's
  installed but the command fails, Docker may still be starting: wait until Docker Desktop shows
  **Engine running** and try again. If it still fails, or you run Docker Engine on Linux without
  Docker Desktop, see
  [Troubleshooting](../reference/troubleshooting.md#docker-wont-start-or-hello-world-fails).
- On a Mac, give Docker Desktop at least 4 GB of RAM under **Settings → Resources**
  ([Lab 02](../labs/lab-02-install-docker-overview.md), Part 1).
- Read [The workbench desktop](../guide/launch-novnc.md) and
  [What the smoke test checks](../guide/smoke-test.md).
- Have roughly 15 GB of free disk and a stable network connection, because the first launch
  downloads an image that is several GB in size.

Time: 30 minutes to 1 hour, most of it waiting for the first download.

## Part 1: Clone the workspace

1. Open a terminal on your laptop.
2. Run:

   ```bash
   git clone https://github.com/uoftasic/workspace.git
   cd workspace
   ```

   The first command creates a folder named `workspace` inside the folder your terminal is in,
   and puts the team's scripts and configuration in it. The second moves your terminal into
   `workspace`. Remember which folder you ran this in, because you'll run the laptop commands in
   Parts 2 and 5 from inside `workspace`, and later courses start the workbench from it too.

You should see git print `Cloning into 'workspace'...` and finish without an error. If you get
`git: command not found`, go back to [Lab 01](../labs/lab-01-terminal-and-git-overview.md). If git
says `fatal: destination path 'workspace' already exists`, you've already cloned it in this folder,
so run `cd workspace` and use that clone.

## Part 2: Start the container

1. From inside `workspace`, start the container.

   On macOS or Linux:

   ```bash
   ./scripts/start_vnc.sh
   ```

   On Windows, run it from Windows Terminal or PowerShell:

   ```bat
   scripts\start_vnc.bat
   ```

   You can also double-click `scripts/start_vnc.bat` in File Explorer, but the window may close
   when the script ends, before you can read what it printed.

2. Wait for the script to finish. The first run downloads `hpretl/iic-osic-tools:2026.08` and can
   take several minutes.

You should see the script end with a block that starts `=== Open in your browser ===`, followed by
the desktop's address and password.

If the script fails because port 80 is in use, start it on another port (on macOS or Linux,
`HOST_PORT=8080 ./scripts/start_vnc.sh`) and use `http://localhost:8080/` in Part 3. Other
failures are in [Troubleshooting](../reference/troubleshooting.md).

## Part 3: Open the desktop

1. In your browser, go to <http://localhost/>, or `http://localhost:<HOST_PORT>/` if you set a
   port in Part 2.

   ![The noVNC password prompt](../assets/img/novnc-password-prompt.png)
   *The address bar shows plain `localhost`, which means the default port, 80. With
   `HOST_PORT=8080` it would show `localhost:8080`.*

2. Enter the password the script printed: `abc123`, unless you changed it with `VNC_PW`
   ([Settings you can change](../guide/launch-novnc.md#settings-you-can-change)).

You should see a Linux desktop with a column of icons down the left, including **Terminal**,
**XSchem** and **Magic**.

![The workbench desktop, loaded](../assets/img/novnc-desktop.png)
*The desktop, running inside the browser tab. `Connected to ...` in the top bar means the VNC
session is live. Every later course that uses the tools runs on this machine.*

If the page is blank or won't load, wait 30–60 s and reload. If it's still blank, see
[Troubleshooting](../reference/troubleshooting.md#container-starts-but-the-browser-page-is-blank).

## Part 4: Run the smoke test

Every command in this part runs in a terminal inside the noVNC desktop, not on your laptop.
Inside the container, your `workspace` folder is `/foss/designs`.

1. Open **Terminal** from the icons on the left of the desktop. To paste a command from this page
   into it, copy the command, paste it into the box under the clipboard icon in the noVNC sidebar,
   click back in the terminal, and press **Ctrl+Shift+V**. Plain `Ctrl+V` doesn't paste in the
   terminal. [The desktop in your browser](../guide/launch-novnc.md#the-desktop-in-your-browser)
   explains the clipboard panel. You can also type the commands.

2. Load the workspace environment:

   ```bash
   . /foss/designs/common/.designinit
   ```

   `.designinit` points the tools at the SKY130 PDK and defines the `mod` command you'll use in
   steps 4 and 5. The `.` and the space after it are part of the command, because the `.` is
   what loads the file into this terminal.

   You should see:

   ```text
   ASIC-EDU: PDK=sky130A  PDK_ROOT=/foss/pdks  designs=/foss/designs
             run 'mod' to list course modules, or 'mod <name>' to enter one.
   ```

   A new terminal on the desktop loads this file by itself, so you may already have seen these
   two lines when the terminal opened. Running it again does no harm, and it's also the fix if a
   terminal ever says `bash: mod: command not found`.

3. Run the smoke test:

   ```bash
   /foss/designs/scripts/smoke_test.sh
   ```

   You should see the same two `ASIC-EDU` lines, then:

   ```text
   === ASIC-EDU workspace smoke test ===
   OK  ngspice
   OK  xschem
   OK  magic
   OK  netgen
   OK  yosys
   OK  PDK sky130A at /foss/pdks/sky130A
       ngspice-47
   --- module helpers ---
   OK  mod function loaded
   OK  add_module.sh present
   OK  mod lists ic101_setup
   OK  mod ic101_setup
   === All checks passed ===
   ```

   The indented `ngspice-47` line is the ngspice version. If any line says `FAIL` or `WARN`, see
   [Smoke test: tool or helper not found](../reference/troubleshooting.md#smoke-test-tool-or-helper-not-found)
   or [Smoke test: PDK is not sky130A](../reference/troubleshooting.md#smoke-test-pdk-is-not-sky130a).

4. List the course modules:

   ```bash
   mod
   ```

   You should see `Available modules:` and, under it, `ic101_setup`.

5. Go to IC101's scratch folder:

   ```bash
   mod ic101_setup
   ```

   You should see `cwd: /foss/designs/modules/ic101_setup`.

## Part 5: Restart the container

Step 3 below is how you stop the workbench, and steps 4 and 5 are how you start it again at the
beginning of every later session. Before you restart it, you'll save two test files and predict
which of them the restart keeps.

1. In the desktop terminal, save one file in your workspace and one in the container's `/tmp`
   folder:

   ```bash
   echo "saved in the workspace" > /foss/designs/modules/ic101_setup/restart-test.txt
   echo "saved in the container" > /tmp/restart-test.txt
   ```

2. Write down which of the two files you expect to find after you remove the container and start
   a new one.
3. In a terminal on your laptop (not the desktop), stop and remove the container. The launch
   script named it `asic-edu-osic`:

   ```bash
   docker rm -f asic-edu-osic
   ```

   It prints the name, `asic-edu-osic`, when the container is gone.
4. From inside your `workspace` folder, start the container again as in Part 2:
   `./scripts/start_vnc.sh` on macOS or Linux, `scripts\start_vnc.bat` on Windows. This time the
   image is already on your computer, so there's nothing to download.
5. Reload <http://localhost/> (or your `HOST_PORT` address), enter the password, and open
   **Terminal** from the icons on the left. If the page is blank, wait 30–60 s and reload, as in
   Part 3.
6. Look for both files:

   ```bash
   cat /foss/designs/modules/ic101_setup/restart-test.txt
   cat /tmp/restart-test.txt
   ```

7. Run the smoke test again:

   ```bash
   /foss/designs/scripts/smoke_test.sh
   ```

In step 6 you should see the workspace file's text, then an error for the `/tmp` file:

```text
saved in the workspace
cat: /tmp/restart-test.txt: No such file or directory
```

In step 7, the smoke test should end with `=== All checks passed ===`, as in Part 4. Compare the
`cat` output with what you wrote down in step 2.

<details>
<summary>Answer</summary>

`/foss/designs` is your `workspace` folder on your laptop, mounted into the container, so the
first file is on your own disk and survives. `/tmp` exists only inside the container, and
`docker rm -f` deleted the container with everything in it.

</details>

Keep your course work under `/foss/designs`. Even if you skip step 3, `start_vnc` removes any old
`asic-edu-osic` container before it starts a new one, so every launch gives you a fresh container
and anything you saved outside `/foss/designs` is lost. Leave `restart-test.txt` where it is, since
`ic101_setup` is IC101's scratch folder and you'll edit the file in Part 6.

## Part 6: Edit a file from your laptop

Because `/foss/designs` is your `workspace` folder
([Your files on your laptop and in the desktop](../guide/launch-novnc.md#your-files-on-your-laptop-and-in-the-desktop)),
you can edit course files in an editor on your laptop and keep the desktop open for its terminal
and GUI tools. In this part you'll open `workspace` in VS Code, edit `restart-test.txt` there, and
read the change in the desktop. If you'd rather use another editor on your laptop, open the same
file in it and save it.

1. In the laptop terminal you used in Part 5, which is still in `workspace`, run:

   ```bash
   pwd
   ```

   It prints the full path of your `workspace` folder on your laptop, which is the folder you'll
   open in VS Code in step 3.

2. If you don't have VS Code, install it from [code.visualstudio.com](https://code.visualstudio.com/).
3. In VS Code, choose **File → Open Folder...** and open your `workspace` folder. If VS Code asks
   whether you trust the folder, choose to trust it: it's the team's `workspace` repo that you
   cloned. If VS Code offers to reopen the folder in a container, dismiss the offer; the courses
   use the desktop that `start_vnc` starts.
4. In the Explorer on the left of VS Code, open `modules`, then `ic101_setup`, and click
   `restart-test.txt`. It holds the line you saved from the desktop in Part 5,
   `saved in the workspace`.
5. Click on the empty second line, type `edited on my laptop`, and press Enter. Then press
   **Ctrl+S** (**Cmd+S** on macOS) to save. VS Code doesn't save a file until you do this, unless
   you've turned on **File → Auto Save**.
6. In the desktop terminal, run:

   ```bash
   cat /foss/designs/modules/ic101_setup/restart-test.txt
   ```

You should see both lines:

```text
saved in the workspace
edited on my laptop
```

If the second line is missing, go back to VS Code, press Ctrl+S, and run `cat` again.

As you work through later courses, keep VS Code and the browser tab with the desktop open side by
side: edit and save files in VS Code, then run them and use the GUI tools in the desktop.

## Finishing

You're done when, after the restart in Part 5, the smoke test ends with
`=== All checks passed ===` in a desktop terminal, and `cat` in the desktop shows the line you
added to `restart-test.txt` from your laptop in Part 6.

### Submit

Nothing to submit. Keep the `workspace` clone, though, because every later course that uses the
tools runs in it.

Next on the Course path: read [Where each tool sits in the tapeout flow](../guide/tapeout-flow.md).
If another course sent you here, go back to the page that sent you. Courses that use the tools
add their own files to your workspace with `mod add <course>`, which
[What the smoke test checks](../guide/smoke-test.md#course-modules-and-mod) describes.
