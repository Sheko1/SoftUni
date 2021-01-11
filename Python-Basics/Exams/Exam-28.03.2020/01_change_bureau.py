bitcoin = int(input())
chinese_money = float(input())
commission = float(input())

bitcoin_euro = (1168 / 1.95) * bitcoin
chinese_money_euro = ((0.15 * 1.76) / 1.95) * chinese_money
total = (bitcoin_euro + chinese_money_euro)
total -= total * (commission / 100)
print(f"{total:.2f}")
