import re

text = input()
pattern = r"(#|\|)(?P<name>[a-zA-Z ]+)\1(?P<date>\d{2}/\d{2}/\d{2})\1(?P<calories>\d+)\1"
matches = re.finditer(pattern, text)
result = []
total_cal = 0

for match in matches:
    obj = match.groupdict()
    total_cal += int(obj['calories'])
    result.append(f"Item: {obj['name']}, Best before: {obj['date']}, Nutrition: {obj['calories']}")

print(f"You have food to last you for: {total_cal//2000} days!")
[print(item) for item in result]
