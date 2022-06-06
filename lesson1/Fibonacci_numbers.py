from tqdm import tqdm


def recurs_function(n, m):
    fib0 = 0
    fib1 = 1
    fib2 = 1
    if n == 1:
        print(fib1)
        return
    if n >= 2:
        # percent = (100//(n - 1))/100
        # print(percent)
        # with alive_bar(total=n, bar='blocks', ctrl_c=True) as bar:

        for i in tqdm(range(2, n + 1)):
            fib2 = (int(str(fib1)[-1]) + int(str(fib0)[-1])) % 10
            # print(i, fib2)
            fib0 = fib1
            fib1 = fib2
            # time.sleep(0.1)
            # bar()
    print(fib2)


def mod_func(n, m):
    fib0 = 0
    fib1 = 1
    fib2 = 1
    if n == 1:
        print(fib1)
        return
    if n >= 2:
        for i in tqdm(range(2, n + 1)):
            fib2 = fib1 + fib0
            fib0 = fib1
            fib1 = fib2

    print(f'F({n}) mod({m}) = {fib2 % m}')


def find_period(n, m):
    list_period = [0, 1]
    list_fib = [0, 1]
    fib0, fib1 = list_fib[0], list_fib[1]
    per0, per1 = list_period[0], list_period[1]
    period = 1

    # for i in tqdm(range(2, n + 1)):
    while n:
        fib0, fib1 = fib1, fib1 + fib0
        # list_fib.append(fib1)
        per0, per1 = per1, fib1 % m
        list_period.append(per1)
        period = len(list_period)
        # time.sleep(0.015)
        if per0 == 0 and per1 == 1:
            period = len(list_period) - 2
            break

    if n <= period:
        mod_m = list_period[n]
    else:
        mod_m = list_period[(n % period)]

    print(f'F({n}) mod({m}) = {mod_m}, P({m}) = {period}')


def find_period_mod(n, m):
    list_period = [0, 1]
    list_fib = [0, 1]
    fib0, fib1 = list_fib[0], list_fib[1]
    per0, per1 = list_period[0], list_period[1]
    period = 1

    # for i in tqdm(range(2, n + 1)):
    while n:
        # fib0, fib1 = fib1, fib1 + fib0
        # list_fib.append(fib1)
        per0, per1 = per1, (per1 + per0) % m
        list_period.append(per1)
        period = len(list_period)
        # time.sleep(0.015)
        if per0 == 0 and per1 == 1:
            period = len(list_period) - 2
            break

    if n <= period:
        mod_m = list_period[n]
    else:
        mod_m = list_period[(n % period)]
    print(f'F({n}) mod({m}) = {mod_m}, P({m}) = {period}')


# find_period_mod= viz(find_period_mod)
# @viz
# def fib1(n):
#     assert n >= 0
#     return n if n <= 1 else fib1(n - 1) + fib1(n - 2)


# fib1=viz(fib1)

cache = {}


def fib2(n):
    assert n >= 0
    if n not in cache:
        if n <= 1:
            cache[n] = n
        else:
            cache[n] = fib2(n - 1) + fib2(n - 2)
    return cache[n]


fib2(8)

fib2(80)

fib2(800)

# fib2 = viz(fib2)

fib2(5)


def main(n, m):
    pass
    # start_time = time.time()
    # find_period_mod(n, m)
    # print(time.time() - start_time)
    # start_time = time.time()
    # find_period(n, m)
    # print(time.time() - start_time)
    # fib1(3)
    # start_time = time.time()
    # mod_func(n, m)
    # print(time.time() - start_time)


if __name__ == '__main__':
    # start_time = time.time()
    # main(1000000000000000000, 100000)
    # print(time.time() - start_time)
    # fib1(3)
    fib2(5)
