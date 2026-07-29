# Run the smoke test

With the noVNC desktop open, verify that the EDA tools and SKY130 PDK resolve inside the container.

## In the container terminal

```bash
. /foss/designs/common/.designinit     # load environment + PDK paths
/foss/designs/scripts/smoke_test.sh    # health-check tools
mod                                    # list course modules (optional)
```

`mod ic101_setup` jumps into this course’s scratch folder under `/foss/designs/modules/ic101_setup`.

## What the smoke test checks

The script confirms these commands exist on `PATH` and that the PDK is present:

| Check | Role |
|-------|------|
| `ngspice` | Circuit simulation |
| `xschem` | Schematic capture |
| `magic` | Layout |
| `netgen` | LVS / netlist comparison |
| `yosys` | RTL synthesis |
| `sky130A` under `$PDK_ROOT` | SKY130 PDK |

Success looks like lines of `OK  …` and a final **All checks passed**. If `sky130A` is missing, follow the script’s hint (typically `sak-pdk sky130A` inside the image) and re-run.

## After a pass

You are ready for any track that uses the workspace. Keep the clone; later courses add more `modules/` folders.

Next: [Where each tool sits in the tapeout flow](tapeout-flow.md).
