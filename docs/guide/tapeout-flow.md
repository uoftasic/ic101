# Where each tool sits in the tapeout flow

A mental map of the tools you just verified — not a full design course. **Tapeout** is the point where a finished chip design is sent off to be manufactured; **GDSII** is the file format that describes the final layout sent to the fab.

## Analog / mixed-signal path

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
|------|--------|
| **XSchem** | Draw and edit schematics |
| **ngspice** | Simulate circuits from those schematics |
| **Magic** / **KLayout** | Full-custom layout; DRC |
| **Netgen** | Layout vs schematic (LVS) |

## Digital path (open-source ASIC)

```text
SystemVerilog RTL → Yosys (synthesis)
         ↓
   LibreLane / OpenROAD-style flow (P&R, signoff)
         ↓
      GDSII for tapeout
```

| Tool | Stage |
|------|--------|
| **Yosys** | RTL → gate-level netlist |
| **Verilator** / **cocotb** | Pre-silicon verification (later courses) |
| **LibreLane** | Automated RTL-to-GDSII (DD103 and friends) |

FPGAs appear in early digital courses as a parallel path before the open ASIC flow — DD102 puts a
design onto a real board with the open toolchain (Yosys, nextpnr, IceStorm) that is already in this
image, so there is no vendor install to do.

## Shared infrastructure

| Piece | Role |
|-------|------|
| **Docker + IIC-OSIC-TOOLS** | One environment with the tools above |
| **SKY130 PDK** | Process design kit for open sky130 |
| **noVNC** | Browser access to the desktop |
| **workspace `modules/`** | Per-course files mounted into the container |

## What to do next

**Pick a track.** Both start here, both assume the workbench you just built, and you can do
them in either order — or both.

| Track | Start with | What you do first |
|---|---|---|
| **Analog** | [**AD101** — Signals & Systems](https://uoftasic.com/ad101/) | Waveforms, spectra and Bode plots, before any circuit |
| **Digital** | [**DD101** — Intro to Digital Logic](https://uoftasic.com/dd101/) | Logic from first principles, down to gates |

Each track then runs on in order — AD101 → AD102 → AD103 → AD104, and DD101 → DD102 → DD103 →
DD104 — and every course links to the next one at the end.

Also worth keeping to hand:

- Re-run the [smoke test](guide/smoke-test.md) if you update Docker tags or the PDK pin
- When stuck: [Troubleshooting](reference/troubleshooting.md)
- Every course, in one place: [edu.uoftasic.com](https://edu.uoftasic.com/)
