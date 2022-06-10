import time


def serch_point_naive(list_segments, point):
    less = [segment for segment in list_segments if segment[1] >= point >= segment[0]]
    return len(less)


def quicksort(list_segments, i):
    if len(list_segments) < 2:
        return list_segments
    else:
        pivot = list_segments[0]
        less = [segment for segment in list_segments[1:] if segment[i] <= pivot[i]]
        greater = [segment for segment in list_segments[1:] if segment[i] > pivot[i]]
        # print(less)
        return quicksort(less, i) + [pivot] + quicksort(greater, i)


def search_point(list_segments, list_points):
    global _array

    for point in list_points:
        array_segments = list_segments.copy()
        binary_search(array_segments, point, i=0)
        array_segments = quicksort(array_segments, i=1)
        print(array_segments)
        binary_search(array_segments, point, i=1)
        print(len(_array), sep=' ')
        _array.clear()


_array = []


def binary_search(list_segments, point, i):
    global _array
    l, r = 1, len(list_segments)
    while l <= r:
        m = (r + l) // 2
        # print(f'm = {m}')
        if list_segments[m - 1][1] >= point >= list_segments[m - 1][0]:
            _array.append(list_segments.pop(m - 1))
            return binary_search(list_segments, point, i)
        elif list_segments[m - 1][i] > point:
            r = m - 1
        else:
            l = m + 1
    return


def input_file():
    list_segments, list_points = [], []
    with open("exmpl.txt", 'r') as file:
        # print(file.read())
        n, m = map(int, file.readline().split(' '))
        for _ in range(n):
            list_segments.append(list(map(int, file.readline().split())))
        print(list_segments)
        list_points = list(map(int, file.readline().split()))
        print(list_points)
    return list_segments, list_points


def input_data():
    list_segments, list_points = [], []
    n, m = map(int, input().split(' '))
    for _ in range(n):
        list_segments.append(list(map(int, input().split())))
    list_points = list(map(int, input().split()))
    return list_segments, list_points


def main():
    res = []
    list_segments, list_points = input_file()
    list_segments = quicksort(list_segments, i=0)
    print(list_segments)
    search_point(list_segments, list_points)
    # for point in list_points:
    #     res.append(quicksort(list_segments, point))
    # print(res)
    # print(*res, sep=' ')


if __name__ == "__main__":
    start_time = time.time()
    main()
    print(time.time() - start_time)
