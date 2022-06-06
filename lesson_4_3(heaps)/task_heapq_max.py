import time
from heapq import heappush, heappop, heapify

tree = []


def input_data():
    for _ in range(int(input())):
        comand = input()
        if comand == 'ExtractMax':
            print(abs(heappop(tree)))
            heapify(tree)
        else:
            count = comand.split()[1]
            heappush(tree, (int(count)) * -1)


T = []


def t_insert(x):
    T.append(x)


def t_extract_max():
    m = 0
    for i in range(1, len(T)):
        if T[i] > T[m]:
            m = i
    result = T[m]
    del T[m]
    return result


def input_file():
    with open("exmpl.txt", 'r') as file:
        for line in file:
            print(line.strip())
            if line.strip() == 'ExtractMax':
                print(abs(heappop(tree)))
                heapify(tree)
            else:
                count = line.split()[1]
                heappush(tree, (int(count)) * -1)


def main():
    input_file()
    # # input_data()
    # all_segments = [2, 3, 18, 15, 18, 12, 12, 2]#[200, 10, 5, 500]#[10, 11, 12, 13, 14, 15, 1, 2, 4, 5, 6, 7, 8, 9]
    # for segments in all_segments:
    #     insert(segments)
    # global tree
    # print(tree)
    # print(extract_max())
    # print(extract_max())
    # print(extract_max())
    # print(extract_max())
    # # print(tree)
    # # print_tree(tree)
    # n = 11999
    # for i in range(10000, n):
    #     insert(i)
    #     t_insert(i)
    # for i in range(10000, n):
    #     a = extract_max()
    #     b = t_extract_max()
    #     if a == b:
    #         print(i, a)
    #     else:
    #         print(i, a, b, "ERROR")
    #         break


if __name__ == "__main__":
    start_time = time.time()
    main()
    print(time.time() - start_time)
