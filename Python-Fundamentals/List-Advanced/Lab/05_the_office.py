def factor_map(data, num):
    for index in range(len(data)):
        data[index] *= num
    return data


def average_happiness(data):
    result = 0

    for num in data:
        result += num

    return result / len(data)


employee_happiness = [int(num) for num in input().split()]
factor = int(input())

employee_happiness_score = factor_map(employee_happiness, factor)
average_score = average_happiness(employee_happiness_score)

count = 0

for score in employee_happiness_score:
    if score >= average_score:
        count += 1

if count > len(employee_happiness_score) // count:
    print(f"Score: {count}/{len(employee_happiness_score)}. Employees are happy!")

else:
    print(f"Score: {count}/{len(employee_happiness_score)}. Employees are not happy!")
