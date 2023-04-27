from __config__ import VERBOSE_DEFAULT

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