def perfect_number(num):
    ismet = [6, 28, 496, 8128, 33550336, 8589869056, 137438691328, 2305843008139952128]
    if num in ismet:
        return "We have a perfect number!"
    else:
        return "It's not so perfect."


number = int(input())
print(perfect_number(number))