class Library:
    def __init__(self):
        self.user_records = []
        self.books_available = {}
        self.rented_books = {}

    def get_left_rented_days_by_book_name(self, book_name):
        for username, books in self.rented_books.items():
            if book_name in books:
                return books[book_name]

    def add_user(self, user):
        if user in self.user_records:
            return f"User with id = {user.user_id} already registered in the library!"

        self.user_records.append(user)

    def remove_user(self, user):
        if user not in self.user_records:
            return "We could not find such user to remove!"

        if self.rented_books.get(user.username):
            self.rented_books.pop(user.username)

        self.user_records.remove(user)

    def change_username(self, user_id: int, new_username: str):
        users = [user for user in self.user_records if user.user_id == user_id]

        if not users:
            return f"There is no user with id = {user_id}!"

        if users[0].username == new_username:
            return "Please check again the provided username - it should be different than the" \
                   " username used so far!"

        for user in users:
            if user.username != new_username:
                if user.username in self.rented_books:
                    books = self.rented_books[user.username]
                    self.rented_books.pop(user.username)
                    self.rented_books[new_username] = books

                user.username = new_username

        return f"Username successfully changed to: {new_username} for userid: {user_id}"
