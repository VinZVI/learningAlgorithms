# for i in tqdm(range(200)):
# # Waiting for 0.01 sec before next execution
#    sleep(.01)
# from functools import lru_cache
from timing import compare


def memo(f):
    cache = {}

    def inner(n):
        if n not in cache:
            cache[n] = f(n)
        return cache[n]

    return inner


# @memo # ИЛИ также можно заменить эту строчку на @lru_cache(maxsize=None)
def fib1(n):
    assert n >= 0
    return n if n <= 1 else fib1(n - 1) + fib1(n - 2)


# tqdm(fib1(80))
# print(fib1(499))


def fib3(n):
    assert n >= 0
    f0, f1 = 0, 1
    for i in range(n - 1):
        f0, f1 = f1, f0 + f1
    return f1


# print(fib3(80000))

# def timed(f, *args, n_iter=100):
#     acc = float("inf")
#     for i in range(n_iter):
#         t0 = time.perf_counter()
#         f(*args)
#         t1 = time.perf_counter()
#         acc = min(acc, t1 - t0)
#     return acc

# def compare(fs, args):
#     for f in fs:
#         plt.plot(args, [timed(f, arg) for arg in args], label = f.__name__)
#         plt.legend()
#         plt.grid(True)

compare([fib1, fib3], list(range(20)))
