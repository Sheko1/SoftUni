from spoopify.album import Album


class Band:
    def __init__(self, name: str):
        self.name = name
        self.albums = []

    def __find_album(self, name: str):
        for album in self.albums:
            if album.name == name:
                return album

    def add_album(self, album: Album):
        if album in self.albums:
            return f"Band {self.name} already has {album.name} in their library."

        self.albums.append(album)
        return f"Band {self.name} has added their newest album {album.name}."

    def remove_album(self, album_name: str):
        album_to_remove = self.__find_album(album_name)

        if not album_to_remove:
            return f"Album {album_name} is not found."

        if album_to_remove.published:
            return "Album has been published. It cannot be removed."

        self.albums.remove(album_to_remove)
        return f"Album {album_name} has been removed."

    def details(self):
        result = f"Band {self.name}\n"
        for album in self.albums:
            result += album.details()

        return result
