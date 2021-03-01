class User:
    def __init__(self, user_id: int, username):
        self.username = username
        self.user_id = user_id
        self.books = []

    def get_book(self, author: str, book_name: str, days_to_return: int, library):
        left_days = library.get_left_rented_days_by_book_name(book_name)

        if left_days:
            return f'The book "{book_name}" is already rented and will be available in {left_days} days!'

        if book_name not in library.books_available.get(author):
            return

        if self.username not in library.rented_books:
            library.rented_books[self.username] = {}

        self.books.append(book_name)
        library.rented_books[self.username][book_name] = days_to_return
        library.books_available[author].remove(book_name)

        return f"{book_name} successfully rented for the next {days_to_return} days!"

    def return_book(self, author: str, book_name: str, library):
        if book_name not in self.books:
            return f"{self.username} doesn't have this book in his/her records!"

        library.rented_books[self.username].pop(book_name)
        self.books.remove(book_name)
        library.books_available[author].append(book_name)

    def info(self):
        return ", ".join(sorted(self.books))

    def __str__(self):
        return f"{self.user_id}, {self.username}, {self.books}"
