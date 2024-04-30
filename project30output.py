class Pokemon:
    def __init__(self, name, level):
        self.name = name
        self.level = level
        self.health = level * 10

    def __str__(self):
        return f"{self.name} (Level {self.level})"
    
def battle(player_pokemon, enemy_pokemon):
    while player_pokemon.health > 0 and enemy_pokemon.health > 0:
        print(f"{player_pokemon} - Health: {player_pokemon.health}")
        print(f"{enemy_pokemon} - Health: {enemy_pokemon.health}\n")
        player_move = input("Please choose your move(1: Attack, 2: Heal): ")
        if player_move == "1":
            enemy_pokemon.health -= player_pokemon.level
        elif player_move == "2":
            player_pokemon.health += player_pokemon.level
        else:
            print("That's a bad move! Please enter '1' or 2'.")
        if enemy_pokemon.health <= 0:
            print(f"{enemy_pokemon} fainted!")
            break
        enemy_move = input("Please choose your opponent's move (1: Attack, 2: Heal): ")
        if enemy_move == "1":
            player_pokemon.health -= enemy_pokemon.level
        elif enemy_move == "2":
            enemy_pokemon.health += enemy_pokemon.level
        else:
            print("That's a bad move. Please enter '1' or '2'.")
        if player_pokemon.health <= 0:
            print(f"{player_pokemon} fainted.")
            break

def main():
    print("Let's play the PokeMon Training Game!")
    player_pokemon = Pokemon("Geodude", 5)
    enemy_pokemon = Pokemon("Wartortle", 10)
    print(f"You have {player_pokemon} to battle against {enemy_pokemon}. \n")
    battle(player_pokemon, enemy_pokemon)

if  __name__ == "__main__":
    main()
