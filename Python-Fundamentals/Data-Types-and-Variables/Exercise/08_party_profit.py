party_size = int(input())
days = int(input())

coins = 0

for i in range(1, days+1):
    if i % 10 == 0:
        party_size -= 2

    if i % 15 == 0:
        party_size += 5

    coins += 50
    coins -= party_size * 2

    if i % 3 == 0:
        coins -= party_size * 3

    if i % 5 == 0:
        coins += party_size * 20
        if i % 3 == 0:
            coins -= party_size * 2

print(f"{party_size} companions received {int(coins / party_size)} coins each.")
