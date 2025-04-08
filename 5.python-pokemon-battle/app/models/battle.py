from app import db
from datetime import datetime
from bson.objectid import ObjectId

class Battle:
    collection = db.battles

    def __init__(self, pokemon1, pokemon2, winner, battle_log):
        self.pokemon1 = pokemon1
        self.pokemon2 = pokemon2
        self.winner = winner
        self.battle_log = battle_log
        self.battle_date = datetime.utcnow()

    def save(self):
        result = self.collection.insert_one(self.to_dict())
        self._id = result.inserted_id
        return result

    def to_dict(self):
        return {
            'pokemon1': self.pokemon1,
            'pokemon2': self.pokemon2,
            'winner': self.winner,
            'battle_log': self.battle_log,
            'battle_date': self.battle_date
        }

    @classmethod
    def find_all(cls, limit=20):
        return list(cls.collection.find().sort('battle_date', -1).limit(limit))

    @classmethod
    def find_by_id(cls, id):
        return cls.collection.find_one({'_id': ObjectId(id)})

    @classmethod
    def find_by_pokemon(cls, pokemon_name):
        return list(cls.collection.find({
            '$or': [
                {'pokemon1.name': pokemon_name},
                {'pokemon2.name': pokemon_name}
            ]
        }).sort('battle_date', -1))
