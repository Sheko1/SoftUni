command = input()
items = {}

while command != "statistics":
    key, value = command.split(": ")
    value = int(value)

    if key not in items:
        items[key] = value

    else:
        items[key] += value

    command = input()

print("Products in stock:")

for key, value in items.items():
    print(f"- {key}: {value}")

print(f"Total Products: {len(items)}\nTotal Quantity: {sum(items.values())}")
