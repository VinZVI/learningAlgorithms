import time


def quicksort(list_segments):
    if len(list_segments) < 2:
        return list_segments
    else:
        pivot = list_segments[0]
        less = [segment for segment in list_segments[1:] if segment <= pivot]
        greater = [segment for segment in list_segments[1:] if segment > pivot]
        # print(less)
        return quicksort(less) + [pivot] + quicksort(greater)


import random

# for _ in range(n_iter):
# print(length)
# length = random.randint(1, 10)
a = [random.randint(1, 100000000) for _ in range(50000)]
b = a.copy()
c = a.copy()


# b = [random.randint(a, 100000) for _ in range(20)]
# print(a)

def test(a, b, c):
    start_time = time.time()
    sorted(a)
    print(time.time() - start_time)

    start_time = time.time()
    b.sort()
    print(time.time() - start_time)

    start_time = time.time()
    quicksort(c)
    print(time.time() - start_time)


def main():
    pass


if __name__ == "__main__":
    # start_time = time.time()
    test(a, b, c)
    # main()
    # print(time.time() - start_time)
