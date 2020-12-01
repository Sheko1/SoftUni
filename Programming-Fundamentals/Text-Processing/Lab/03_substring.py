word_to_remove = input()
string = input()

while word_to_remove in string:
    string = string.replace(word_to_remove, "")

print(string)
