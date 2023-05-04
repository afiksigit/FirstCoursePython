# Bonus tasks - afik

# exercise 8.2.1
def format_change():
    data = ("self", "py", 1.543)
    format_string = "Hello {}.{} learner, you have only {:.1f} units left before you master the course!"
    print(format_string.format(data[0], data[1], data[2]))


# exercise 8.2.2
def sort_prices(list_of_tuples):
    return sorted(list_of_tuples, key=lambda x: float(x[1]), reverse=True)


# exercise 8.2.3
def mult_tuple(tuple1, tuple2):
    result = ()
    for i in tuple1:
        for j in tuple2:
            result += ((i, j), (j, i))
    return result


# exercise 8.2.4
def sort_anagrams(list_of_strings):
    anagrams = {}
    for word in list_of_strings:
        key = ''.join(sorted(word))
        print(key)
        if key in anagrams:
            anagrams[key].append(word)
        else:
            anagrams[key] = [word]
    return list(anagrams.values())


# exercise 8.3.2
def menu2():
    mariah = {"first_name": "Mariah",
              "last_name": "Carey",
              "birth_date": "27.03.1970",
              "hobbies": ["Sing", "Compose", "Act"]}

    choice = int(input("Enter a number between 1 and 7: "))

    if choice == 1:
        print(mariah["last_name"])

    elif choice == 2:
        birth_date = mariah["birth_date"]
        month = birth_date[3:5]
        print(month)

    elif choice == 3:
        num_hobbies = len(mariah["hobbies"])
        print(num_hobbies)

    elif choice == 4:
        last_hobby = mariah["hobbies"][-1]
        print(last_hobby)

    elif choice == 5:
        mariah["hobbies"].append("Cooking")
        print(mariah["hobbies"])

    elif choice == 6:
        birth_date = mariah["birth_date"]
        day = int(birth_date[:2])
        month = int(birth_date[3:5])
        year = int(birth_date[6:])
        birth_tuple = (day, month, year)
        print(birth_tuple)

    elif choice == 7:
        birth_date = mariah["birth_date"]
        birth_year = int(birth_date[6:])
        current_year = 2023
        age = current_year - birth_year
        mariah["age"] = age
        print(mariah["age"])


# exercise 8.3.3
def count_chars(my_str):
    my_dict = {}
    for char in my_str:
        if char != ' ':
            if char in my_dict:
                my_dict[char] += 1
            else:
                my_dict[char] = 1
    return my_dict


# exercise 8.3.4
def inverse_dict(my_dict):
    new_dict = {}
    for key, value in my_dict.items():
        if value not in new_dict:
            new_dict[value] = [key]
        else:
            new_dict[value].append(key)
    for key in new_dict:
        new_dict[key] = sorted(new_dict[key])
    return new_dict


def main():
    format_change()

    print(sort_prices([('milk', '5.5'), ('candy', '2.5'), ('bread', '9.0')]))

    first_tuple = (1, 2)
    second_tuple = (4, 5)
    print(mult_tuple(first_tuple, second_tuple))

    print(sort_anagrams(
        ['deltas', 'retainers', 'desalt', 'pants', 'slated', 'generating', 'ternaries', 'smelters', 'termless',
         'salted', 'staled', 'greatening', 'lasted', 'resmelts']))

    menu2()

    magic_str = "abra cadabra"
    print(count_chars(magic_str))

    print(inverse_dict({'I': 3, 'love': 3, 'self.py!': 2}))


if __name__ == '__main__':
    main()