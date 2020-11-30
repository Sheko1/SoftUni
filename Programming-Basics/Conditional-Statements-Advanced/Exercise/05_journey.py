budget = float(input())
season = input()

price = 0
vac = ""
type_vac = ""

if budget <= 100:
    if season == "summer":
        price = budget * 0.70
        vac = "Bulgaria"
        type_vac = "Camp"

    elif season == "winter":
        price = budget * 0.30
        vac = "Bulgaria"
        type_vac = "Hotel"

elif budget <= 1000:
    if season == "summer":
        price = budget * 0.60
        vac = "Balkans"
        type_vac = "Camp"

    elif season == "winter":
        price = budget * 0.20
        vac = "Balkans"
        type_vac = "Hotel"


else:
    if season == "summer":
        price = budget * 0.1
        vac = "Europe"
        type_vac = "Hotel"

    elif season == "winter":
        price = budget * 0.1
        vac = "Europe"
        type_vac = "Hotel"

total_money = budget - price

print(f"Somewhere in {vac}")
print(f"{type_vac} - {total_money:.2f}")
