from app import db
from bson.objectid import ObjectId

class Pokemon:
    collection = db.pokemon

    def __init__(self, name, types, hp, attack, defense, sp_attack, sp_defense, speed, moves, image_url, pokedex_id):
        self.name = name
        self.types = types
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.sp_attack = sp_attack
        self.sp_defense = sp_defense
        self.speed = speed
        self.moves = moves
        self.image_url = image_url
        self.pokedex_id = pokedex_id

    def save(self):
        if hasattr(self, '_id'):
            return self.collection.update_one(
                {'_id': self._id},
                {'$set': self.to_dict()}
            )
        else:
            result = self.collection.insert_one(self.to_dict())
            self._id = result.inserted_id
            return result

    def to_dict(self):
        return {
            'name': self.name,
            'types': self.types,
            'hp': self.hp,
            'attack': self.attack,
            'defense': self.defense,
            'sp_attack': self.sp_attack,
            'sp_defense': self.sp_defense,
            'speed': self.speed,
            'moves': self.moves,
            'image_url': self.image_url,
            'pokedex_id': self.pokedex_id
        }

    @classmethod
    def find_all(cls):
        return list(cls.collection.find())

    @classmethod
    def find_by_id(cls, id):
        return cls.collection.find_one({'_id': ObjectId(id)})

    @classmethod
    def find_by_name(cls, name):
        return cls.collection.find_one({'name': {'$regex': name, '$options': 'i'}})

    @classmethod
    def find_by_type(cls, pokemon_type):
        return list(cls.collection.find({'types': pokemon_type}))
