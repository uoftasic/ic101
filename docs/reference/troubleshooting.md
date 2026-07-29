# Troubleshooting

Common setup issues for IC101 / the shared workspace.

## Docker won’t start or `hello-world` fails

- Confirm Docker Desktop shows **Engine running**
- On Windows, ensure WSL2 is installed and selected as the Docker backend
- On Linux, check your user is in the `docker` group (`groups`) and re-login after adding it
- Free disk space; large image pulls fail quietly on full disks

## Port 80 already in use

Start with another host port:

```bash
HOST_PORT=8080 ./scripts/start_vnc.sh
```

Then open `http://localhost:8080/`.

## Container starts but browser page is blank

- Wait ~30–60s after first pull/start for services to come up
- Check `docker ps` for container `asic-edu-osic`
- Inspect logs: `docker logs asic-edu-osic`
- Try a hard refresh; confirm you’re using the port you set

## Smoke test: tool not found

- Source the environment first: `. /foss/designs/common/.designinit`
- Confirm the workspace is mounted: `ls /foss/designs/scripts`
- Re-pull the image tag your scripts expect (`DOCKER_TAG`, default `2026.04`)

## Smoke test: sky130A missing

Inside the container, install/fetch the PDK as the smoke script suggests (often `sak-pdk sky130A`), then re-run `/foss/designs/scripts/smoke_test.sh`.

## Copy/paste between host and noVNC

Use the noVNC clipboard panel, or **Ctrl+Shift+V** to paste into the VM. Host Ctrl+V often does not reach the remote desktop.

## Still stuck

Ask on the team Discord and include: OS, Docker version, exact command, and the failing log snippet (no secrets).
