def detect_verbose(function):
    def wrapper(*args, verbose=True, **kwargs):
        output = function(*args, **kwargs)
        if verbose:
            print(output)
        return output
    return wrapper