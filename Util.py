from __config__ import VERBOSE_DEFAULT

def detect_verbose(function):
    def wrapper(*args, verbose=VERBOSE_DEFAULT, **kwargs):
        output = function(*args, **kwargs)
        if verbose:
            print(output)
        return output
    return wrapper