# Troubleshooting

Common setup issues for IC101 / the shared workspace. Each entry shows what
you'll see, why it happens, and exactly what to do about it.

## "I don't know how to open a terminal"

**Symptom:** A guide says "run this command" and you're not sure where to
type it.

**Why:** Every guide from [Install Docker](guide/install-docker.md) onward
assumes you have a terminal window open.

**Fix:** See [Prerequisites](guide/prerequisites.md) — it has per-OS steps
for opening a terminal, right at the top of the page.

## `git: command not found` (or `'git' is not recognized...` on Windows)

**Symptom:** Running `git clone ...` prints an error instead of downloading
anything.

**Why:** git isn't installed yet, or (on Windows) you need to open a new
terminal window after installing it.

**Fix:** Follow the git install steps in [Prerequisites](guide/prerequisites.md),
then open a **new** terminal window and try again — an already-open
terminal won't pick up a program you just installed.

## Docker won't start or `hello-world` fails

**Symptom:** Docker Desktop never shows **Engine running**, or
`docker run --rm hello-world` errors out instead of printing
`Hello from Docker!`.

**Why:** Docker itself isn't fully started yet, or a one-time OS setting
(WSL2 on Windows, group membership on Linux) hasn't been applied.

**Fix:**

- Confirm Docker Desktop shows **Engine running** before running any
  `docker` command — give it a minute after opening it.
- On Windows, ensure WSL2 is installed and selected as the Docker backend
  (see [Install Docker](guide/install-docker.md)).
- On Linux, check your user is in the `docker` group (run `groups` and look
  for `docker` in the output) and log out/back in after adding it.
- Free up disk space; large image pulls fail quietly on a full disk.

## `permission denied` running a `docker` command (Linux)

**Symptom:** A `docker` command fails with a message containing
`permission denied` instead of running.

**Why:** Your Linux user isn't in the `docker` group yet, so you don't have
permission to talk to Docker without `sudo`.

**Fix:**

```bash
sudo usermod -aG docker $USER
```

Then **log out and log back in** (group changes don't apply to an
already-open terminal) and try the command again.

## Port 80 already in use

**Symptom:** `start_vnc` fails, or the browser refuses to load
`http://localhost/`, because something else on your computer is already
using port 80.

**Why:** Only one program can listen on a given port at a time — something
else (often another local web server) got there first.

**Fix:** Start with another host port:

```bash
HOST_PORT=8080 ./scripts/start_vnc.sh
```

Then open `http://localhost:8080/`.

## Container starts but browser page is blank

**Symptom:** `start_vnc` finishes without errors, but `http://localhost/`
shows a blank or unreachable page.

**Why:** The desktop takes a little time to finish starting inside the
container after the script exits.

**Fix:**

- Wait ~30–60s after first pull/start for services to come up, then reload.
- Check `docker ps` for a container named `asic-edu-osic`.
- Inspect logs: `docker logs asic-edu-osic`.
- Confirm you're using the port you actually set (default `80`, or your
  `HOST_PORT`).

## Smoke test: tool not found

**Symptom:** `smoke_test.sh` reports a missing command (e.g. `ngspice`,
`magic`) instead of `OK`.

**Why:** The shared environment variables and PATH entries from
`.designinit` haven't been loaded into this terminal session yet.

**Fix:**

```bash
. /foss/designs/common/.designinit
```

Then confirm the workspace is mounted (`ls /foss/designs/scripts` should
list files) and re-run `/foss/designs/scripts/smoke_test.sh`. If tools are
still missing, re-pull the image tag the scripts expect (`DOCKER_TAG`,
default `2026.04`).

## Smoke test: `sky130A` missing

**Symptom:** The smoke test reports the SKY130 PDK as missing.

**Why:** Not because the PDK is absent — SKY130 ships inside the image at
`/foss/pdks/sky130A`. The image *starts on a different PDK* (`ihp-sg13g2`), so
`PDKPATH` and the ngspice and KLayout search paths all point somewhere else.

**Fix:** Source the workspace environment, which switches every one of those
variables over to SKY130, then re-run the smoke test:

```bash
. /foss/designs/.designinit
/foss/designs/scripts/smoke_test.sh
```

If you ever need to switch by hand, the image's own switcher is
`sak-pdk-script.sh`, and it must be **sourced** — run as a plain command it
prints the settings and changes nothing in your shell, which looks very much
like it worked:

```bash
. sak-pdk-script.sh sky130A
```

(Its own usage message calls it `sak-pdk`. There is no such command on `PATH`.)

## Copy/paste between host and noVNC

**Symptom:** `Ctrl+V` on your host keyboard doesn't paste into the noVNC
desktop.

**Why:** noVNC streams a remote desktop over the browser — your host
clipboard isn't automatically shared with it.

**Fix:** Use the noVNC clipboard panel (in the sidebar), or press
**Ctrl+Shift+V** to paste into the VM instead of the usual `Ctrl+V`.

## Still stuck

Ask on the team Discord and include: OS, Docker version, exact command, and
the failing log snippet (no secrets).
