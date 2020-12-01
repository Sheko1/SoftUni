def palindrome(list_of_integers):
    reverse_data = []

    for i in range(len(list_of_integers)):
        reversed_number = ""
        for index in range(1, len(list_of_integers[i]) + 1):
            reversed_number += list_of_integers[i][-index]
        reverse_data.append(reversed_number)

    for i in range(len(list_of_integers)):
        if list_of_integers[i] == reverse_data[i]:
            print("True")
        else:
            print("False")


numbers = input().split(", ")
palindrome(numbers)