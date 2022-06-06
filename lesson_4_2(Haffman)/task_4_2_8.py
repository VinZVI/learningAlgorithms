import time


def decode_huffman(dict_code, input_string):
    result_string = ''
    l = ''
    for i in input_string:
        i = l + i
        if i in dict_code:
            result_string += dict_code[i]
            l = ''
        else:
            l = i
    return result_string


def input_data():
    dict_code = {}
    n, len_string = map(int, input().split())
    while n:
        n -= 1
        k, v = [x.strip() for x in input().split(':')]
        dict_code.update({v: k})
    input_string = input()
    return dict_code, input_string


def main():
    # print(input_data())
    dict_code, input_string = input_data()
    print(decode_huffman(dict_code, input_string))
    # all_segments = [1, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    # for segments in all_segments:
    #     find_point(segments)


if __name__ == "__main__":
    start_time = time.time()
    main()
    print(time.time() - start_time)
