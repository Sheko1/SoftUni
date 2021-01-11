def validator(password):
    is_valid = True
    if len(password) < 6 or len(password) > 10:
        is_valid = False
        print("Password must be between 6 and 10 characters")
    count = 0
    for i in range(len(password)):
        if password[i].isdigit():
            count += 1
        if not password[i].isdigit() and not password[i].isalpha():
            is_valid = False
            print("Password must consist only of letters and digits")
            break

    if count < 2:
        is_valid = False
        print("Password must have at least 2 digits")

    if is_valid:
        print("Password is valid")


pas = input()
validator(pas)