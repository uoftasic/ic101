# Lab 01: Terminal and git

You'll open a terminal on your own computer, install git if you don't have it, and check that git
runs. Every later lab starts by typing commands into this terminal.

## Before you start

- Read [Getting started](../guide/getting-started.md) and [Terminal and git](../guide/prerequisites.md).
- You need permission to install software on this computer.

Time: about 15 minutes, less if git is already installed.

## Part 1: Open a terminal

1. Open the terminal app for your OS:

   | OS | App | How to open it |
   |----|-----|----------------|
   | macOS | Terminal | Press `Cmd+Space`, type `Terminal`, press Enter |
   | Windows | Windows Terminal (or PowerShell) | Press the Windows key, type `Terminal` (or `PowerShell`), press Enter |
   | Linux | Varies by Linux distribution (distro), for example GNOME Terminal or Konsole | Press the Super (Windows) key, type `Terminal`, press Enter |

2. Click into the window so that what you type goes there.
3. When a step in a lab says "Run:", type or paste the command shown under it into the terminal,
   then press Enter.

You should see a window with a prompt, often ending in `$` or `>`, waiting for you to type.

## Part 2: Install git

Follow the steps for your OS.

### macOS

1. Run:

   ```bash
   git --version
   ```

   If it prints a version number, git is already installed and you can skip to Finishing.
2. If git isn't installed yet, macOS prompts you to install the **Xcode Command Line Tools**,
   which include git. Accept the prompt and wait for the install to finish.
3. Run `git --version` again.

### Windows

1. Download and run the installer from [git-scm.com](https://git-scm.com/download/win).
2. Accept the default options during the install. They're fine for this course.
3. Close any terminal you already had open, and open a new Windows Terminal or PowerShell window.
   A terminal that was open during the install won't find git.
4. Run:

   ```bat
   git --version
   ```

### Linux

1. Run:

   ```bash
   sudo apt update && sudo apt install -y git
   git --version
   ```

   `sudo` asks for your password. Nothing appears on screen while you type it; type it and press
   Enter. If your distro doesn't use `apt`, use its package manager instead, for example `dnf` on
   Fedora or `pacman` on Arch.

On every OS, you should see `git --version` print a version number, in a line like
`git version 2.34.1`. Your number may differ, and some systems add more text after it. If you see
`command not found` (on Windows, `'git' is not recognized...`), see
[Troubleshooting](../reference/troubleshooting.md#git-command-not-found).

## Finishing

You're done when `git --version` prints a version number, not `command not found`, in a terminal
on your own computer.

### Submit

Nothing to submit.

Next on the Course path: read [Why a containerized toolchain](../guide/why-containers.md) and
[What Docker needs](../guide/install-docker.md), then do
[Lab 02: Install Docker](../labs/lab-02-install-docker-overview.md).
