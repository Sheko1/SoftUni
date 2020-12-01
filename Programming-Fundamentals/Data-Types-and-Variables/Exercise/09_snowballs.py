n = int(input())

snow_value = 0
highest_value = 0
snow = 0
time = 0
quality = 0

for i in range(n):
    snowball_snow = int(input())
    snowball_time = int(input())
    snowball_quality = int(input())

    snow_value = (snowball_snow / snowball_time) ** snowball_quality

    if snow_value > highest_value:
        highest_value = snow_value
        snow = snowball_snow
        time = snowball_time
        quality = snowball_quality

print(f"{snow} : {time} = {int(highest_value)} ({quality})")
