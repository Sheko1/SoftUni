def needed_coffee(event_1, coffee_1):
    if event.isupper():
        coffee_1[0] += 2

    else:
        coffee_1[0] += 1

    return coffee_1


event = input()

coffee = [0]
is_more_than_5 = False

while event != "END":
    if event.lower() == "coding":
        needed_coffee(event, coffee)

    elif event.lower() == "dog" or event.lower() == "cat":
        needed_coffee(event, coffee)

    elif event.lower() == "movie":
        needed_coffee(event, coffee)

    if coffee[0] > 5:
        is_more_than_5 = True
        break

    event = input()

if is_more_than_5:
    print("You need extra sleep")

else:
    print(coffee[0])