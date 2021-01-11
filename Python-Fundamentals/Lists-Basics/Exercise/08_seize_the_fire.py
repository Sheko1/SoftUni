HIGH_RANGE = range(81, 126)
MEDIUM_RANGE = range(51, 81)
LOW_RANGE = range(1, 51)

fire = input().split("#")
water = int(input())
value_data = []
effort = 0

for i in fire:
    type_fire, value = i.split(" = ")
    value = int(value)

    if (
            type_fire == "High" and value not in HIGH_RANGE or
            type_fire == "Medium" and value not in MEDIUM_RANGE or
            type_fire == "Low" and value not in LOW_RANGE
    ):
        continue

    if water >= value:
        water -= value
        effort += value * 0.25
        value_data.append(value)

print("Cells:")

for i in value_data:
    print(f" - {i}")

print(f"Effort: {effort:.2f}")
print(f"Total Fire: {sum(value_data)}")
