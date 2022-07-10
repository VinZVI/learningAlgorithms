def calc(n):
    D = [[0] * 2] * (n + 1)
    D[0] = [100000, 0]
    for i in range(2, n + 1):
        x3 = i / 3 if (i / 3) == int(i / 3) else 0
        x2 = i / 2 if (i / 2) == int(i / 2) else 0
        x1 = i - 1
        D[i] = min([[D[int(x3)][0] + 1, x3], [D[int(x2)][0] + 1, x2], [D[int(x1)][0] + 1, x1]], key=lambda x: x[0])
    # print(D)
    print(D[n][0])
    l = []
    while n >= 1:
        l.append(n)
        n = int(D[n][1])
    l.reverse()
    print(*l, sep=' ')


def main():
    n = int(input())
    calc(n)


if __name__ == "__main__":
    main()
