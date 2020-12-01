def loading_bar(n):
    data = ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', ]
    index = 0
    for i in range(1, n + 1):
        if i % 10 == 0:
            data[index] = "%"
            index += 1

    loading = "".join(data)
    if n == 100:
        print(f"{n}% Complete!")
        print(f"[{loading}]")
    else:
        print(f"{n}% [{loading}]")
        print("Still loading...")


number = int(input())
loading_bar(number)