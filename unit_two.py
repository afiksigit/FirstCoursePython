# Bonus tasks - afik

# exercise 2.3.3
def pigs():
    rock_numbers = int(input("Please Enter 3 digits. each digit for diff pig:"))
    first_pig = rock_numbers % 10
    second_pig = rock_numbers % 100 // 10
    third_pig = rock_numbers // 100
    sum_rocks = first_pig + second_pig + third_pig
    print(sum_rocks)
    print(sum_rocks // 3)
    print(sum_rocks - (sum_rocks // 3) * 3)
    print(sum_rocks % 3 == 0)


def main():
    pigs()


if __name__ == '__main__':
    main()
