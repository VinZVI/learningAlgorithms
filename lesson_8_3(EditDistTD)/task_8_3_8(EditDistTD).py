def editDistTD(a, b):
    n, m = len(a), len(b)

    d = [0] * (n + 1)
    for i in range(n + 1):
        d[i] = [0] * (m + 1)

    for i in range(0, n + 1):
        d[i][0] = i

    for j in range(0, m + 1):
        d[0][j] = j

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            c = 0
            if a[i - 1] != b[j - 1]:
                c = 1
            d[i][j] = min([d[i - 1][j] + 1, d[i][j - 1] + 1, d[i - 1][j - 1] + c])

    return d[n][m]


def input_data():
    a = input()
    b = input()
    return a, b


def input_file():
    with open("exmpl.txt", 'r') as file:
        # print(file.read())
        a = file.readline().strip()
        b = file.readline().strip()
    # print(a, b)
    return a, b


def main():
    a, b = input_data()
    print(editDistTD(a, b))


if __name__ == "__main__":
    main()
