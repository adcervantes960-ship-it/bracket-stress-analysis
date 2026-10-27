"""Cantilever bracket calculator: bending stress, tip deflection, factor of safety.

All units are SI: meters, newtons, pascals.
Assumptions: linear elastic, small deflection (Euler-Bernoulli), point load at the
free end, rigid fixed end, constant rectangular cross-section, no stress concentrations.
"""

def moment_of_inertia(b, h):
    """Second moment of area of a rectangle about its neutral axis (m^4)."""
    return b * h ** 3 / 12.0


def max_moment(P, L):
    """Maximum bending moment at the fixed end of a tip-loaded cantilever (N*m)."""
    return P * L


def bending_stress(P, L, b, h):
    """Maximum bending stress at the fixed end, on the outer surface (Pa)."""
    M = max_moment(P, L)
    c = h / 2.0
    I = moment_of_inertia(b, h)
    return M * c / I


def tip_deflection(P, L, E, b, h):
    """Deflection of the free end (m)."""
    I = moment_of_inertia(b, h)
    return P * L ** 3 / (3.0 * E * I)


def factor_of_safety(yield_strength, stress):
    """Yield strength divided by the maximum stress. Below 1 means yielding."""
    return yield_strength / stress


def analyze(P, L, b, h, E, yield_strength, dynamic_factor=1.0):
    """Run the full calculation with an optional dynamic load factor and return results."""
    effective_P = P * dynamic_factor
    stress = bending_stress(effective_P, L, b, h)
    return {
        "P_applied": P,
        "dynamic_factor": dynamic_factor,
        "effective_P": effective_P,
        "I": moment_of_inertia(b, h),
        "M": max_moment(effective_P, L),
        "stress": stress,
        "deflection": tip_deflection(effective_P, L, E, b, h),
        "FOS": factor_of_safety(yield_strength, stress),
    }


if __name__ == "__main__":
    # Baseline case: Aluminum 6061-T6
    L = 0.300             # length, m
    b = 0.025             # width, m
    h = 0.010             # thickness, m
    P = 200.0             # tip load, N
    E = 68.9e9            # Young's modulus, Pa
    YIELD = 276e6         # yield strength, Pa

    # Run static baseline
    r_static = analyze(P, L, b, h, E, YIELD, dynamic_factor=1.0)
    print("=== Cantilever bracket: Static Baseline ===")
    print(f"  Max bending stress  : {r_static['stress'] / 1e6:.1f} MPa")
    print(f"  Factor of safety    : {r_static['FOS']:.2f}")

    # Run dynamic loading case (DLF = 1.5)
    r_dynamic = analyze(P, L, b, h, E, YIELD, dynamic_factor=1.5)
    print("\n=== Cantilever bracket: Dynamic Loading (DLF = 1.5) ===")
    print(f"  Effective Load      : {r_dynamic['effective_P']:.1f} N")
    print(f"  Max bending stress  : {r_dynamic['stress'] / 1e6:.1f} MPa")
    print(f"  Factor of safety    : {r_dynamic['FOS']:.2f}")
