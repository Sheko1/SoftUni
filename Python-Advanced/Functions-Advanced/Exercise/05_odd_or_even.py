def odd_sum(nums_list):
    return sum([num for num in nums_list if num % 2 != 0]) * len(nums_list)


def even_sum(nums_list):
    return sum([num for num in nums_list if num % 2 == 0]) * len(nums_list)


command = input()
nums_data = [int(num) for num in input().split()]
mapper = {"Odd": odd_sum(nums_data), "Even": even_sum(nums_data)}
print(mapper[command])
