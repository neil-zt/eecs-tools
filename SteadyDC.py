import math
from Util import detect_verbose

@detect_verbose
def R(V: float=None, I: float=None, P: float=None) -> float:
    if V is not None and I is not None:
        return V / I
    if V is not None and P is not None: 
        return V ** 2 / P
    if I is not None and P is not None: 
        return P / (I ** 2)
    return None
    
@detect_verbose
def V(R: float=None, I: float=None, P: float=None) -> float:
    if R is not None and I is not None: 
        return R * I
    if R is not None and P is not None: 
        return math.sqrt(R * P)
    if I is not None and P is not None: 
        return P / (I ** 2)
    return None