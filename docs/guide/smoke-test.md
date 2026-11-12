# What the smoke test checks

The **smoke test** is a script in the workspace, `scripts/smoke_test.sh`, that checks the EDA tools
and the SKY130 PDK resolve inside the container. You'll run it in
[Lab 03](labs/lab-03-launch-the-workbench-overview.md), Part 4. This page explains what it checks
and what a failure usually means.

## Two terms

- Your **`PATH`** is the list of folders your shell searches when you type a command name. A tool
  "resolves" when typing its name finds it on the `PATH`.
- A **PDK** (process design kit) is the set of files that describe how one chip fab's
  manufacturing process behaves, so tools can simulate and check designs against it. The courses
  use SKY130, an open PDK. The tools call it `sky130A`, and its files are in
  `/foss/pdks/sky130A` inside the container (`$PDK_ROOT` is `/foss/pdks`).

## The environment file

Inside the container, your `workspace` folder is `/foss/designs`. The file
`/foss/designs/common/.designinit` sets up the shell for the courses: it sets the environment
variables and `PATH` entries the tools read, points the PDK paths at SKY130, and defines the
`mod` command. Lab 03 has you load it with `. /foss/designs/common/.designinit` before running
the smoke test. The leading `.` means "run this file in my current shell", so its settings stay
in the terminal you're using.

## The checks

| Check | Role |
|-------|------|
| `ngspice` | Circuit simulation |
| `xschem` | Schematic capture |
| `magic` | Layout |
| `netgen` | LVS (netlist comparison) |
| `yosys` | RTL synthesis |
| `sky130A` under `$PDK_ROOT` | The SKY130 PDK is present and is the one in use |
| `mod`, `add_module.sh`, `ic101_setup` | The course module helpers work: `mod` is defined, `add_module.sh` is present, and `mod` lists and enters this course's `ic101_setup` folder |

A pass is a column of `OK` lines, plus an ngspice version line and a `--- module helpers ---`
heading, ending with `=== All checks passed ===`.

## When the PDK check fails

The cause is almost never a missing PDK. SKY130 ships inside the image at `/foss/pdks/sky130A`.
The image starts on a different PDK, `ihp-sg13g2`, so the tools look in the wrong place until
the workspace environment switches everything over to SKY130. Loading `.designinit` does that
switch. [Troubleshooting](reference/troubleshooting.md#smoke-test-pdk-is-not-sky130a) has the
exact messages and the fix.

## Course modules and `mod`

Each course keeps its files in a folder under `modules/` in your workspace, which the container
sees as `/foss/designs/modules/`. After you load `.designinit`, the `mod` command moves between
them:

| Command | What it does |
|---------|--------------|
| `mod` | List the course modules |
| `mod ic101_setup` | Go to this course's scratch folder, `/foss/designs/modules/ic101_setup` |
| `mod add ad101` | Clone `github.com/uoftasic/ad101` into `modules/ad101` (a later course) |
| `mod ad101` | Go to `modules/ad101`, once it's cloned |

On your laptop, `./scripts/add_module.sh ad101`, run from your `workspace` clone, does the same
as `mod add ad101`. It's the same folder, mounted into the container.

Next: [Lab 03: Launch the workbench](labs/lab-03-launch-the-workbench-overview.md).
