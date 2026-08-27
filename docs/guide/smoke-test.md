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

The script confirms these commands exist on your **`PATH`** (the list of folders your shell searches when you type a command name), that the **PDK** (Process Design Kit — the set of files describing how a specific chip fab's manufacturing process behaves, so tools can simulate and check designs against it) is present, and that module helpers work:

| Check | Role |
|-------|------|
| `ngspice` | Circuit simulation |
| `xschem` | Schematic capture |
| `magic` | Layout |
| `netgen` | LVS / netlist comparison |
| `yosys` | RTL synthesis |
| `sky130A` under `$PDK_ROOT` | SKY130 PDK |
| `mod` + `ic101_setup` | Course module navigation |

Success looks like lines of `OK  …` and a final **All checks passed**.

If the PDK line fails, the cause is almost never a missing PDK — SKY130 ships inside the image at `/foss/pdks/sky130A`. It is that the image starts on a *different* PDK (`ihp-sg13g2`), so the tools are looking in the wrong place. Fix it by sourcing the workspace environment, which selects SKY130 for everything:

```bash
. /foss/designs/.designinit
```

Then re-run the smoke test.

## After a pass

You are ready for either track. Keep the clone; later courses add more `modules/` folders (`mod add <course>`) — [**AD101**](https://uoftasic.com/ad101/) starts the analog track and [**DD101**](https://uoftasic.com/dd101/) starts the digital one.

Next: [Where each tool sits in the tapeout flow](guide/tapeout-flow.md).
