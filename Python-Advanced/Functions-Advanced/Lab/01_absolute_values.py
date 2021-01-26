def absolute_values(nums_data):
    return [abs(float(num)) for num in nums_data]


nums = input().split()
print(absolute_values(nums))
