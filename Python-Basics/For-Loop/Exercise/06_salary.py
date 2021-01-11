from math import floor
n = int(input())
salary = int(input())

fine = 0

for i in range(n):
    site = input()

    if site == "Facebook":
        fine += 150

    if site == "Instagram":
        fine += 100

    if site == "Reddit":
        fine += 50

    if fine >= salary:
        break

if fine >= salary:
    print("You have lost your salary.")

else:
    money_left = salary - fine
    print(floor(money_left))
