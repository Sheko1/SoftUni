from math import floor
hours = int(input())
minutes = int(input())
hours_1 = hours * 60
total = hours_1 + minutes + 15
total_hours = total / 60
total_minutes = total % 60

if total_hours >= 24:
    total_hours = 0

if total_minutes < 10:
    print(f"{floor(total_hours)}:0{floor(total_minutes)}")

else:
    print(f"{floor(total_hours)}:{floor(total_minutes)}")
