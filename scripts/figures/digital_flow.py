"""The digital (open-source ASIC) flow, from SystemVerilog RTL to the GDSII file sent for tapeout.

The rows and the down arrows sit where the text sketch on tapeout-flow.md had them:
the first down arrow leaves the SystemVerilog RTL box, the second the LibreLane box.
"""
import schemdraw.backends.svgtext as svgtext
import schemdraw.elements as elm
import schemdraw.flow as flow

from circuit_style import drawing, save

# schemdraw 0.23 sizes text by parsing it as XML, so a bare "&" (in "P&R") stops the
# script with a ParseError. Escape it for the size estimate only; the drawing itself
# still prints "&".
_text_size = svgtext.text_approx_size
svgtext.text_approx_size = lambda text, *a, **k: _text_size(text.replace("&", "&amp;"), *a, **k)

H = 1.1      # box height
GAP = 0.9    # arrow between two boxes in a row
DROP = 0.8   # arrow from one row down to the next

d = drawing()
d.config(margin=0.3)     # a little white around the edge, so no text touches it


def box(x, y, w, text, anchor="W"):
    return d.add(flow.Box(w=w, h=H).anchor(anchor).at((x, y)).label(text))


def below(prev, w, text):
    """An arrow down out of prev, then a box of width w centred under it."""
    d.add(elm.Arrow().at(prev.S).down(DROP))
    return box(prev.S[0], prev.S[1] - DROP, w, text, anchor="N")


rtl = box(0, 0, 4.0, "SystemVerilog RTL")
d.add(elm.Arrow().at(rtl.E).right(GAP))
box(rtl.E[0] + GAP, 0, 2.5, "Yosys\n(synthesis)")

pnr = below(rtl, 6.9, "LibreLane / OpenROAD-style flow\n(P&R, signoff)")
below(pnr, 3.8, "GDSII for tapeout")

print(save(d, "ic101-digital-flow"))
