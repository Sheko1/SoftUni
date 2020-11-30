days = int(input())
count_bakers = int(input())
count_cakes = int(input())
count_waffles = int(input())
count_pancakes = int(input())
price_cake = 45
price_waffles = 5.8
price_pancake = 3.2
cakes_per_day = count_cakes * price_cake
waffles_per_day = count_waffles * price_waffles
pancake_per_day = count_pancakes * price_pancake
total_sum_per_day = (cakes_per_day + waffles_per_day + pancake_per_day) * count_bakers
total_money = total_sum_per_day * days
result = total_money - 1/8 * total_money
print(result)