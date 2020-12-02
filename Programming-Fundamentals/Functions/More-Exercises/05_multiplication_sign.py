def positive_or_negative(num1, num2, num3):
    if num1 == 0 or num2 == 0 or num3 == 0:
        return "zero"

    elif num1 * num2 * num3 < 0:
        return "negative"

    else:
        return "positive"


num_1 = int(input())
num_2 = int(input())
num_3 = int(input())

print(positive_or_negative(num_1, num_2, num_3))