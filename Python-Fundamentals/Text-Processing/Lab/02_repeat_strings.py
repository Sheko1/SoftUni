words = input().split()


def multiply(word, req_len, merfin):
    if len(word) == req_len:
        return word
    return multiply(word+merfin, req_len, merfin)


result = ""

for w in words:
    lenght_3 = len(w*len(w))
    result += multiply(w, lenght_3, w)

print(result)
