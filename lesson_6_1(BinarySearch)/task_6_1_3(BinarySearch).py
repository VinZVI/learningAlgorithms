import time


def binary_search(a, k):
    a.sort()
    l, r = 1, len(a) - 1
    while l <= r:
        m = l + (r - l) // 2
        # print(f'm = {m}')
        if a[m] == k:
            return m, a.index(k)
        elif a[m] > k:
            r = m - 1
        else:
            l = m + 1
    return -1


def dict_serch(a, k):
    j = a.get(k)
    if j == None:
        return -1
    else:
        return j


def test(n_iter=1):
    import random
    for i in range(n_iter):
        length = random.randint(1, 10)
        # print(length)
        a = [random.randint(1, 10) for _ in range(20)]
        b = [random.randint(1, 10) for _ in range(20)]
        print(a, b)
        a.sort()
        for k in b:
            v = binary_search(a, k)
            n = a.index(k)
            print(v, n)
            assert v == n
            # assert binary_search(a, k) == a.index(k)


def input_file():
    with open("exmpl.txt", 'r') as file:
        # print(file.read())
        a, b = file.read().split('\n')
        a = list(map(int, a[1::].split()))
        print(a)
        b = list(map(int, b[1::].split()))
        print(b)
        dict_a = {}
        for i, val in enumerate(a, start=1):
            dict_a.update({val: i})
        print(dict_a)
        a.insert(0, -1)
    for k in b:
        print(f'{binary_search(a, k)}={dict_serch(dict_a, k)}', end=' ')


def main():
    # a = list(map(int, input()[1:].split()))
    # print(a)
    # b = list(map(int, input()[1:].split()))
    # print(b)
    # a.insert(0, -1)
    # for k in b:
    #     print(binary_search(a, k))
    # test()
    input_file()


if __name__ == "__main__":
    start_time = time.time()
    main()
    print(time.time() - start_time)
