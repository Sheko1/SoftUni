import re
phones = input()

pattern = r"(^|(?<=\s))\+359([\s-])2\2\d{3}\2\d{4}\b"
matches = re.finditer(pattern, phones)
matches = [match.group() for match in matches]
print(', '.join(matches))
