city = input()
sales_volume = float(input())

commissions = 0

if city == "Sofia":
    if 0 <= sales_volume <= 500:
        commissions = sales_volume * 0.05

    elif 500 < sales_volume <= 1000:
        commissions = sales_volume * 0.07

    elif 1000 < sales_volume <= 10000:
        commissions = sales_volume * 0.08

    elif sales_volume > 10000:
        commissions = sales_volume * 0.12

if city == "Varna":
    if 0 <= sales_volume <= 500:
        commissions = sales_volume * 0.045

    elif 500 < sales_volume <= 1000:
        commissions = sales_volume * 0.075

    elif 1000 < sales_volume <= 10000:
        commissions = sales_volume * 0.1

    elif sales_volume > 10000:
        commissions = sales_volume * 0.13

if city == "Plovdiv":
    if 0 <= sales_volume <= 500:
        commissions = sales_volume * 0.055

    elif 500 < sales_volume <= 1000:
        commissions = sales_volume * 0.08

    elif 1000 < sales_volume <= 10000:
        commissions = sales_volume * 0.12

    elif sales_volume > 10000:
        commissions = sales_volume * 0.145

if commissions == 0:
    print("error")

else:
    print(f"{commissions:.2f}")
