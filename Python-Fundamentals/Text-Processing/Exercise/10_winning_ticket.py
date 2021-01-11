tickets = [el.strip() for el in input().split(", ")]

for ticket in tickets:
    if len(ticket) == 20:
        first_half = ticket[:10]
        second_half = ticket[10:]

        count_1 = 0
        count_2 = 0
        winning_symbol_1 = ""
        winning_symbol_2 = ""

        for char in first_half:
            if char == "#" or char == "@" or char == "$" or char == "^":
                if winning_symbol_1 != char:
                    if count_1 >= 6:
                        break

                    else:
                        count_1 = 0

                count_1 += 1
                winning_symbol_1 = char

            elif count_1 >= 6:
                break

            else:
                winning_symbol_1 = ""
                count_1 = 0

        for char in second_half:
            if char == "#" or char == "@" or char == "$" or char == "^":
                if winning_symbol_2 != char:
                    if count_2 >= 6:
                        break

                    else:
                        count_2 = 0

                count_2 += 1
                winning_symbol_2 = char

            elif count_2 >= 6:
                break

            else:
                winning_symbol_2 = ""
                count_2 = 0

        if winning_symbol_1 == winning_symbol_2 and count_1 >= 6 and count_2 >= 6:
            if count_1 > count_2:
                count_1 = count_2

            if count_1 < 10:
                print(f'ticket "{ticket}" - {count_1}{winning_symbol_1}')

            else:
                print(f'ticket "{ticket}" - {count_1}{winning_symbol_1} Jackpot!')

        else:
            print(f'ticket "{ticket}" - no match')

    else:
        print("invalid ticket")
