def expression(nums):
    if not nums:
        print(nums)

    expression(nums[1:])
    expression(nums[1:])


expression([int(i) for i in input().split(", ")])
