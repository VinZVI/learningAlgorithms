def lis_funtion(n, array_numbers):
    d = []
    for i in range(0, n):
        d.append(1)
        for j in range(0, i):
            if array_numbers[i] % array_numbers[j] == 0 and d[j] + 1 > d[i]:
                d[i] = d[j] + 1
    ans = 0
    for i in range(0, n):
        ans = max(ans, d[i])
    return ans


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
    main()
    # print(time.time() - start_time)
