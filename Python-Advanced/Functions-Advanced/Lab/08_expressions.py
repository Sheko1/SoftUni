def expressions(nums_list, current_sum=0, expression=""):
    if not nums_list:
        print(f"{expression}={current_sum}")
        return

    expressions(nums_list[1:], current_sum+nums_list[0], f"{expression}+{nums_list[0]}")
    expressions(nums_list[1:], current_sum-nums_list[0], f"{expression}-{nums_list[0]}")


nums = [int(num) for num in input().split(", ")]
expressions(nums)
