import random
import time


def nod_div(a, b):
    if a == b:
        return a
    if a == 0:
        return b
    if b == 0:
        return a
    if a > b:
        return nod_div(a % b, b)
    if b > a:
        return nod_div(a, b % a)


def nod_sab(a, b):
    if a == b:
        return a
    if a == 0:
        return b
    if b == 0:
        return a
    if a > b:
        return nod_sab(a - b, b)
    if b > a:
        return nod_sab(a, b - a)

def test(gcd, n_iter=100):
    for i in range(n_iter):
        c = random.randint(0, 1024)
        a = random.randint(0, 120)
        b = random.randint(0, 120)
        assert gcd(a, a) == gcd(a, 0) == a
        assert gcd(b, b) == gcd(b, 0) == b
        assert gcd(a, 1) == gcd(b, 1) == 1
        d = gcd(a, b)
        assert a % d == b % d == 0


def main(a,b):
    test(nod_sab)
    test(nod_div)
    start_time = time.time()
    print(nod_div(a, b))
    print(time.time() - start_time)
    start_time = time.time()
    print(nod_sab(a, b))
    print(time.time() - start_time)


if __name__ == '__main__':
    # start_time = time.time()
    main(1415957200, 6396707200)
    # print(time.time() - start_time)
