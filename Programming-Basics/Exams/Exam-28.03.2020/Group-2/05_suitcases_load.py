trunk = float(input())
command = input()

suitcase = 0

while command != "End":
    number = float(command)
    suitcase += 1
    if suitcase % 3 == 0:
        number += number * 0.1

    trunk -= number
    if trunk <= 0:
        suitcase -= 1
        break
    command = input()

if trunk > 0:
    print("Congratulations! All suitcases are loaded!")

else:
    print("No more space!")

print(f"Statistic: {suitcase} suitcases loaded.")
