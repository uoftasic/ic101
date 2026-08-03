# Run the smoke test

With the noVNC desktop open, verify that the EDA tools and SKY130 PDK resolve inside the container.

## In the container terminal

```bash
. /foss/designs/common/.designinit     # load environment + PDK paths + mod
/foss/designs/scripts/smoke_test.sh    # health-check tools + module helpers
mod                                    # list course modules (optional)
```

`mod ic101_setup` jumps into this course’s scratch folder under `/foss/designs/modules/ic101_setup`.

For a later course (for example AD101), after sourcing `.designinit`:

```bash
mod add ad101    # clones github.com/uoftasic/ad101 into modules/ad101
mod ad101        # if it is already cloned
```

You can also run `./scripts/add_module.sh ad101` on the **host** from your workspace clone — same folder, bind-mounted into the container.

## What the smoke test checks

The script confirms these commands exist on `PATH`, that the PDK is present, and that module helpers work:

| Check | Role |
|-------|------|
| `ngspice` | Circuit simulation |
| `xschem` | Schematic capture |
| `magic` | Layout |
| `netgen` | LVS / netlist comparison |
| `yosys` | RTL synthesis |
| `sky130A` under `$PDK_ROOT` | SKY130 PDK |
| `mod` + `ic101_setup` | Course module navigation |

Success looks like lines of `OK  …` and a final **All checks passed**. If `sky130A` is missing, follow the script’s hint (typically `sak-pdk sky130A` inside the image) and re-run.

## After a pass

You are ready for any track that uses the workspace. Keep the clone; later courses add more `modules/` folders (`mod add <course>`).

Next: [Where each tool sits in the tapeout flow](guide/tapeout-flow.md).
