from pokemon_battle.pokemon import Pokemon


class Trainer:
    def __init__(self, name: str):
        self.name = name
        self.pokemon = []
        self.pokemon_to_remove = None

    def add_pokemon(self, pokemon: Pokemon):
        if pokemon not in self.pokemon:
            self.pokemon.append(pokemon)
            return f"Caught {pokemon.pokemon_details()}"

        return "This pokemon is already caught"

    def find_pokemon(self, name: str):
        for pokemon in self.pokemon:
            if pokemon.name == name:
                self.pokemon_to_remove = pokemon
                return True

    def release_pokemon(self, pokemon_name: str):
        if self.find_pokemon(pokemon_name):
            self.pokemon.remove(self.pokemon_to_remove)
            return f"You have released {pokemon_name}"

        return "Pokemon is not caught"

    def trainer_data(self):
        data = f"Pokemon Trainer {self.name}\nPokemon count {len(self.pokemon)}"
        for pokemon in self.pokemon:
            data += f"\n- {pokemon.pokemon_details()}\n"

        return data
