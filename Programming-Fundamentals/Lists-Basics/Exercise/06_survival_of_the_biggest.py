numbers = input()
n = int(input())

data = numbers.split(" ")
nums = [0] * len(data)

for i in range(len(data)):
    nums[i] += int(data[i])
    data[i] = int(data[i])

nums.sort()
for j in range(n):
    last_number = nums.pop(0)
    data.remove(last_number)

print(data)
