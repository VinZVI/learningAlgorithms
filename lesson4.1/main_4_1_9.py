def find_point(segments):
    list_point = []
    for seg in segments:
        if len(list_point) != 0:
            if seg[0] > list_point[-1]:
                list_point.append(seg[1])
        else:
            list_point.append(seg[1])
    # print(list_point)
    print(len(list_point))
    print(*list_point, end=' ')
    print(' '.join(map(str, list_point)))
    # for i in list_point:
    #     print(i, end=' ')


def input_segments():
    segments = []
    # count = int(input())
    for _ in range(int(input())):
        l, r = map(int, input().split())
        segments.append([l, r])

    # print(segments)
    return segments


def main():
    # print(input_segments())
    all_segments = [[[1, 2], [3, 4], [0, 5]], [[0, 0], [1, 1], [2, 2], [0, 3]]]
    for segments in all_segments:
        # segments = input_segments()
        segments.sort(key=lambda x: x[1])
        find_point(segments)


if __name__ == "__main__":
    main()
