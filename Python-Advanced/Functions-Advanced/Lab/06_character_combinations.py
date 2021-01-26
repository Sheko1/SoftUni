def permute(text, curr_index=0):
    if curr_index == len(text):
        print("".join(text))
        return

    for i in range(curr_index, len(text)):
        text[i], text[curr_index] = text[curr_index], text[i]
        permute(text, curr_index+1)
        text[i], text[curr_index] = text[curr_index], text[i]


permute(list(input()))
