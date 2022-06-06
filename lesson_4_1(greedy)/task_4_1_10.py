def find_cost(volume, items):
    # volume_backpack = 0
    cost_backpack: float = 0
    for item in items:
        # print(volume - volume_backpack)
        # if item[1] <= (volume - volume_backpack):
        if item[1] <= volume:
            cost_backpack += item[0]
            volume -= item[1]
            # volume_backpack += item[1]
        else:
            cost_backpack += (item[0] / item[1]) * volume
            volume -= volume
    return print(f'{cost_backpack:.3f}')
    # volume -= item[1]
    # print((item[0]/item[1])*(volume - volume_backpack))
    # cost_backpack += (item[0]/item[1])*(volume - volume_backpack)
    # volume_backpack += (volume - volume_backpack)
    # print(round(cost_backpack, 3))


def input_data():
    items = []
    n, volume = map(float, input().split())
    for _ in range(n):
        cost, size = map(float, input().split())
        items.append([cost, size])
    items.sort(key=lambda x: x[0] / x[1])
    items.reverse()
    # print(segments)
    return volume, items


def main():
    # print(input_data())
    all_segments = [(100, [[80, 40], [60, 20], [120, 30]]), (12, [[80, 10], [60, 10]]),
                    (9022, [[3316, 1601], [5375, 8940], [2852, 6912], [3336, 9926], [1717, 8427]])]
    for volume, items in all_segments:
        items.sort(key=lambda x: x[0] / x[1], reverse=True)
        # items.reverse()
        print(volume, items)
        find_cost(volume, items)


if __name__ == "__main__":
    main()
