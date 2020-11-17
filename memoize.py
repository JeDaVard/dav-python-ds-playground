def fib(n):
    if n < 2:
        return n

    return fib(n-2) + fib(n-1)


if __name__ == '__main__':
    import timeit

    print('not memoized', timeit.timeit('fib(32)', globals=globals(), number=1))


def memoize(fn):
    cache = {}

    def execute(*args):
        if args in cache:
            return cache[args]
        else:
            result = fn(*args)
            cache[args] = result
            return result

    return execute


fib = memoize(fib)


if __name__ == '__main__':
    import timeit

    print('memoized', timeit.timeit('fib(32)', globals=globals(), number=1))
