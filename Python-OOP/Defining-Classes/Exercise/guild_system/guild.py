from guild_system.player import Player


class Guild:
    def __init__(self, name: str):
        self.name = name
        self.players = []

    def __find_player(self, name: str):
        for player in self.players:
            if player.name == name:
                return player

    def assign_player(self, player: Player):
        if player.guild == self.name:
            return f"Player {player.name} is already in the guild."

        elif player.guild == "Unaffiliated":
            self.players.append(player)
            player.guild = self.name
            return f"Welcome player {player.name} to the guild {self.name}"

        else:
            return f"Player {player.name} is in another guild."

    def kick_player(self, player_name: str):
        player_to_remove = self.__find_player(player_name)

        if player_to_remove:
            self.players.remove(player_to_remove)
            return f"Player {player_name} has been removed from the guild."

        return f"Player {player_name} is not in the guild."

    def guild_info(self):
        result = f"Guild: {self.name}\n"

        for player in self.players:
            result += player.player_info()

        return result
