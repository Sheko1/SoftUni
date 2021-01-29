from re import findall


def write_output(result_list):
    with open("output.txt", "w") as f:
        [f.write(line + "\n") for line in result_list]


with open("text.txt", "r") as file:
    line_count = 1
    result = []

    while True:
        curr_line = file.readline()
        curr_line = curr_line.replace("\n", "")

        if not curr_line:
            break

        letters_count = len(findall(r"[a-zA-Z]", curr_line))
        punctuation_marks_count = len(findall(r"[^\w\s]", curr_line))

        result.append(f"Line {line_count}: {curr_line} ({letters_count})({punctuation_marks_count})")

    write_output(result)
