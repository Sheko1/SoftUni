def get_positive_numbers(nums_list):
    return [num for num in nums_list if num >= 0]


def get_negative_numbers(nums_list):
    return [num for num in nums_list if num < 0]


def get_positive_and_negative_sum(positive_nums, negative_nums):
    return sum(positive_nums), sum(negative_nums)


num_data = [int(num) for num in input().split()]

positive_numbers = get_positive_numbers(num_data)
negative_numbers = get_negative_numbers(num_data)

positive_sum, negative_sum = get_positive_and_negative_sum(positive_numbers, negative_numbers)

print(f"{negative_sum}\n{positive_sum}")

if positive_sum > abs(negative_sum):
    print("The positives are stronger than the negatives")

elif abs(negative_sum) > positive_sum:
    print("The negatives are stronger than the positives")
