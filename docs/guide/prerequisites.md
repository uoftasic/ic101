# Prerequisites: terminal + git

Before you touch Docker or any EDA tool, you need two things every later step
assumes you already have: a way to type commands, and **git**. This page is
the whole of what you need to know about both — just enough to get through
this course, not a full tutorial.

## What is a terminal?

A terminal (also called a "shell" or "command line") is a text window where
you type commands instead of clicking buttons. Every OS ships one:

| OS | App name | How to open it |
|----|----------|-----------------|
| macOS | **Terminal** | Press `Cmd+Space`, type `Terminal`, press Enter |
| Windows | **Windows Terminal** (or PowerShell) | Press the Windows key, type `Terminal` (or `PowerShell`), press Enter |
| Linux | Varies by distro (e.g. **GNOME Terminal**, **Konsole**) | Press the "Super"/Windows key, type `Terminal`, press Enter |

Once it's open you'll see a prompt (often ending in `$` or `>`) where you can
type. When a guide says "run this command," it means: click into the
terminal window and type (or paste) the command, then press Enter.

> [Screenshot: a terminal window open with a shell prompt visible]

## What is git?

**Git** is a tool for downloading and syncing a folder of files (called a
**repository**, or "repo") from a site like GitHub onto your computer. In
this course, git's only job is running one command — `git clone` — to copy
the team's shared **workspace** repo onto your machine. You will not need to
learn git beyond that for IC101.

## Install git

### macOS

Open a terminal and run:

```bash
git --version
```

If git isn't installed yet, macOS will offer to install the **Xcode Command
Line Tools** — accept that prompt and wait for it to finish, then run
`git --version` again.

### Windows

1. Download and run the installer from [git-scm.com](https://git-scm.com/download/win).
2. Accept the default options during install (they're fine for this course).
3. Open **Windows Terminal** and run:

```bat
git --version
```

### Linux

Open a terminal and run:

```bash
sudo apt update && sudo apt install -y git
git --version
```

(Use your distro's package manager if it isn't `apt` — e.g. `dnf` on
Fedora, `pacman` on Arch.)

## Checklist

- [ ] I can open a terminal on my computer
- [ ] `git --version` prints a version number (not "command not found")

Next: [Why containers](guide/why-containers.md).
