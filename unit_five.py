# Bonus tasks - afik

# exercise 5.3.4
def last_early(user_str):
    user_str = user_str.lower()
    last_char = user_str[-1]
    return last_char in user_str[:-1]


# exercise 5.3.5
def distance(num1, num2, num3):
    if abs(num2 - num1) <= 1 and abs(num3 - num1) >= 2 and abs(num2 - num3) >= 2:
        return True
    elif abs(num2 - num3) <= 1 and abs(num1 - num2) >= 2 and abs(num1 - num3) >= 2:
        return True
    elif abs(num3 - num1) <= 1 and abs(num2 - num1) >= 2 and abs(num2 - num3) >= 2:
        return True
    else:
        return False


# exercise 5.3.6

def filter_teens(a=13, b=13, c=13):
    return fix_the_age(a) + fix_the_age(b) + fix_the_age(c)


def fix_the_age(age):
    if 13 <= age <= 19 and age != 15 and age != 16:
        return 0
    else:
        return age


# exercise 5.3.7
def chocolate_maker(small_cube, big_cube, x):
    max_big_cubes = x // 5
    big_cubes_needed = min(max_big_cubes, big_cube)
    small_cubes_needed = x - big_cubes_needed * 5
    return small_cubes_needed <= small_cube


# exercise 5.4.1
def fun(num1, num2):
    """
        This function takes two numbers, num1 and num2, and returns their sum.

        Parameters:
        num1 (int or float): the first number
        num2 (int or float): the second number

        Returns:
        int or float: the sum of num1 and num2
        """
    return num1 + num2


def main():
    print(last_early("hello sigit"))

    print(distance(7, 4, 2))

    print(filter_teens(1, 11, 3))

    print(chocolate_maker(3, 1, 9))

    print(fun(2, 6))
    help(fun)


if __name__ == '__main__':
    main()
