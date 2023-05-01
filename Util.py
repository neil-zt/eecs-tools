from __config__ import VERBOSE_DEFAULT
import math

def detect_verbose(function):
    def wrapper(*args, verbose=VERBOSE_DEFAULT, **kwargs):
        output = function(*args, **kwargs)
        if verbose:
            print(output)
        return output
    return wrapper


def inv_sum_inv(values: list[float]=None) -> float:
    inv_sum: float = 0
    for value in values:
        inv_sum += 1 / value
    return 1 / inv_sum


def degree_to_radian(degree: float) -> float:
    return math.radians(degree)


def radian_to_degree(radian: float) -> float:
    return math.degrees(radian)


def phasor_to_rectangular(phasor: tuple[float]) -> tuple[float]:
    (magnitude, angle) = phasor
    real = magnitude * math.cos(angle)
    imag = magnitude * math.sin(angle)
    return (real, imag)


def rectangular_to_phasor(coord: tuple[float]) -> tuple[float]:
    (real, imag) = coord
    magnitude = math.sqrt(real**2 + imag**2)
    angle = math.atan2(imag, real)
    if angle < 0:
        angle += 2*math.pi
    return (magnitude, angle)


def complex_arithmetic(
        complex1: tuple[float], 
        operator: str, 
        complex2: tuple[float]
        ) -> tuple[float]:
    
    (real1, imag1) = complex1
    (real2, imag2) = complex2
    rect_sum = None
    if operator == "+":
        rect_sum = (real1 + real2, imag1 + imag2)
    elif operator == "-":
        rect_sum = (real1 - real2, imag1 - imag2)
    elif operator == "*":
        rect_sum = (real1 * real2 - imag1 * imag2, real1 * imag2 + real2 * imag1)
    elif operator == "/":
        denom = real2**2 + imag2**2
        rect_sum = ((real1 * real2 + imag1 * imag2) / denom, (imag1 * real2 - real1 * imag2) / denom)

    return rect_sum


def phasor_arithmetic(
        phasor1: tuple[float], 
        operator: str, 
        phasor2: tuple[float]
        ) -> tuple[float]:
    
    complex1: tuple[float] = phasor_to_rectangular(phasor1)
    complex2: tuple[float] = phasor_to_rectangular(phasor2)
    
    rect_result = complex_arithmetic(complex1, operator, complex2)
    if rect_result is None:
        return None
    
    return rectangular_to_phasor(rect_result)


