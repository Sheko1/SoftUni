type_cinema = input()
rows = int(input())
columns = int(input())

chairs = rows * columns

price = 0

if type_cinema == "Premiere":
    price = 12.00 * chairs

elif type_cinema == "Normal":
    price = 7.50 * chairs

else:
    price = 5.00 * chairs

print(f"{price:.2f} leva")
