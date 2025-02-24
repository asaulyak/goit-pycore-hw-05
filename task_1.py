def caching_fibonacci():
    cache = {0: 0, 1: 1}

    def fibonacci(n: int) -> int:
        if not isinstance(n, int):
            raise ValueError("n must be an integer")

        p = 0 if n < 0 else n

        if p in cache:
            return cache[p]
        else:
            result = fibonacci(p - 1) + fibonacci(p - 2)
            cache[p] = result

            return result

    return fibonacci
