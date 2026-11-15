# Lab 01: Terminal and git

You'll open a terminal on your own computer, install git if you don't already have it, and check
that git runs. Every later lab starts with you typing commands into this terminal.

## Before you start

- Read [Getting started](../guide/getting-started.md) and [Terminal and git](../guide/prerequisites.md).
- You need permission to install software on this computer.

Time: about 15 minutes, or less if git is already installed.

## Part 1: Open a terminal

1. Open the terminal app for your OS:

   | OS | App | How to open it |
   |----|-----|----------------|
   | macOS | Terminal | Press `Cmd+Space`, type `Terminal`, press Enter |
   | Windows | Windows Terminal (or PowerShell) | Press the Windows key, type `Terminal` (or `PowerShell`), press Enter |
   | Linux | Varies by Linux distribution (distro), for example GNOME Terminal or Konsole | Press the Super (Windows) key, type `Terminal`, press Enter |

2. Click inside the window, so that what you type goes to the terminal and not to some other app.
3. Whenever a step in a lab says "Run:", type or paste the command shown under it into the
   terminal, then press Enter.

You should see a window with a prompt, which often ends in `$` or `>`, waiting for you to type.

## Part 2: Install git

Follow the steps for your OS, and skip the other two.

### macOS

1. Run:

   ```bash
   git --version
   ```

   If it prints a version number, git is already installed and you can skip to Finishing.
2. If git isn't installed yet, macOS instead offers to install the **Xcode Command Line Tools**,
   which include git. Accept the offer and wait for the install to finish.
3. Run `git --version` again.

### Windows

1. Download and run the installer from [git-scm.com](https://git-scm.com/download/win).
2. The installer's default options are fine for this course, so accept them as you go through it.
3. Close any terminal you already had open, and open a new Windows Terminal or PowerShell window.
   A terminal that was already open during the install won't find git, so you need a new one.
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

   `sudo` asks for your password. Nothing appears on screen while you type it, which is normal, so
   type it anyway and press Enter. If your distro doesn't use `apt`, use its own package manager
   instead, for example `dnf` on Fedora or `pacman` on Arch.

On every OS, you should see `git --version` print a version number, in a line like
`git version 2.34.1`. Your number may be different, and some systems add more text after it. If
you see `command not found` instead (on Windows, `'git' is not recognized...`), see
[Troubleshooting](../reference/troubleshooting.md#git-command-not-found).

## Finishing

You're done when `git --version`, run in a terminal on your own computer, prints a version number
rather than `command not found`.

### Submit

Nothing to submit.

Next on the Course path: read [Why a containerized toolchain](../guide/why-containers.md) and
[What Docker needs](../guide/install-docker.md), then do
[Lab 02: Install Docker](../labs/lab-02-install-docker-overview.md).
