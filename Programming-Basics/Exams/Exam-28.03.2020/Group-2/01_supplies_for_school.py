pen = int(input())
marker = int(input())
preparat = float(input())
discount = int(input())

pen_price = 5.80 * pen
marker_price = 7.20 * marker
preparat_price = 1.20 * preparat

total = pen_price + marker_price + preparat_price
total -= total * (discount / 100)

print(f"{total:.3f}")
