def knapsack(W, n, weigth):
    d = [0] * (n + 1)
    for i in range(n + 1):
        d[i] = [0] * (W + 1)

    for i in range(1, n + 1):
        for w in range(1, W + 1):
            d[i][w] = d[i - 1][w]

            if weigth[i - 1] <= w:
                d[i][w] = max([d[i - 1][w], d[i - 1][w - weigth[i - 1]] + weigth[i - 1]])

    return d[n][W]


def input_data():
    W, n = map(int, input().split(' '))
    w = [int(i) for i in input().split(' ')]
    return W, n, w


def input_file():
    with open("exmpl.txt", 'r') as file:
        # print(file.read())
        W, n = map(int, file.readline().split(' '))
        w = [int(i) for i in file.readline().split(' ')]
    return W, n, w


def main():
    W, n, w = input_file()
    print(knapsack(W, n, w))


if __name__ == "__main__":
    main()
