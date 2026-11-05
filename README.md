# Cantilever Bracket Stress Analysis

## Goal
This is a personal project to learn Python and to understand how programming connects to engineering: turning a beam-theory hand calculation into code, then testing how the design responds to changes in its inputs.

## Description
The tool uses Euler-Bernoulli beam theory to analyze a rectangular Aluminum 6061-T6 cantilever bar (300 mm x 25 mm x 10 mm) fixed at one end with a point load at the tip. For a given load it calculates:

- Area moment of inertia: I = b·h³ / 12
- Maximum bending moment: M = P·L
- Maximum bending stress: σ = M·c / I, with c = h / 2
- Tip deflection: δ = P·L³ / (3·E·I)
- Factor of safety against yield: FOS = yield strength / σ

It also sweeps thickness, length, and load one at a time and saves a plot for each. Material values are E = 68.9 GPa and yield strength = 276 MPa ([add datasheet source, e.g. MatWeb or ASM]).

**How to run it:** Python 3.12, then `pip install numpy matplotlib`, then `python v3/bracket_calc.py`.

**Disclaimer:** This project is for education only. The results are simplified estimates and must not be used for any real engineering design, safety decision, or certification. The model assumes linear elastic behavior, small deflections, a point load at the tip, a perfectly rigid fixed end, and a constant rectangular cross-section. It ignores stress concentrations, and the load cases are static.

## Onshape model
![Onshape model](v3/onshape.png)

## Results
Python results were compared with an Onshape FEA simulation of the same bar at two loads: 200 N, and 300 N (200 N with a 1.5x dynamic load factor).

| Case | Quantity | Python | Onshape | Difference |
|---|---|---|---|---|
| 200 N | Max bending moment | 60 N·m | 60 N·m | 0% |
| 200 N | Max stress | 144.0 MPa | 135 MPa | -6.3% |
| 200 N | Tip deflection | 12.54 mm | 4.62 mm | -63.2% |
| 200 N | Factor of safety | 1.92 | 2.04 | +6.7% |
| 300 N | Max bending moment | 90 N·m | 90 N·m | 0% |
| 300 N | Max stress | 216.0 MPa | 202.5 MPa | -6.3% |
| 300 N | Tip deflection | 18.81 mm | 6.93 mm | -63.2% |
| 300 N | Factor of safety | 1.28 | 1.36 | +6.7% |

Onshape setup: [material, load direction, mesh settings, and that signed von Mises stress was read]

**Sweep plots**

![Thickness sweep](v3/sweep_thickness.png)
![Length sweep](v3/sweep_length.png)
![Load sweep](v3/sweep_load.png)

## Conclusion
The maximum stress from the Python tool agreed well with Onshape, within about 6% at both loads, and the factor of safety, which is calculated from stress, differs by the same amount. The tip deflection did not agree: Onshape gave about 63% less deflection than beam theory at both loads. Because the gap is the same at both loads, it looks like a systematic difference between the two setups rather than random error, and I did not find the cause. Mesh settings alone would not normally explain a gap this large, so the likely places to check are the material properties used in Onshape, how the load and fixed end were applied, and how the displacement was read. Until that is resolved, the stress results are the more trustworthy part of this tool, and the deflection results should be treated with caution.
