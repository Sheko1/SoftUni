from math import floor
record = float(input())
meters = float(input())
time_for_one_meter = float(input())

time = meters * time_for_one_meter
time1 = floor((meters / 50)) * 30
time += time1

if time < record:
    print(f"Yes! The new record is {time:.2f} seconds.")

else:
    print(f"No! He was {time - record:.2f} seconds slower.")
