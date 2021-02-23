from spoopify.song import Song


class Album:
    def __init__(self, name: str, *args):
        self.name = name
        self.songs = list(args)
        self.published = False

    def __find_song(self, name):
        for song in self.songs:
            if name == song.name:
                return song

    def add_song(self, song: Song):
        if song.single:
            return f"Cannot add {song.name}. It's a single"

        elif self.published:
            return "Cannot add songs. Album is published."

        elif song in self.songs:
            return "Song is already in the album."

        self.songs.append(song)
        return f"Song {song.name} has been added to the album {self.name}."

    def remove_song(self, song_name: str):
        if self.published:
            return "Cannot remove songs. Album is published."

        song_to_remove = self.__find_song(song_name)

        if not song_to_remove:
            return "Song is not in the album."

        self.songs.remove(song_to_remove)
        return f"Removed song {song_name} from album {self.name}."

    def publish(self):
        if not self.published:
            self.published = True
            return f"Album {self.name} has been published."

        return f"Album {self.name} is already published."

    def details(self):
        result = f"Album {self.name}\n"
        for song in self.songs:
            result += f"== {song.get_info()}\n"

        return result
