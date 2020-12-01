n1 = int(input())
n2 = int(input())
result = ""
for i in range(n1, n2+1):
    result += chr(i)
    result += " "
print(result)
