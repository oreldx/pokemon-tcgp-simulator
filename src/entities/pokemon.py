from .card import Card
from .attack import Attack
from ..utils import PokemonType, PokemonStatus


class Pokemon(Card):
    def __init__(
        self,
        card_id: str,
        name: str,
        pokemon_type: PokemonType,
        hp: int,
        attacks: list[Attack],
        retreat_cost: int,
        weakness: dict[PokemonType, int],
    ):
        super().__init__(card_id, name)
        self.id = card_id
        self.name = name
        self.type = pokemon_type
        self.attacks = attacks
        self.retreat_cost = retreat_cost
        self.weakness = weakness

        self.hp = hp
        self.status = PokemonStatus.NORMAL
        self.energy_attached = 0

    def __str__(self):
        return f"{self.name} ({self.hp} HP)"
