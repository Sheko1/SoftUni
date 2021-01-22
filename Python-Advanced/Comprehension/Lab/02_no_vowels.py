VOWELS = ['a', 'o', 'u', 'e', 'i']
result = [ch for ch in input() if ch.lower() not in VOWELS]
print("".join(result))
