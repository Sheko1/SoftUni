n = int(input())

number = 1
flag = False
for i in range(1, n+1):
    for j in range(1, i+1):
        if number > n:
            flag = True
            break
        print(str(number) + " ", end="")
        number +=1
    if flag:
        break
    print()
