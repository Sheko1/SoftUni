from math import ceil


class PhotoAlbum:
    def __init__(self, pages: int):
        self.pages = pages
        self.photos = [[] for _ in range(pages)]
        self.pages_count = 0
        self.slot_count = 0

    @staticmethod
    def free_space(pages_count, slot_count, pages):
        return pages_count < pages and slot_count <= 4

    @classmethod
    def from_photos_count(cls, photos_count):
        return cls(ceil(photos_count / 4))

    def add_photo(self, label: str):
        self.slot_count += 1
        if self.slot_count > 4:
            self.pages_count += 1
            self.slot_count = 1

        if not self.free_space(self.pages_count, self.slot_count, self.pages):
            return "No more free spots"

        self.photos[self.pages_count].append(label)
        return f"{label} photo added successfully on page {self.pages_count + 1} slot {self.slot_count}"

    def display(self):
        result = ""
        for photo in self.photos:
            result += "-" * 11 + "\n"
            if photo:
                result += f"{'[] ' * len(photo)}".strip()
                result += "\n"
                continue
            result += "\n"

        result += "-" * 11 + "\n"

        return result


album = PhotoAlbum(2)

print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))

print(album.display())
