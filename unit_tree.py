# Bonus tasks - afik

# exercise 3.2.1
def shuffle_taki():
    print('"Shuffle, Shuffle, Shuffle", say it together! \n Change colors and directions, Don\'t back down and stop '
          'the player! \n \tDo you want to play Taki? \n \tPress y\\n')


# exercise 3.3.3
def decryption():
    encrypted_message = "!XgXnXiXcXiXlXsX XnXoXhXtXyXpX XgXnXiXnXrXaXeXlX XmXaX XI"
    print(encrypted_message[::-2])


# exercise 3.4.2
def change_to_e():
    letter_to_switch = 'e'
    sentence = input("enter a string: ")
    print(sentence[0] + sentence[1::].replace(sentence[0], letter_to_switch))


# exercise 3.4.3
def lower_upper():
    user_str = input("enter string: ")
    first_part = user_str[:len(user_str) // 2]
    second_part = user_str[len(user_str) // 2:]
    print(first_part.lower() + second_part.upper())


def main():
    shuffle_taki()
    change_to_e()
    lower_upper()


if __name__ == '__main__':
    main()
