import time


def left_bound(list_segments, point):
    left = -1
    rith = len(list_segments)
    while rith - left > 1:
        middle = (rith + left) // 2
        if list_segments[middle][1] < point:
            left = middle
        else:
            rith = middle
    # if left == -1:
    #     return 0
    return left


def rith_bound(list_segments, point):
    left = -1
    rith = len(list_segments)
    while rith - left > 1:
        middle = (rith + left) // 2
        if list_segments[middle][0] <= point:
            left = middle
        else:
            rith = middle
    return rith


def serch_bound(list_segments, array_segments, list_points):
    # print(array_segments)
    for point in list_points:
        left_index = rith_bound(list_segments, point)
        rith_index = left_bound(array_segments, point)
        if left_index == 0 and rith_index == -1:
            print(0, end=' ')
        else:
            len_left_index = len(list_segments[:left_index])
            len_rith_index = len(array_segments[:rith_index + 1])
            print(len_left_index - len_rith_index, end=' ')
        # array_segments.clear()

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
        #print(array_segments)
        binary_search(array_segments, point, i=1)
        print(len(_array), end=' ')
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
        #print(list_segments)
        list_points = list(map(int, file.readline().split()))
        #print(list_points)
    return list_segments, list_points


def input_data():
    list_segments, list_points = [], []
    n, m = map(int, input().split(' '))
    for _ in range(n):
        list_segments.append(list(map(int, input().split())))
    list_points = list(map(int, input().split()))
    return list_segments, list_points


def main():
    input_list, list_points = input_file()
    list_segments = input_list.copy()
    list_segments_sec = input_list.copy()

    # list_segments = quicksort(list_segments, i=0)
    list_segments = sorted(list_segments, key=lambda x: x[0])
    print(list_segments)

    # array_segments = quicksort(list_segments, i=1)
    array_segments = sorted(list_segments_sec, key=lambda x: x[1])

    start_time = time.time()
    serch_bound(list_segments, array_segments, list_points)
    print(time.time() - start_time)

    start_time = time.time()
    search_point(list_segments, list_points)
    print(time.time() - start_time)


if __name__ == "__main__":
    #start_time = time.time()
    main()
    #print(time.time() - start_time)
