def rahim(num, num1, operator):
    result = None
    if operator == "multiply":
        result = num * num1
    elif operator == "divide":
        result = num // num1
    elif operator == "add":
        result = num + num1
    elif operator == "subtract":
        result = num - num1

    return result


operator = input()
num = int(input())
num1 = int(input())

print(rahim(num, num1, operator))
