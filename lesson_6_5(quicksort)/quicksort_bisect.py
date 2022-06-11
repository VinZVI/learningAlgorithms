import time
from bisect import bisect_left, bisect_right


def serch_bound(list_segments, array_segments, list_points):
    for point in list_points:
        left_index = bisect_right(list_segments, point, key=lambda x: x[0])
        rith_index = bisect_left(array_segments, point, key=lambda x: x[1])
        print(left_index - rith_index, end=' ')

        # if left_index == 0 and rith_index == 0:
        #     print(0, end=' ')
        #
        # else:
        #     len_left_index = len(list_segments[:left_index])
        #     len_rith_index = len(array_segments[:rith_index])
        #     print(len_left_index - len_rith_index, end=' ')


def input_file():
    list_segments, list_points = [], []
    with open("exmpl.txt", 'r') as file:
        # print(file.read())
        n, m = map(int, file.readline().split(' '))
        for _ in range(n):
            list_segments.append(list(map(int, file.readline().split())))
        # print(list_segments)
        list_points = list(map(int, file.readline().split()))
        # print(list_points)
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


if __name__ == "__main__":
    # start_time = time.time()
    main()
    # print(time.time() - start_time)
