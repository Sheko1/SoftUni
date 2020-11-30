food_bought = int(input())
command = input()

food = 0

while command != "Adopted":
    food += int(command)

    command = input()

if food <= (food_bought * 1000):
    print(f"Food is enough! Leftovers: {(food_bought * 1000) - food} grams.")

else:
    print(f"Food is not enough. You need {food - (food_bought * 1000)} grams more.")
