# Bonus tasks - afik

import calendar
import datetime


# exercise 4.2.2
def is_palindrome():
    user_input = input("enter word: ")
    user_input = user_input.replace(" ", "").lower()
    if user_input == user_input[::-1]:
        print("OK")
    else:
        print("NOT")


# exercise 4.2.3
def convert_temp():
    temperature = input("enter the temperature to convert: ")
    if temperature[-1].lower() == 'c':
        temperature_c = float(temperature[:-1])
        temperature_f = (temperature_c * 9 / 5) + 32
        print(str(temperature_f) + "F")
    elif temperature[-1].lower() == 'f':
        temperature_f = float(temperature[:-1])
        temperature_c = (temperature_f - 32) * 5 / 9
        print(str(temperature_c) + "C")
    else:
        print("Invalid input")


# exercise 4.2.4
def info_date():
    date = input("Enter a date (dd/mm/yyyy): ")
    date_obj = datetime.datetime.strptime(date, '%d/%m/%Y')
    print(calendar.day_name[date_obj.weekday()])  # day


def main():
    is_palindrome()
    convert_temp()
    info_date()


if __name__ == '__main__':
    main()
