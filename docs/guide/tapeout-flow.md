# Where each tool sits in the tapeout flow

This page is a map of the tools you just checked. The design work itself comes in later
courses. **Tapeout** is the point where a finished chip design is sent off to be manufactured.
**GDSII** is the file format that describes the final layout sent to the fab.

## Analog and mixed-signal flow

```text
Idea → XSchem (schematic) → ngspice (simulate)
         ↓
      Magic / KLayout (layout) → DRC
         ↓
      Netgen (LVS) → PEX → iterate
         ↓
      GDSII for tapeout
```

| Tool | Stage |
|------|-------|
| XSchem | Draw and edit schematics |
| ngspice | Simulate circuits from those schematics |
| Magic / KLayout | Full-custom layout; DRC |
| Netgen | Layout vs schematic (LVS) |

## Digital flow (open-source ASIC)

```text
SystemVerilog RTL → Yosys (synthesis)
         ↓
   LibreLane / OpenROAD-style flow (P&R, signoff)
         ↓
      GDSII for tapeout
```

| Tool | Stage |
|------|-------|
| Yosys | RTL → gate-level netlist |
| Verilator / cocotb | Pre-silicon verification (later courses) |
| LibreLane | Automated RTL-to-GDSII (DD103 and later) |

Early digital courses also use FPGAs, as a path alongside the open ASIC flow. DD102 puts a design
onto a real board with the open FPGA toolchain (Yosys, nextpnr, IceStorm). That toolchain is
already in this image, so there's no vendor software to install.

## Shared infrastructure

| Piece | Role |
|-------|------|
| Docker + IIC-OSIC-TOOLS | One environment with all the tools above |
| SKY130 PDK | Process design kit for the open SKY130 process |
| noVNC | Browser access to the desktop |
| `workspace` `modules/` | Per-course files, mounted into the container |

## Pick a track

You've finished IC101. Both tracks start here and both assume the workbench you just built. You
can take them in either order, or both.

| Track | Start with | What you do first |
|---|---|---|
| Analog | [AD101: Signals](https://uoftasic.com/ad101/) | Waveforms, spectra and Bode plots, before any circuit |
| Digital | [DD101: Intro to Digital Logic](https://uoftasic.com/dd101/) | Logic from first principles, down to gates |

Each track then runs in order, AD101 → AD102 → AD103 → AD104 and DD101 → DD102 → DD103 → DD104,
and every course links to the next one at the end. Courses that use the tools reuse this
workspace. Early courses that run in a web browser don't need Docker until their labs say so.

Keep these to hand:

- Re-run the smoke test ([Lab 03, Part 4](labs/lab-03-launch-the-workbench-overview.md#part-4-run-the-smoke-test))
  if you change the Docker tag or the PDK pin.
- When something breaks: [Troubleshooting](reference/troubleshooting.md).
- Every course, in one place: [edu.uoftasic.com](https://edu.uoftasic.com/).
