import cProfile
import sys


def lis_funtion(n, array_numbers):
    d, prev = [1 for _ in range(n)], [-1 for _ in range(n)]
    for i in range(0, n):
        for j in range(0, i):
            if array_numbers[j] >= array_numbers[i] and d[j] + 1 > d[i]:
                d[i] = d[j] + 1
                prev[i] = j
    ans = 0
    for i in range(0, n):
        ans = max(ans, d[i])
    l = restor_result(ans, d, prev)
    return ans, l


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
    lines = [line for line in sys.stdin.read().split('\n') if line != '']
    n = int(lines[0])
    print(lines[1])
    array_numbers = [int(x) for x in lines[1].split(' ')]
    # n = next(reader)
    # array_numbers = next(reader)
    # n = int(sys.stdin.readline().strip())
    # print(sys.stdin.readline().split(' '))
    # array_numbers = map(int, sys.stdin.readline().split(' '))
    # array_numbers.append(int(x.strip()))
    return n, array_numbers


def main():
    n, array_numbers = input_file()
    # print(input_data())
    ans, x = lis_funtion(n, array_numbers)
    print(ans)
    print(*x, sep=' ')


if __name__ == "__main__":
    # start_time = time.time()
    cProfile.run("main()")
    # print(time.time() - start_time)
