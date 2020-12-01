n = int(input())
positive_nums = []
negative_nums = []

for i in range(n):
    number = int(input())
    if number >= 0:
        positive_nums.append(number)

    if number < 0:
        negative_nums.append(number)

print(positive_nums)
print(negative_nums)
print(f"Count of positives: {len(positive_nums)}. Sum of negatives: {sum(negative_nums)}")
