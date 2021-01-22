words = input().split()
filtered_words = [word for word in words if len(word) % 2 == 0]
[print(word) for word in filtered_words]
