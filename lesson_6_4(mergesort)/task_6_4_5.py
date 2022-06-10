import time


def iterative_merge_sort(a):
    a.reverse()
    q, s = [], []
    for count in a:
        q.append([count])
    print(q)
    while len(q) > 1:
        s.append(merg(q.pop(), q.pop()))
        if len(q) == 1:
            s.append(q.pop())
            q.extend(s)
            q.reverse()
            s.clear()
        elif len(q) < 1:
            q.extend(s)
            q.reverse()
            s.clear()
        print(s, q)


c = 0


# def iterative_merge_sort(a):
#     q = []
#     for count in a:
#         q.append([count])
#     i = 0
#     n, m = len(q), len(q)
#     while n > 1:
#         q.append(merg(q[i], q[i + 1]))
#         i += 2
#         if m - i == 1:
#             q.append(q[i])
#             i += 1
#             n = n // 2 + 1
#             m += n
#         elif m - i == 0:
#             n //= 2
#             m += n


def merg(list_i, list_j):
    global c
    len_list_i, len_list_j = len(list_i), len(list_j)
    i, j = 0, 0
    res = []
    while len_list_j - j > 0:
        if list_i[i] > list_j[j]:
            c += len_list_i - i
            res.append(list_j[j])
            j += 1
            if len_list_j - j == 0:
                res += list_i[i:]
                break
        else:
            res.append(list_i[i])
            i += 1
            if len_list_i - i == 0:
                res += list_j[j:]
                break
    return res


# def merg(list_i, list_j):
#     global c
#     for i in list_i:
#         for j in list_j:
#             if i > j:
#                 c += 1
#     return list_i + list_j

def input_file():
    with open("exmpl.txt", 'r') as file:
        # print(file.read())
        n, a = file.read().split('\n', maxsplit=1)
        a = list(map(int, a.split()))
        print(a)
        iterative_merge_sort(a)


def main():
    input_file()
    print(c)


if __name__ == "__main__":
    start_time = time.time()
    main()
    print(time.time() - start_time)
