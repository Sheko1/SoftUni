from re import findall


def replace_chars(text):
    chars_to_replace = ("-", ",", ".", "!", "?")

    for char in chars_to_replace:
        text = text.replace(char, "@")

    return text


with open("text.txt", "r") as file:
    line_count = 0
    result = ""

    while True:
        curr_line = file.readline()
        if not curr_line:
            break

        if line_count % 2 == 0:
            result += " ".join(reversed(findall(r"[a-zA-Z-,.'!?]+", curr_line))) + "\n"

        line_count += 1

    result = replace_chars(result)
    print(result)
