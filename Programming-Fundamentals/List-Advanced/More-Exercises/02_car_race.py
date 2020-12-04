def time_calculator(side):
    result = 0
    for el in side:
        if el == 0:
            result *= 0.8

        else:
            result += el
    return result


data = [int(i) for i in input().split()]

half = len(data) // 2

left_side = data[:half]
right_side = data[-1:-half-1:-1]

left_time = time_calculator(left_side)
right_time = time_calculator(right_side)

if left_time < right_time:
    print(f"The winner is left with total time: {left_time:.1f}")

else:
    print(f"The winner is right with total time: {right_time:.1f}")