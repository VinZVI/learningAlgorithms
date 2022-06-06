import time


def iterative_merge_sort(a):
    q = []
    for count in a:
        q.append([count])
    # if len(q)%2 == 1:
    #     q.append([0])
    print(q)
    s = []
    while len(q) > 1:
        s.append(merg(q.pop(0), q.pop(0)))
        if len(q) == 1:
            s.append(q.pop())
            q.extend(s)
            s.clear()
        elif len(q) < 1:
            q.extend(s)
            s.clear()
        print(s, q)


c = 0


def merg(list_i, list_j):
    res = []
    global c
    if list_i[0] > list_j[0]:


def merg(list_i, list_j):
    global c
    for i in list_i:
        for j in list_j:
            if i > j:
                c += 1

    return list_i + list_j


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
