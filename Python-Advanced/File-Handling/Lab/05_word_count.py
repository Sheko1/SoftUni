from re import findall


def get_words_from_file(path):
    with open(path, "r") as file:
        content = "".join(file.readlines())
        return findall(r"[a-z]+", content.lower())


words_to_search = get_words_from_file("words.txt")
text = get_words_from_file("input.txt")

result = {word: text.count(word) for word in words_to_search}
result = sorted(result.items(), key=lambda x: -x[1])

with open("output.txt", "w") as file:
    file.writelines("\n".join(f"{x[0]}-{x[1]}" for x in result))
