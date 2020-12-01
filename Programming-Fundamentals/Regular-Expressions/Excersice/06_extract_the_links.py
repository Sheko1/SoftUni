import re

line = input()
pattern = r"w{3}\.\b[A-Za-z0-9-]+\.[a-z]+[\.[a-z]+]?"
result = []
while line:
    result.extend(re.findall(pattern, line))

    line = input()

[print(email) for email in result]