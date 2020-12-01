width = int(input())
length = int(input())
shebekerish = input()

cake = width * length
shebek = 0

while shebekerish != "STOP":
    shebek += int(shebekerish)

    if shebek > cake:
        break

    shebekerish = input()

if shebek > cake:
    print(f"No more cake left! You need {shebek - cake} pieces more.")

else:
    print(f"{cake - shebek} pieces are left.")
