def maxsum(n, A):
    capacity = [0] * (n + 1)
    capacity[1] = A[0]
    for i in range(2, n + 1):
        capacity[i] = max([capacity[i - 2] + A[i - 1], capacity[i - 1] + A[i - 1]])
        print(capacity)
    return capacity[n]


def input_data():
    n = map(int, input())
    A = [int(i) for i in input().split(' ')]
    return n, A


def input_file():
    with open("exmpl.txt", 'r') as file:
        # print(file.read())
        n = int(file.readline().strip())
        A = [int(i) for i in file.readline().split(' ')]
    print(n, A)
    return n, A


def main():
    n, A = input_file()
    print(maxsum(n, A))


if __name__ == "__main__":
    main()
