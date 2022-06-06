import math
import time

tree = []


def insert(count):
    global tree
    tree.insert(0, count)
    n = len(tree)
    if n == 2 and count <= tree[1]:
        tree.pop(0)
        tree.append(count)
        return
    if len(tree) > 2:
        # count = tree.pop()
        n = 0

        while n * 2 + 2 < len(tree):
            if tree[n * 2 + 1] > tree[n * 2 + 2]:
                if count < tree[n * 2 + 1]:
                    tree.pop(n)
                    n = n * 2 + 1
                    tree.insert(n, count)
                else:
                    break
            else:
                if count < tree[n * 2 + 2]:
                    tree.pop(n)
                    sec_el = tree.pop(n * 2 + 1)
                    tree.insert(n, sec_el)
                    n = n * 2 + 2
                    tree.insert(n, count)
                else:
                    break
    # print(tree)


def extract_max():
    global tree
    if len(tree) == 0:
        print(None)
    max = tree.pop(0)

    if len(tree) > 2:
        count = tree.pop()
        n = 0
        tree.insert(0, count)
        while n * 2 + 2 < len(tree):
            if tree[n * 2 + 1] > tree[n * 2 + 2]:
                if count < tree[n * 2 + 1]:
                    tree.pop(n)
                    sec_el = tree.pop(n * 2)
                    tree.insert(n, sec_el)
                    n = n * 2 + 1
                    tree.insert(n, count)
                else:
                    break
            else:
                if count < tree[n * 2 + 2]:
                    tree.pop(n)
                    sec_el = tree.pop(n * 2 + 1)
                    tree.insert(n, sec_el)
                    n = n * 2 + 2
                    tree.insert(n, count)
                else:
                    break
        # tree.insert(n, count)

    elif len(tree) == 2 and tree[1] > tree[0]:
        count = tree.pop(0)
        tree.append(count)

    print(max)
    print(tree)


def input_data():
    for _ in range(int(input())):
        comand = input()
        if comand == 'ExtractMax':
            print('extract_max()')
        else:
            count = comand.split()[1]
            print(f'insert({int(count)})')


def print_tree(tree):
    deep_heap = math.ceil(math.log2(len(tree)))
    print(deep_heap)
    count = deep_heap
    s = 1
    indent = int((deep_heap * deep_heap) / 2)
    while count:
        if s == 1:
            print(' ' * indent, end='')
            print(tree[0])
            s *= 2
            count -= 1
            continue
        print(' ' * int(indent / s), end='')
        for x in range(s - 1, s * 2 - 1):
            print(tree[x], end=' ')
        print()
        s *= 2
        count -= 1


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
        # print(file.read())
        for line in file:
            print(line.strip())
            # comand = line
            # print(comand)
            if line.strip() == 'ExtractMax':
                extract_max()
            else:
                count = line.split()[1]
                insert(int(count))


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
