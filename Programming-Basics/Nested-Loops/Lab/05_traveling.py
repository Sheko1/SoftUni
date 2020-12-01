destination = input()

need_money = 0

while destination != "End":
    budget = float(input())

    while need_money < budget:
        money = float(input())
        need_money += money

    if need_money >= budget:
        need_money = 0
        print(f'Going to {destination}!')

    destination = input()
