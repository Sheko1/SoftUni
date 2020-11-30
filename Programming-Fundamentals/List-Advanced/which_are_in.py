first_string = input().split(", ")
second_string = input()

words = list(filter(lambda x: x in second_string, first_string))

print(words)