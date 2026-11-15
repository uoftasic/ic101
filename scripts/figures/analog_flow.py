"""The analog and mixed-signal flow, from an idea to the GDSII file sent for tapeout.

The rows and the down arrows sit where the text sketch on tapeout-flow.md had them:
each down arrow leaves the box above it (XSchem, then Magic / KLayout, then Netgen).
"""
import schemdraw.elements as elm
import schemdraw.flow as flow

from circuit_style import drawing, save

H = 1.1      # box height
GAP = 0.9    # arrow between two boxes in a row
DROP = 0.8   # arrow from one row down to the next

d = drawing()
d.config(margin=0.3)     # a little white around the edge, so no text touches it


def box(x, y, w, text, anchor="W"):
    return d.add(flow.Box(w=w, h=H).anchor(anchor).at((x, y)).label(text))


def right_of(prev, w, text):
    """An arrow out of prev's right side, then a box of width w at its tip."""
    d.add(elm.Arrow().at(prev.E).right(GAP))
    return box(prev.E[0] + GAP, prev.E[1], w, text)


def below(prev, w, text):
    """An arrow down out of prev, then a box of width w centred under it."""
    d.add(elm.Arrow().at(prev.S).down(DROP))
    return box(prev.S[0], prev.S[1] - DROP, w, text, anchor="N")


idea = box(0, 0, 1.4, "Idea")
xschem = right_of(idea, 2.5, "XSchem\n(schematic)")
right_of(xschem, 2.5, "ngspice\n(simulate)")

layout = below(xschem, 3.3, "Magic / KLayout\n(layout)")
right_of(layout, 1.4, "DRC")

netgen = below(layout, 2.1, "Netgen\n(LVS)")
pex = right_of(netgen, 1.4, "PEX")
right_of(pex, 1.8, "iterate")

below(netgen, 3.8, "GDSII for tapeout")

print(save(d, "ic101-analog-flow"))
