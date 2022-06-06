import time


def huffman(liters):
    liters.sort(key=lambda x: x[1])
    print(liters)
    dict_code = {}
    n = len(liters)
    if n == 1:
        dict_code.update({liters[0][0]: '0'})
    for k in range(n + 1, 2 * n):
        liters.sort(key=lambda x: x[1])
        fist_el = liters.pop(0)
        second_el = liters.pop(0)
        for el_left in fist_el[0]:
            count = dict_code.get(el_left)
            if count == None:
                dict_code.update({el_left: '0'})
            else:
                dict_code[el_left] = '0' + dict_code[el_left]
        for el_rite in second_el[0]:
            count = dict_code.get(el_rite)
            if count == None:
                dict_code.update({el_rite: '1'})
            else:
                dict_code[el_rite] = '1' + dict_code[el_rite]
        liters.append([fist_el[0] + second_el[0], fist_el[1] + second_el[1]])

    return dict_code


def input_data():
    liters = []
    input_string = input()
    set_list = set([i for i in input_string])
    for liter in set_list:
        frequency = input_string.count(liter)
        liters.append([liter, frequency])
    return input_string, liters


def output_data(input_string, dict_code):
    otput_string = ''
    for liter in input_string:
        otput_string += dict_code[liter]
    print(len(dict_code), len(otput_string))
    for key, value in dict_code.items():
        print(f'{key}:{value}')
    print(otput_string)


def main():
    # print(input_data())
    input_string, liters = input_data()
    output_data(input_string, huffman(liters))
    # all_segments = [1, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    # for segments in all_segments:
    #     find_point(segments)


if __name__ == "__main__":
    start_time = time.time()
    main()
    print(time.time() - start_time)
