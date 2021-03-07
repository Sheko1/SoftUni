from .player import Player


class Team:
    def __init__(self, name: str, rating: int):
        self.__name = name
        self.__rating = rating
        self.__players = []

    @staticmethod
    def __get_player_by_name(players_list, player_name):
        result = [player for player in players_list if player.name == player_name]
        return result

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def rating(self):
        return self.__rating

    @rating.setter
    def rating(self, value):
        self.__rating = value

    @property
    def players(self):
        return self.__players

    @players.setter
    def players(self, value):
        self.__players = value

    def add_player(self, player: Player):
        if player in self.__players:
            return f"Player {player.name} has already joined"

        self.__players.append(player)
        return f"Player {player.name} joined team {self.name}"

    def remove_player(self, player_name: str):
        player = self.__get_player_by_name(self.__players, player_name)

        if not player:
            return f"Player {player_name} not found"

        self.__players.remove(player[0])
        return player[0]
