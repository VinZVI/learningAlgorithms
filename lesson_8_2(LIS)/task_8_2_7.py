import cProfile


def lis_funtion(n, array_numbers):
    d, prev = [], []
    for i in range(0, n):
        d.append(1)
        prev.append(-1)
        for j in range(0, i):
            if array_numbers[j] >= array_numbers[i] and d[j] + 1 > d[i]:
                d[i] = d[j] + 1
                prev[i] = j
    ans = 0
    for i in range(0, n):
        ans = max(ans, d[i])

    return f"{ans}\n{array_numbers}\n{d}\n{prev}\n{restor_result(ans, d, prev)}"


def restor_result(ans, d, prev):
    l = [1 for _ in range(ans)]
    k = 0
    for i in range(1, len(d)):
        if d[i] > d[k]:
            k = i
    j = ans - 1
    while k > 0:
        l[j] = k + 1
        j -= 1
        k = prev[k]
    return l


def input_file():
    # array_numbers = []
    with open("exmpl.txt", 'r') as file:
        n = int(file.readline().strip())
        # print(n)
        array_numbers = list(map(int, file.readline().split()))
    return n, array_numbers


def input_data():
    array_numbers = []
    n = map(int, input())
    array_numbers.append(list(map(int, input().split())))
    return n, array_numbers


def main():
    n, array_numbers = input_file()
    print(lis_funtion(n, array_numbers))


if __name__ == "__main__":
    # start_time = time.time()
    cProfile.run(main())
    # print(time.time() - start_time)
