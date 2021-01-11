import re
phones = input()

pattern = r"(^|(?<=\s))-?\d+(\.\d+)?($|(?=\s))"
matches = re.finditer(pattern, phones)
matches = [m.group() for m in matches]
print(' '.join(matches))
