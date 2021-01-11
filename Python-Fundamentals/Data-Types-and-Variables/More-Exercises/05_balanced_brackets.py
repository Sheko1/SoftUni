n = int(input())
last_line = ")"
balanced = True
for _ in range(n):
    line = input()

    if line == "(" or line == ")":
        if line != last_line:
            last_line = line

        else:
            balanced = False

if balanced:
    print("BALANCED")

else:
    print("UNBALANCED")