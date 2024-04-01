# noinspection PyShadowingBuiltins,PyUnusedLocal
def compute(x, y):
    if not (0 <= x <= 100) or not (0 <= y <= 100):
        raise ValueError('x and y must be between 0 and 100')

    result = x + y
    return result


