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


def analyze(P, L, b, h, E, yield_strength):
    """Run the full calculation and return the results in a dictionary."""
    stress = bending_stress(P, L, b, h)
    return {
        "I": moment_of_inertia(b, h),
        "M": max_moment(P, L),
        "stress": stress,
        "deflection": tip_deflection(P, L, E, b, h),
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

    r = analyze(P, L, b, h, E, YIELD)

    print("Cantilever bracket, baseline case (Aluminum 6061-T6)")
    print(f"  Moment of inertia I : {r['I']:.4e} m^4")
    print(f"  Max moment M        : {r['M']:.1f} N*m")
    print(f"  Max bending stress  : {r['stress'] / 1e6:.1f} MPa")
    print(f"  Factor of safety    : {r['FOS']:.2f}")
    print(f"  Tip deflection      : {r['deflection'] * 1000:.1f} mm")
