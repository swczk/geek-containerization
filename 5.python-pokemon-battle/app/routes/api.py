from flask import Blueprint, jsonify, request, render_template
from app.services.pokemon_service import get_all_pokemon, get_pokemon_by_name, get_random_pokemon
from app.services.battle_service import simulate_battle, get_recent_battles, get_battle_by_id

bp = Blueprint('api', __name__)

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/api/pokemon', methods=['GET'])
def get_pokemon():
    pokemon = get_all_pokemon()
    return jsonify([{**p, '_id': str(p['_id'])} for p in pokemon])

@bp.route('/api/pokemon/<name>', methods=['GET'])
def get_pokemon_details(name):
    pokemon = get_pokemon_by_name(name)
    if pokemon:
        pokemon['_id'] = str(pokemon['_id'])
        return jsonify(pokemon)
    return jsonify({'error': 'Pokémon not found'}), 404

@bp.route('/api/battle/random', methods=['GET'])
def random_battle():
    pokemon1 = get_random_pokemon()
    pokemon2 = get_random_pokemon()

    # Ensure different Pokémon
    while pokemon1['_id'] == pokemon2['_id']:
        pokemon2 = get_random_pokemon()

    pokemon1['_id'] = str(pokemon1['_id'])
    pokemon2['_id'] = str(pokemon2['_id'])

    battle_result = simulate_battle(pokemon1, pokemon2)
    return jsonify(battle_result)

@bp.route('/api/battle', methods=['POST'])
def custom_battle():
    data = request.json

    if not data or 'pokemon1' not in data or 'pokemon2' not in data:
        return jsonify({'error': 'Select two Pokémon for battle'}), 400

    pokemon1 = get_pokemon_by_name(data['pokemon1'])
    pokemon2 = get_pokemon_by_name(data['pokemon2'])

    if not pokemon1 or not pokemon2:
        return jsonify({'error': 'One or both Pokémon not found'}), 404

    pokemon1['_id'] = str(pokemon1['_id'])
    pokemon2['_id'] = str(pokemon2['_id'])

    battle_result = simulate_battle(pokemon1, pokemon2)
    return jsonify(battle_result)

@bp.route('/api/battles/recent', methods=['GET'])
def recent_battles():
    battles = get_recent_battles()
    return jsonify([{
        '_id': str(battle['_id']),
        'pokemon1': battle['pokemon1']['name'],
        'pokemon2': battle['pokemon2']['name'],
        'winner': battle['winner']['name'],
        'date': battle['battle_date'].isoformat()
    } for battle in battles])

@bp.route('/api/battle/<id>', methods=['GET'])
def battle_details(id):
    battle = get_battle_by_id(id)
    if battle:
        battle['_id'] = str(battle['_id'])
        return jsonify(battle)
    return jsonify({'error': 'Battle not found'}), 404

@bp.route('/battle')
def battle_page():
    return render_template('battle.html')

@bp.route('/results')
def results_page():
    return render_template('results.html')
