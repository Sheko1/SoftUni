berries = float(input())
banana_kilo = float(input())
orange_kilo = float(input())
raspberries_kilo = float(input())
berries_kilo = float(input())
raspberries_per_kilo = berries - berries * 0.5
orange_per_kilo = raspberries_per_kilo - raspberries_per_kilo * 0.4
banana_per_kilo = raspberries_per_kilo - raspberries_per_kilo * 0.8
sum_raspberries = raspberries_kilo * raspberries_per_kilo
sum_orange = orange_kilo * orange_per_kilo
sum_banana = banana_kilo * banana_per_kilo
sum_berries = berries_kilo * berries
result = sum_raspberries + sum_orange + sum_banana + sum_berries
print(result)