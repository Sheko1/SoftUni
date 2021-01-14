text = input()

s = []
mapper = {'}': '{', ']': '[', ')': '('}

for ch in text:
    if ch in "{[(":
        s.append(ch)

    elif s:
        if mapper[ch] == s[-1]:
            s.pop()

        else:
            break

    else:
        s.append(ch)
        break
if s:
    print("NO")

else:
    print("YES")