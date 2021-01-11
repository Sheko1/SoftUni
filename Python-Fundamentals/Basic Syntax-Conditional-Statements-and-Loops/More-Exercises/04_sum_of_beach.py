word = input().lower()

count_words = ["sand", "water", "fish", "sun"]
result = 0

for w in count_words:
    result += word.count(w)

print(result)
