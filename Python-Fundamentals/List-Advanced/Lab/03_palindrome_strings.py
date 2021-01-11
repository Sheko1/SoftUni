text = input().split()
palindrome_search = input()

palindromes = []

for word in text:
    if word == word[::-1]:
        palindromes.append(word)

print(palindromes)
print(f"Found palindrome {palindromes.count(palindrome_search)} times")
