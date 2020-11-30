from math import floor
word_record = float(input())
distance = float(input())
time = float(input())

time_distance = distance * time
time1 = floor((distance / 15)) * 12.5
total_time = time_distance + time1
needed_time = total_time - word_record

if word_record > total_time:
    print(f"Yes, he succeeded! The new world record is {total_time:.2f} seconds.")

else:
    print(f"No, he failed! He was {needed_time:.2f} seconds slower.")
