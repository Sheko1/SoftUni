length = int(input())
width = int(input())
height = int(input())
percentage_volume = float(input())
volume = length * width * height
total_liters = volume * 0.001
percent = percentage_volume * 0.01
result = total_liters * (1 - percent)
print(result)