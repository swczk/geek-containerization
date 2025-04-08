from app.models.pokemon import Pokemon
import random

def get_all_pokemon():
    return Pokemon.find_all()

def get_pokemon_by_id(id):
    return Pokemon.find_by_id(id)

def get_pokemon_by_name(name):
    return Pokemon.find_by_name(name)

def get_pokemon_by_type(pokemon_type):
    return Pokemon.find_by_type(pokemon_type)

def get_random_pokemon():
    all_pokemon = Pokemon.find_all()
    return random.choice(all_pokemon)

def calculate_damage(attacker, defender, move):
    # Type effectiveness (simplified)
    type_effectiveness = get_type_effectiveness(move['type'], defender['types'])

    # Select stats based on move category
    if move['category'] == 'Physical':
        attack_stat = attacker['attack']
        defense_stat = defender['defense']
    else:  # Special
        attack_stat = attacker['sp_attack']
        defense_stat = defender['sp_defense']

    # Basic damage calculation
    power = move['power']
    level = 50  # Assuming level 50 for all Pokémon

    # Damage formula based on original game
    damage = ((2 * level / 5 + 2) * power * attack_stat / defense_stat) / 50 + 2

    # Apply modifiers
    damage *= type_effectiveness

    # Random variation (between 85% and 100% of calculated damage)
    damage *= random.uniform(0.85, 1.0)

    # Critical hit chance (6.25%)
    if random.random() < 0.0625:
        damage *= 1.5
        is_critical = True
    else:
        is_critical = False

    return {
        'damage': int(damage),
        'effectiveness': type_effectiveness,
        'is_critical': is_critical
    }

def get_type_effectiveness(move_type, defender_types):
    # Simplified type effectiveness chart
    type_chart = {
        'Normal': {'Rock': 0.5, 'Ghost': 0, 'Steel': 0.5},
        'Fire': {'Fire': 0.5, 'Water': 0.5, 'Grass': 2, 'Ice': 2, 'Bug': 2, 'Rock': 0.5, 'Dragon': 0.5, 'Steel': 2},
        'Water': {'Fire': 2, 'Water': 0.5, 'Grass': 0.5, 'Ground': 2, 'Rock': 2, 'Dragon': 0.5},
        'Electric': {'Water': 2, 'Electric': 0.5, 'Grass': 0.5, 'Ground': 0, 'Flying': 2, 'Dragon': 0.5},
        'Grass': {'Fire': 0.5, 'Water': 2, 'Grass': 0.5, 'Poison': 0.5, 'Ground': 2, 'Flying': 0.5, 'Bug': 0.5, 'Rock': 2, 'Dragon': 0.5, 'Steel': 0.5},
        'Ice': {'Fire': 0.5, 'Water': 0.5, 'Grass': 2, 'Ice': 0.5, 'Ground': 2, 'Flying': 2, 'Dragon': 2, 'Steel': 0.5},
        'Fighting': {'Normal': 2, 'Ice': 2, 'Poison': 0.5, 'Flying': 0.5, 'Psychic': 0.5, 'Bug': 0.5, 'Rock': 2, 'Ghost': 0, 'Dark': 2, 'Steel': 2, 'Fairy': 0.5},
        'Poison': {'Grass': 2, 'Poison': 0.5, 'Ground': 0.5, 'Rock': 0.5, 'Ghost': 0.5, 'Steel': 0, 'Fairy': 2},
        'Ground': {'Fire': 2, 'Electric': 2, 'Grass': 0.5, 'Poison': 2, 'Flying': 0, 'Bug': 0.5, 'Rock': 2, 'Steel': 2},
        'Flying': {'Electric': 0.5, 'Grass': 2, 'Fighting': 2, 'Bug': 2, 'Rock': 0.5, 'Steel': 0.5},
        'Psychic': {'Fighting': 2, 'Poison': 2, 'Psychic': 0.5, 'Dark': 0, 'Steel': 0.5},
        'Bug': {'Fire': 0.5, 'Grass': 2, 'Fighting': 0.5, 'Poison': 0.5, 'Flying': 0.5, 'Psychic': 2, 'Ghost': 0.5, 'Dark': 2, 'Steel': 0.5, 'Fairy': 0.5},
        'Rock': {'Fire': 2, 'Ice': 2, 'Fighting': 0.5, 'Ground': 0.5, 'Flying': 2, 'Bug': 2, 'Steel': 0.5},
        'Ghost': {'Normal': 0, 'Psychic': 2, 'Ghost': 2, 'Dark': 0.5},
        'Dragon': {'Dragon': 2, 'Steel': 0.5, 'Fairy': 0},
        'Dark': {'Fighting': 0.5, 'Psychic': 2, 'Ghost': 2, 'Dark': 0.5, 'Fairy': 0.5},
        'Steel': {'Fire': 0.5, 'Water': 0.5, 'Electric': 0.5, 'Ice': 2, 'Rock': 2, 'Steel': 0.5, 'Fairy': 2},
        'Fairy': {'Fire': 0.5, 'Fighting': 2, 'Poison': 0.5, 'Dragon': 2, 'Dark': 2, 'Steel': 0.5}
    }

    effectiveness = 1.0

    # Apply effectiveness for each defender type
    for defender_type in defender_types:
        if move_type in type_chart and defender_type in type_chart[move_type]:
            effectiveness *= type_chart[move_type][defender_type]

    return effectiveness
