numbers = [int(i) for i in input().split(", ")]
i = 1
while len(numbers) > 0:
    rahim = list(filter(lambda x: x <= i*10, numbers))
    print(f"Group of {i * 10}'s: {rahim}")

    for j in rahim:
        numbers.remove(j)

    i += 1