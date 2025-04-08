import json
from app import db
from app.models.pokemon import Pokemon

def load_pokemon_data():
    try:
        with open('pokemon_data.json', 'r') as f:
            pokemon_data = json.load(f)

        # Clear existing collection
        db.pokemon.drop()

        # Insert new data
        for data in pokemon_data:
            pokemon = Pokemon(
                name=data['name'],
                types=data['types'],
                hp=data['hp'],
                attack=data['attack'],
                defense=data['defense'],
                sp_attack=data['sp_attack'],
                sp_defense=data['sp_defense'],
                speed=data['speed'],
                moves=data['moves'],
                image_url=data['image_url'],
                pokedex_id=data['pokedex_id']
            )
            pokemon.save()

        print(f"Data loaded successfully: {len(pokemon_data)} Pokémon")
    except Exception as e:
        print(f"Error loading data: {e}")

if __name__ == "__main__":
    load_pokemon_data()
