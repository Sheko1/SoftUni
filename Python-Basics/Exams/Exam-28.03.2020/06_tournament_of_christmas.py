day = int(input())

total_money = 0
win1 = 0
lose1 = 0
count = 0
for i in range(day):
    sport = input()
    win = 0
    lose = 0
    money = 0
    while sport != "Finish":
        result = input()
        if result == "win":
            win += 1
            win1 += 1
            money += 20

        else:
            lose1 += 1
            lose += 1
        sport = input()

    total_money += money
    if win > lose:
        total_money += money * 0.1


if win1 > lose1:
    total_money += total_money * 0.2
    print(f"You won the tournament! Total raised money: {total_money:.2f}")

else:
    print(f"You lost the tournament! Total raised money: {total_money:.2f}")
