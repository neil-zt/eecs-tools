import math
from Util import detect_verbose, inv_sum_inv, complex_arithmetic, phasor_arithmetic, phasor_to_rectangular


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
    return 1 / R(v=v, i=i, p=p)
    

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
def C(v: float=None, q: float=None) -> float:
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
    l: float=None,
    ) -> float:
    """
    Compute the energy, given the parameters 
    """
    if c is not None and v is not None: 
        return 0.5 * c * v ** 2
    if l is not None and i is not None: 
        return 0.5 * l * i ** 2
    if p is not None and t is not None: 
        return p * t
    if t is not None: 
        return t * P(r=r, v=v, i=i)
    return None


@detect_verbose
def parallel(
    rs: list[float]=None,
    cs: list[float]=None,
    ls: list[float]=None,
    ) -> float:
    """
    Compute the equivalent resistance, capacitance, or inductance in parallel
    """
    if rs is not None:
        return inv_sum_inv(rs)
    if ls is not None: 
        return sum(ls)
    if cs is not None:
        return inv_sum_inv(cs)
    return None


@detect_verbose
def series(
    rs: list[float]=None,
    cs: list[float]=None,
    ls: list[float]=None,
    ) -> float:
    """
    Compute the equivalent resistance, capacitance, or inductance in series 
    """
    if rs is not None:
        return sum(rs)
    if ls is not None:
        return inv_sum_inv(ls)
    if cs is not None: 
        return sum(cs)
    return None


@detect_verbose
def cseries(zs: list[tuple[float]]=None) -> tuple[float]:
    """
    Compute the equivalent impedance in complex regtangular form of many impedances in series
    """
    if zs is None or not len(zs):
        return (0, 0)
    z_sum: tuple[float] = zs[0]
    for z in zs[1:]:
        z_sum = complex_arithmetic(z_sum, "+", z)
    return z_sum


@detect_verbose
def pseries(ps: list[tuple[float]]=None) -> tuple[float]:
    """
    Compute the equivalent impedance in phasor form of many impedances in series 
    """
    if ps is None or not len(ps):
        return (0, 0)
    p_sum: tuple[float] = ps[0]
    for p in ps[1:]:
        p_sum = phasor_arithmetic(p_sum, "+", p)
    return p_sum


@detect_verbose
def cparallel(zs: list[tuple[float]]=None) -> tuple[float]:
    """
    Compute the equivalent impedance in complex rectangular form of many impedances in parallel 
    """
    if zs is None or not len(zs):
        return (0, 0)
    inv_sum: tuple[float] = complex_arithmetic((1, 0), "/", zs[0])
    for z in zs[1:]:
        inv_curr = complex_arithmetic((1, 0), "/", z)
        inv_sum = complex_arithmetic(inv_sum, "+", inv_curr)
    return complex_arithmetic((1, 0), "/", inv_sum)


@detect_verbose
def pparallel(ps: list[tuple[float]]=None) -> tuple[float]:
    """
    Compute the equivalent impedance in phasor form of many impedances in parallel
    """
    if ps is None or not len(ps):
        return (0, 0)
    zs = list(map(phasor_to_rectangular, ps))
    return cparallel(zs)


@detect_verbose
def Z(r: float=None, l: float=None, c: float=None, w: float=None) -> tuple[float]:
    """
    Compute the impedance of a resistor, an inductor, or a capacitor in an AC circuit
    """
    if r is not None:
        return (r, 0)
    if l is not None and w is not None:
        return (0, l * w)
    if c is not None and w is not None:
        return (0, - 1 / (c * w))
    return None


