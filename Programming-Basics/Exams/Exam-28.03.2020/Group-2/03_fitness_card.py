money = float(input())
sex = input()
age = int(input())
type_sport = input()

price = 0

if sex == "m":
    if type_sport == "Gym":
        price = 42

    elif type_sport == "Boxing":
        price = 41

    elif type_sport == "Yoga":
        price = 45

    elif type_sport == "Zumba":
        price = 34

    elif type_sport == "Dances":
        price = 51

    elif type_sport == "Pilates":
        price = 39

elif sex == "f":
    if type_sport == "Gym":
        price = 35

    elif type_sport == "Boxing":
        price = 37

    elif type_sport == "Yoga":
        price = 42

    elif type_sport == "Zumba":
        price = 31

    elif type_sport == "Dances":
        price = 53

    elif type_sport == "Pilates":
        price = 37


if age <= 19:
    price *= 0.8

if price <= money:
    print(f"You purchased a 1 month pass for {type_sport}.")

else:
    print(f"You don't have enough money! You need ${price - money:.2f} more.")
