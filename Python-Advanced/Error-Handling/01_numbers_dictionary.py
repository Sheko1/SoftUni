numbers_dictionary = {}

while True:
    number_as_text = input()

    if number_as_text == "Search":
        break

    try:
        number_as_int = int(input())

    except ValueError:
        print("The variable number must be an integer")
        continue

    numbers_dictionary[number_as_text] = number_as_int


line = input()

while line != "Remove":
    try:
        print(numbers_dictionary[line])

    except KeyError:
        print("Number does not exist in dictionary")

    line = input()

number_to_remove = input()

while number_to_remove != "End":
    try:
        del numbers_dictionary[number_to_remove]

    except KeyError:
        print("Number does not exist in dictionary")

    number_to_remove = input()
