# Bonus tasks - afik

# exercise 7.1.4
def squared_numbers(start, stop):
    """
    :param start:
    :param stop:
    :return: squared
    """
    new_list = []
    i = start
    j = stop
    while i <= j:
        new_list.append(i * i)
        i = i + 1
    return new_list


# exercise 7.2.1
def is_greater(my_list, n):
    """
    :param my_list:
    :param n:
    :return: only the long
    """
    new_list = []
    for item in my_list:
        if int(item) > n:
            new_list.append(item)
    return new_list


# exercise 7.2.2
def numbers_letters_count(my_str):
    """
   :param my_str:
   :return: list
   """
    num_digits = sum(1 for c in my_str if c.isdigit())
    num_letters = sum(1 for c in my_str if c.isalpha() or c.isspace() or c in string.punctuation)
    return [num_digits, num_letters]


# exercise 7.2.4
def seven_boom(end_number):
    """
    :param end_number:
    :return: seven BOOM list
    """
    new_list = []
    for i in range(0, end_number + 1):
        if i % 7 == 0 or '7' in str(i):
            new_list.append("BOOM")
        else:
            new_list.append(i)
    return new_list


# exercise 7.2.5
def sequence_del(my_str):
    """
    :param my_str:
    :return: DISTINCT
    """
    new_str = ""
    for char in my_str:
        if not char in new_str:
            new_str = new_str + char
    return new_str


# exercise 7.2.6
def print_products(products):
    print("Product list:")
    print(", ".join(products))


def print_num_products(products):
    print("Number of products:", len(products))


def is_product_in_list(products, product_name):
    if product_name in products:
        print("Yes, {} is on the list".format(product_name))
    else:
        print("No, {} is not on the list".format(product_name))


def print_product_count(products, product_name):
    count = products.count(product_name)
    print("The product {} appears {} times in the list".format(product_name, count))


def remove_product(products, product_name):
    if product_name in products:
        products.remove(product_name)
        print("{} was removed from the list".format(product_name))
    else:
        print("Product not found in list")


def add_product(products, product_name):
    products.append(product_name)
    print("{} was added to the list".format(product_name))


def print_invalid_products(products):
    invalid_products = [p for p in products if len(p) < 3 or not p.isalpha()]
    if invalid_products:
        print("Invalid products:", ", ".join(invalid_products))
    else:
        print("No invalid products found")


def remove_duplicates(products):
    unique_products = list(set(products))
    print("List with duplicates removed:")
    print_products(unique_products)


def menu():
    products_str = input("Enter list of products, separated by commas: ")
    products = products_str.split(",")

    while True:
        print("\nmenu:")
        print("a. product list")
        print("b.  number of products")
        print("c. is product on list")
        print("d. how many times does a product appear?")
        print("e. remove product from list")
        print("f. add product to list")
        print("g. print invalid products")
        print("h. remove duplicates from list")
        print("j. exit program")

        choice = input("enter choice between 1-9: ")

        if choice == "1":
            print_products(products)
        elif choice == "2":
            print_num_products(products)
        elif choice == "3":
            product_name = input(" product name: ")
            is_product_in_list(products, product_name)
        elif choice == "4":
            product_name = input(" product name: ")
            print_product_count(products, product_name)
        elif choice == "5":
            product_name = input(" product name to remove: ")
            remove_product(products, product_name)
        elif choice == "6":
            product_name = input(" product name to add: ")
            add_product(products, product_name)
        elif choice == "7":
            print_invalid_products(products)
        elif choice == "8":
            remove_duplicates(products)
        elif choice == "9":
            break
        else:
            print("Wrong enter a number between 1 and 9.")


# exercise 7.2.7
def arrow(my_char, max_length):
    """
    :param my_char:
    :param max_length:
    :return: shape
    """
    new_str = ""
    for i in range(max_length):
        new_str = new_str + (i + 1) * my_char + "\n"
    for j in range(max_length - 1, 0, -1):
        new_str = new_str + j * my_char + "\n"
    return new_str


def main():
    print(squared_numbers(5, 9))

    print(is_greater([1, 30, 25, 60, 27, 28], 28))

    print(numbers_letters_count("Python 3.6.3"))

    print(seven_boom(17))

    print(sequence_del("ppyyyyythhhhhooonnnnn"))

    menu()

    print(arrow('*', 5))


if __name__ == '__main__':
    main()
