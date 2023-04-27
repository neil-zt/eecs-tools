import math
from Util import detect_verbose

class DC_Cheat:

    @staticmethod
    @detect_verbose
    def basic():
        return """
V = IR
P = IV = (I^2)R = (V^2) / R
        """


@detect_verbose
def R(v: float=None, i: float=None, p: float=None) -> float:
    """
    Compute the resistance, given any two of voltage, current, and power
    """
    if v is not None and i is not None:
        return v / i
    if v is not None and p is not None: 
        return v ** 2 / p
    if i is not None and p is not None: 
        return p / (i ** 2)
    return None


@detect_verbose
def G(v: float=None, i:float=None, p:float=None) -> float:
    """
    Compute the conductance, given any two of voltage, current, and power
    """
    return 1 / r(v=v, i=i, p=p)
    

@detect_verbose
def V(
        r: float=None, 
        i: float=None, 
        p: float=None, 
        c: float=None, 
        q: float=None, 
        l: float=None, 
        di: float=None
    ) -> float:
    """
    Compute the voltage, given the parameters
    """
    if r is not None and i is not None: 
        return r * i
    if r is not None and p is not None: 
        return math.sqrt(r * p)
    if i is not None and p is not None: 
        return p / (i ** 2)
    if c is not None and q is not None: 
        return q / c
    if l is not None and di is not None: 
        return l * di
    return None


@detect_verbose
def I(r: float=None, v: float=None, p: float=None) -> float:
    """
    Compute the current, given any two of resistance, voltage, and power
    """
    if r is not None and v is not None:
        return v / r
    if v is not None and p is not None:
        return p / v
    if r is not None and p is not None:
        return math.sqrt(p / r)
    return None


@detect_verbose
def P(r: float=None, v: float=None, i: float=None) -> float:
    """
    Compute the power, given any two of resistance, voltage, and current
    """
    if r is not None and v is not None:
        return v ** 2 / r
    if v is not None and i is not None:
        return i * v
    if r is not None and i is not None:
        return i ** 2 * r
    return None


@detect_verbose
def C(v: float=None, q: float=None):
    """
    Compute the capacitance of a linear capacitor, given the voltage and charge
    """
    if v is not None and q is not None:
        return q / v
    return None


@detect_verbose
def Q(v: float=None, c: float=None) -> float:
    """
    Compute the charge stored on a linear capacitor, given the voltage and capacitance
    """
    if v is not None and c is not None:
        return c * v
    return None


@detect_verbose
def E(
    c: float=None, 
    v: float=None, 
    i: float=None,
    p: float=None,
    r: float=None, 
    t: float=None, 
    ) -> float:
    """
    Compute the energy, given the parameters 
    """
    if c is not None and v is not None: 
        return 0.5 * c * v ** 2
    if p is not None and t is not None: 
        return p * t
    if t is not None: 
        return t * p
    return None


@detect_verbose
def parallel(resistances: list[float]) -> float:
    """
    Compute the equivalence resistance of a parallel circuit, given the resistance values
    """
    inv_sum: float = 0
    for resistance in resistances:
        inv_sum += 1 / resistance
    return 1 / inv_sum


@detect_verbose
def series(resistances: list[float]) -> float:
    """
    Compute the equivalence resistance of a series circuit, given the resistance values
    """
    return sum(resistances)

