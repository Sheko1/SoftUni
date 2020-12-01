import re

text = input()

pattern = r"(@|#)(?P<first_word>[a-zA-Z]{3,}\b)\1\1(?P<second_word>[a-zA-Z]{3,})\1"
matches = re.finditer(pattern, text)
count = 0
result = []


for match in matches:
    obj = match.groupdict()
    count += 1

    if obj['first_word'] == obj['second_word'][::-1]:
        result.append(f"{obj['first_word']} <=> {obj['second_word']}")


if count == 0:
    print('No word pairs found!\nNo mirror words!')

else:
    print(f'{count} word pairs found!')

    if len(result) > 0:
        print(f"The mirror words are:\n{', '.join(result)}")

    else:
        print('No mirror words!')
