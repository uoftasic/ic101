# Scripts

Utilities for **IC101 - Introduction to IC Tools & Workspace** under the UofT ASIC org (`uoftasic`).

## Entry points

| Script | Purpose |
|--------|---------|
| `init-template.py` | Fill `ic101` / title / description after using the template |
| `check_site.py` | Check that every local link and `#anchor` in the rendered site resolves. `.github/workflows/site.yml` runs it on `docs/_site` |

## Usage

```bash
# From repo root, after rendering the site
python3 scripts/check_site.py docs/_site

python3 scripts/init-template.py \
  --id dd103 \
  --title "DD103 — RTL on FPGAs & ASICs" \
  --description "RTL on FPGAs and open-source ASIC flows"
```

## Conventions

- Prefer Python; HDL tooling belongs in `labs/` or the shared workbench.
- No secrets in the repo; use `.env.example` if configuration is needed.
- Document new scripts here when you add them.
