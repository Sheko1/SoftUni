import re
phones = input()

pattern = r'(?P<day>\b\d{2})([-\./])(?P<month>[A-Z][a-z]{2})\2(?P<year>\d{4}\b)'
matches = re.finditer(pattern, phones)

for m in matches:
    d = m.groupdict()
    print(f"Day: {d['day']}, Month: {d['month']}, Year: {d['year']}")
