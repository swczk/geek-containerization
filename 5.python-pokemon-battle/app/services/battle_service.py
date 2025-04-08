from app.models.battle import Battle
from app.services.pokemon_service import calculate_damage
import random

def simulate_battle(pokemon1, pokemon2):
    # Copies of original stats to avoid modifying objects
    p1 = {
        'name': pokemon1['name'],
        'types': pokemon1['types'],
        'hp': pokemon1['hp'],
        'max_hp': pokemon1['hp'],
        'attack': pokemon1['attack'],
        'defense': pokemon1['defense'],
        'sp_attack': pokemon1['sp_attack'],
        'sp_defense': pokemon1['sp_defense'],
        'speed': pokemon1['speed'],
        'moves': pokemon1['moves'],
        'image_url': pokemon1['image_url'],
        'pokedex_id': pokemon1['pokedex_id']
    }

    p2 = {
        'name': pokemon2['name'],
        'types': pokemon2['types'],
        'hp': pokemon2['hp'],
        'max_hp': pokemon2['hp'],
        'attack': pokemon2['attack'],
        'defense': pokemon2['defense'],
        'sp_attack': pokemon2['sp_attack'],
        'sp_defense': pokemon2['sp_defense'],
        'speed': pokemon2['speed'],
        'moves': pokemon2['moves'],
        'image_url': pokemon2['image_url'],
        'pokedex_id': pokemon2['pokedex_id']
    }

    battle_log = []
    current_turn = 1

    # Determine who attacks first based on speed
    if p1['speed'] > p2['speed']:
        first = p1
        second = p2
    elif p2['speed'] > p1['speed']:
        first = p2
        second = p1
    else:
        # If speed is equal, choose randomly
        if random.choice([True, False]):
            first = p1
            second = p2
        else:
            first = p2
            second = p1

    battle_log.append(f"Battle between {p1['name']} and {p2['name']} begins!")

    # Battle continues until one Pokémon runs out of HP
    while p1['hp'] > 0 and p2['hp'] > 0 and current_turn <= 20:  # Limit of 20 turns
        battle_log.append(f"\nTurn {current_turn}")

        # First Pokémon attacks
        battle_log.extend(execute_turn(first, second))

        # Check if second Pokémon is still standing
        if second['hp'] <= 0:
            battle_log.append(f"{second['name']} fainted!")
            break

        # Second Pokémon attacks
        battle_log.extend(execute_turn(second, first))

        # Check if first Pokémon is still standing
        if first['hp'] <= 0:
            battle_log.append(f"{first['name']} fainted!")
            break

        current_turn += 1

    # Determine winner
    if p1['hp'] <= 0:
        winner = p2
        battle_log.append(f"\n{p2['name']} won the battle!")
    elif p2['hp'] <= 0:
        winner = p1
        battle_log.append(f"\n{p1['name']} won the battle!")
    else:
        # Tie - Pokémon with higher % HP remaining wins
        p1_hp_percent = p1['hp'] / p1['max_hp']
        p2_hp_percent = p2['hp'] / p2['max_hp']

        if p1_hp_percent > p2_hp_percent:
            winner = p1
            battle_log.append(f"\nTime's up! {p1['name']} won the battle with {p1['hp']} HP remaining ({int(p1_hp_percent * 100)}%)!")
        else:
            winner = p2
            battle_log.append(f"\nTime's up! {p2['name']} won the battle with {p2['hp']} HP remaining ({int(p2_hp_percent * 100)}%)!")

    # Save battle result to database
    battle = Battle(
        pokemon1=p1,
        pokemon2=p2,
        winner=winner,
        battle_log=battle_log
    )
    battle.save()

    # Return battle info
    return {
        'pokemon1': p1,
        'pokemon2': p2,
        'winner': winner,
        'battle_log': battle_log
    }

def execute_turn(attacker, defender):
    log = []

    # Select random move
    move = random.choice(attacker['moves'])

    log.append(f"{attacker['name']} used {move['name']}!")

    # Calculate damage
    result = calculate_damage(attacker, defender, move)
    damage = result['damage']

    # Apply damage
    defender['hp'] = max(0, defender['hp'] - damage)

    # Record attack result
    if result['effectiveness'] > 1:
        log.append("It's super effective!")
    elif result['effectiveness'] < 1 and result['effectiveness'] > 0:
        log.append("It's not very effective...")
    elif result['effectiveness'] == 0:
        log.append("It doesn't affect the opposing Pokémon...")

    if result['is_critical']:
        log.append("Critical hit!")

    log.append(f"{defender['name']} lost {damage} HP! ({defender['hp']}/{defender['max_hp']} HP remaining)")

    return log

def get_recent_battles(limit=10):
    return Battle.find_all(limit)

def get_battle_by_id(id):
    return Battle.find_by_id(id)

def get_battles_by_pokemon(pokemon_name):
    return Battle.find_by_pokemon(pokemon_name)
