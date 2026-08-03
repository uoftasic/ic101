# Launch the IIC-OSIC-TOOLS desktop (noVNC)

This step clones the shared **workspace** and starts the containerized EDA desktop in your browser.

## 1. Clone the workspace

```bash
git clone https://github.com/uoftasic/workspace.git
cd workspace
```

(Locally we call the folder `workspace`.)

## 2. Start noVNC

**macOS / Linux:**

```bash
./scripts/start_vnc.sh
```

**Windows:** double-click `scripts/start_vnc.bat`, or from a shell:

```bat
scripts\start_vnc.bat
```

The script will:

1. Pull `hpretl/iic-osic-tools:2026.04` (override with `DOCKER_TAG` if needed)
2. Run the container with your workspace mounted at `/foss/designs`
3. Expose the desktop on **http://localhost/** (port `80` by default; override with `HOST_PORT`)

Useful overrides:

```bash
VNC_RESOLUTION=1920x1080 ./scripts/start_vnc.sh
VNC_PW='your-password' HOST_PORT=8080 ./scripts/start_vnc.sh
```

## 3. Open the desktop

1. Browse to **http://localhost/** (or `http://localhost:<HOST_PORT>/`)
2. Password: **`abc123`** unless you set `VNC_PW`
3. You should see a Linux desktop suitable for XSchem, Magic, terminals, etc.

Copy/paste tip: use the clipboard control in the noVNC sidebar, or **Ctrl+Shift+V** to paste into the VM.

## 4. Optional: local X11 instead of noVNC

On Linux (or macOS with XQuartz), `./scripts/start_x.sh` can be faster than streaming the desktop. Prefer noVNC for the standard IC101 path so everyone shares the same UI.

## 5. Stop / restart

```bash
docker rm -f asic-edu-osic   # default container name from start_vnc
```

Then run `start_vnc` again. Your files under the workspace folder persist on the host.

## Checklist

- [ ] Workspace cloned into a `workspace` directory
- [ ] `start_vnc` completed without Docker errors
- [ ] Browser desktop loads and accepts the VNC password
- [ ] You can open a terminal inside the desktop

Next: [Smoke test](guide/smoke-test.md).
