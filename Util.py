def detect_verbose(function):
    def wrapper(verbose=True, *args, **kwargs):
        output = function(*args, **kwargs)
        if verbose:
            print(output)
        return output
    return wrapper