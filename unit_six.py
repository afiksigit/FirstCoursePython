# Bonus tasks - afik

# exercise 6.1.2
def shift_left(list):
    """
    :param list:
    :return: shift the list one step left
    """
    return list[1:] + [list[0]]


# exercise 6.2.3
def format_list(list):
    """
    :param list:
    :return: with ,
    """
    return ", ".join(list[::2][:-1]) + ", and " + list[-1]


# exercise 6.2.4
def extend_list_x(list_x, list_y):
    """
    Concatenate two lists where list_y is added to the beginning of list_x
    :param list_x:
    :param list_y: list to be added to the beginning of list_x
    :return: the extended list_x
    """
    for i in list_x:
        list_y.append(i)
    return list_y


# exercise 6.3.1
def are_lists_equal(list1, list2):
    """
    :param list1:
    :param list2:
    :return: if the list has same elements
    """
    return set(list1) == set(list2) and len(list1) == len(list2)


# exercise 6.3.2
def longest(my_list):
    """
    :param my_list:
    :return: the longest word
    """
    return max(my_list, key=len)


def main():
    print(shift_left(['monkey', 2.0, 1]))

    print(format_list(["hydrogen", "helium", "lithium", "beryllium", "boron", "magnesium"]))

    x = [4, 5, 6]
    y = [1, 2, 3]
    print(extend_list_x(x, y))

    list1 = [5, 1, 2, 7]
    list2 = [7, 2, 5, 1]
    list3 = [9, 0, 8, 11.5]
    print(are_lists_equal(list1, list2))
    print(are_lists_equal(list1, list3))

    print(longest(["111", "234", "2000", "goru", "birthday", "09"]))


if __name__ == '__main__':
    main()
