import re

text = input()

pattern = r"(^|(?<=\s))[a-zA-Z0-9]+([\._-][a-z0-9]+)?@[a-z]+(-[a-z]+)?\.[a-z]+[\.[a-z]+]?\b"
match = re.finditer(pattern, text)
match = [print(i.group()) for i in match]