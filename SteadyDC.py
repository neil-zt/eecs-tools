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
def R(V: float=None, I: float=None, P: float=None) -> float:
    """
    Compute the resistance, given any two of voltage, current, and power
    """
    if V is not None and I is not None:
        return V / I
    if V is not None and P is not None: 
        return V ** 2 / P
    if I is not None and P is not None: 
        return P / (I ** 2)
    return None
    
@detect_verbose
def V(R: float=None, I: float=None, P: float=None) -> float:
    """
    Compute the voltage, given any two of resistance, current, and power
    """
    if R is not None and I is not None: 
        return R * I
    if R is not None and P is not None: 
        return math.sqrt(R * P)
    if I is not None and P is not None: 
        return P / (I ** 2)
    return None

@detect_verbose
def I(R: float=None, V: float=None, P: float=None) -> float:
    """
    Compute the current, given any two of resistance, voltage, and power
    """
    if R is not None and V is not None:
        return V / R
    if V is not None and P is not None:
        return P / V
    if R is not None and P is not None:
        return math.sqrt(P / R)
    return None

@detect_verbose
def P(R: float=None, V: float=None, I: float=None) -> float:
    """
    Compute the power, given any two of resistance, voltage, and current
    """
    if R is not None and V is not None:
        return V ** 2 / R
    if V is not None and I is not None:
        return I * V
    if R is not None and I is not None:
        return I ** 2 * R
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