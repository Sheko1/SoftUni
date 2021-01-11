min_walk = int(input())
walk_per_day = int(input())
cat_calories = int(input())

total_min = min_walk * walk_per_day
calories = total_min * 5

calories_percent = calories / cat_calories * 100

if calories_percent >= 50:
    print(f"Yes, the walk for your cat is enough. Burned calories per day: {calories}.")

else:
    print(f"No, the walk for your cat is not enough. Burned calories per day: {calories}.")
