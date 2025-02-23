cache = {0: 0, 1: 1}

def caching_fibonacci(n):
    if not isinstance(n, int):
        raise ValueError("n must be an integer")

    p = 0 if n < 0 else n

    if p in cache:
        return cache[p]
    else:
        result = caching_fibonacci(p - 1) + caching_fibonacci(p - 2)
        cache[p] = result

        return result
