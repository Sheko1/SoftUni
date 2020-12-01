book_name = input()
is_book_found = False
book = input()
count = 0

while book != "No More Books":
    if book == book_name:
        is_book_found = True
        print(f"You checked {count} books and found it.")
        break
    count += 1
    book = input()

if not is_book_found:
    print("The book you search is not here!")
    print(f"You checked {count} books.")
