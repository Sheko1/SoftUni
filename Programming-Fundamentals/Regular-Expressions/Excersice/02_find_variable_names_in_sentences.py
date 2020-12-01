from re import finditer

sentence = input()

regex = r"((?<=^_)|(?<=\s_))[a-zA-Z0-9]+\b"

result = finditer(regex, sentence)
result = [i.group() for i in result]
print(','.join(result))