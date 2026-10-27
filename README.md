# Bracket Stress Analysis

> **Status: work in progress.** The problem definition and hand calculation are done. The Python calculator, parametric sweep, and validation are still to come.

> **Note:** This is a personal learning project, not a professional or certified engineering tool. It uses simplified assumptions (see below) and should not be used for real structural design or safety decisions.

A Python tool to estimate bending stress, tip deflection, and factor of safety (FOS) for a cantilever bracket, and to study how geometry and loading affect performance.

## Problem setup

A rectangular bar is fixed at one end with a point load at the free end.

| Input | Value |
|---|---|
| Length, L | 0.300 m |
| Width, b | 0.025 m |
| Thickness, h | 0.010 m |
| Load, P | 200 N |
| Material | Aluminum 6061-T6 |
| Young's modulus, E | 68.9 GPa |
| Yield strength | 276 MPa |

Material values are commonly published figures for 6061-T6. Source: 

## Equations

- Moment of inertia: I = b·h³ / 12
- Maximum bending moment (at the fixed end): M = P·L
- Maximum bending stress: σ = M·c / I, where c = h/2
- Tip deflection: δ = P·L³ / (3·E·I)
- Factor of safety: FOS = yield strength / σ

## Hand calculation (baseline case)

| Quantity | Result |
|---|---|
| Moment of inertia, I | 2.083 × 10⁻⁹ m⁴ |
| Maximum moment, M | 60 N·m |
| Maximum bending stress, σ | 144 MPa |
| Factor of safety | 1.92 |
| Tip deflection, δ | 12.5 mm |

The Python calculator will be checked against these values.

## Assumptions and limitations

- Linear elastic material; stresses stay below yield
- Small deflection (Euler-Bernoulli beam theory)
- Point load at the free end
- Perfectly rigid fixed end
- Constant rectangular cross-section, no holes or fillets
- Stress concentrations at the fixed end are ignored
- Baseline case is static; dynamic loading will be modeled with a simple load factor
