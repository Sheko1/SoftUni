def print_result(elements):
    for key, value in elements:
        print(f"{key}: {value} time/s")


text = input()
ch_counter = {}

for ch in text:
    if ch not in ch_counter:
        ch_counter[ch] = 0

    ch_counter[ch] += 1

ch_counter = sorted(ch_counter.items(), key=lambda x: x)
print_result(ch_counter)