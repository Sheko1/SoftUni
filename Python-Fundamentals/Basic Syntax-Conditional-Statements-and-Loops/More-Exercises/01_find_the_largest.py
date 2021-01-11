number = input()
result = []
for num in number:
    result.append(num)

print(''.join(sorted(result, reverse=True)))