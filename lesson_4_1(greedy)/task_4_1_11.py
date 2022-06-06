import time


def find_point(number):
    list_natural_terms = []
    term = 1
    while number > term * 2:
        number -= term
        list_natural_terms.append(term)
        # if number in list_natural_terms:
        #     break
        term += 1
    list_natural_terms.append(number)
    print(len(list_natural_terms))
    print(*list_natural_terms, end=' ')
    print('\n')


def main():
    find_point(int(input()))
    # all_segments = [1, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    # for segments in all_segments:
    #     find_point(segments)


if __name__ == "__main__":
    start_time = time.time()
    main()
    print(time.time() - start_time)
