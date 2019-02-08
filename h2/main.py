import statistics


def get_mean(int_list):
    total = 0
    list_len = len(int_list)
    for num in int_list:
        total += num
    return total/list_len


def get_mode(int_list):
    try:
        return statistics.mode(int_list)
    except statistics.StatisticsError:
        return "No mode"


def main():
    print(get_mean([5, 4, 3, 2, 1]))
    print(get_mean([1, 2, 6, 9, 3]))
    print(get_mode([1, 2, 3, 4, 4]))
    print(get_mode([1, 2, 3]))
    print(get_mode([1, 4, 2, 3, 4, 5, 5, 5, 7, 7]))


main()

