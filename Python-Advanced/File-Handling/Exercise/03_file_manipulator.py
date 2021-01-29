import os


def get_string_from_txt(file_name):
    with open(file_name, "r") as file:
        result = "".join(file.readlines())
        return result


def create_file(file_name):
    with open(file_name, "w"):
        pass


def add(file_name, content):
    if os.path.exists(file_name):
        with open(file_name, "a") as file:
            file.write(content + "\n")

    else:
        with open(file_name, "w") as file:
            file.write(content + "\n")


def replace(file_name, old_string, new_string):
    if os.path.exists(file_name):
        content = get_string_from_txt(file_name)
        content = content.replace(old_string, new_string)

        with open(file_name, "w") as file:
            file.writelines(content)

    else:
        print("An error occurred")


def delete(file_name):
    if os.path.exists(file_name):
        os.remove(file_name)

    else:
        print("An error occurred")


command = input()

while command != "End":
    command_data = command.split("-")

    if command_data[0] == "Create":
        name = command_data[1]
        create_file(name)

    elif command_data[0] == "Add":
        name, text = command_data[1:]
        add(name, text)

    elif command_data[0] == "Replace":
        name, old, new = command_data[1:]
        replace(name, old, new)

    elif command_data[0] == "Delete":
        name = command_data[1]
        delete(name)

    command = input()
