queue = input().split(", ")
queue.reverse()
if queue[0] == "wolf":
    print("Please go away and stop eating my sheep")

else:
    index = queue.index("wolf")
    metin = queue[:index]
    print(f"Oi! Sheep number {len(metin)}! You are about to be eaten by a wolf!")
