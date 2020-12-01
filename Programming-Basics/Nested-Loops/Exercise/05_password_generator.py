n = int(input())
l = int(input())

for s1 in range(1, n+1):
    for s2 in range(1, n+1):
        for s3 in range(97, 97+l):
            for s4 in range(97, 97+l):
                for s5 in range(1, n+1):
                    if s5 > s1 and s5 > s2:
                        print(f"{s1}{s2}{chr(s3)}{chr(s4)}{s5}", end=" ")
