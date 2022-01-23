import numpy as np

from ..local_interpolation import FourthOrderPolynomialInterpolation
from .base import AbstractStratonovichSolver
from .runge_kutta import AbstractERK, ButcherTableau


_midpoint_tableau = ButcherTableau(
    a_lower=(np.array([0.5]),),
    b_sol=np.array([0.0, 1.0]),
    b_error=np.array([1.0, -1.0]),
    c=np.array([0.5]),
)


class _MidpointInterpolation(FourthOrderPolynomialInterpolation):
    # I don't think this is well-chosen -- I think this is just a simple choice to get
    # an approximation for y at the middle of each step, and that better choices are
    # probably available.
    c_mid = np.array([0, 0.5])


class Midpoint(AbstractERK, AbstractStratonovichSolver):
    """Midpoint method.

    2nd order explicit Runge--Kutta method. Has an embedded Euler method for adaptive
    step sizing.

    Also sometimes known as the "modified Euler method".

    When used to solve SDEs, converges to the Stratonovich solution.
    """

    tableau = _midpoint_tableau
    interpolation_cls = _MidpointInterpolation
    order = 2
    strong_order = 0.5
