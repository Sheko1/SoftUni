email = input()
command = input()

while command != "Complete":
    if command == "Make Upper":
        email = email.upper()
        print(email)

    elif command == "Make Lower":
        email = email.lower()
        print(email)

    elif command.split()[0] == "GetDomain":
        count = int(command.split()[1])
        domain = email[-1:-1-count:-1]
        print(domain[::-1])

    elif command == "GetUsername":
        if "@" in email:
            index = email.index("@")
            print(email[:index])

        else:
            print(f"The email {email} doesn't contain the @ symbol.")

    elif command.split()[0] == "Replace":
        char = command.split()[1]
        email = email.replace(char, "-")
        print(email)

    elif command == "Encrypt":
        [print(ord(char), end=" ") for char in email]

    command = input()