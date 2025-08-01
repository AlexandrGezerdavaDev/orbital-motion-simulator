import numpy as np
from scipy.integrate import odeint

def orbital_dynamics(state, t, mu):
    """Compute derivatives for orbital motion."""
    r = state[:3]
    v = state[3:]
    r_norm = np.linalg.norm(r)
    a = -mu * r / r_norm**3
    return np.concatenate([v, a])

def simulate_orbit(r0, v0, t_span, mu):
    """Simulate orbit given initial conditions."""
    state0 = np.concatenate([r0, v0])
    states = odeint(orbital_dynamics, state0, t_span, args=(mu,))
    return states