month = input()
nights = int(input())

apart = 0
studio = 0

if month == "May" or month == "October":
    apart = nights * 65
    studio = nights * 50

    if 7 < nights <= 14:
        studio = nights * (50 * 0.95)
        apart = nights * 65

    elif nights > 14:
        studio = nights * (50 * 0.7)
        apart = nights * (65 * 0.9)


elif month == "June" or month == "September":
    apart = nights * 68.70
    studio = nights * 75.20

    if nights > 14:
        studio = nights * (75.20 * 0.8)
        apart = nights * (68.70 * 0.9)

else:
    apart = nights * 77
    studio = nights * 76

    if nights > 14:
        apart = nights * (77 * 0.9)

print(f"Apartment: {apart:.2f} lv.")
print(f"Studio: {studio:.2f} lv.")
