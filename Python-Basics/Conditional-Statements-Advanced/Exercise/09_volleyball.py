from math import floor
year = input()
p = int(input())
h = int(input())

weeks = 48 - h
games = 0

if year == "leap":
    games = h
    games = games + (weeks * 3/4)
    games = games + (p * 2/3)
    games = games + (games * 0.15)

else:
    games = h
    games = games + (weeks * 3/4)
    games = games + (p * 2/3)

print(floor(games))
