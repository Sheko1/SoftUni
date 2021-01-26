def round_values(nums_data):
    return [round(num) for num in nums_data]


nums = [float(num) for num in input().split()]
print(round_values(nums))
