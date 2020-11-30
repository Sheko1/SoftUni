import re

text = input()
word = input()

result = re.findall(f"\\b{word}\\b", text, re.IGNORECASE)
print(len(result))