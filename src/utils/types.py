from enum import Enum


class AttackType(Enum):
    NORMAL = "C"
    FIRE = "R"
    WATER = "W"
    ELECTRIC = "L"
    GRASS = "G"
    FIGHTING = "F"
    DARK = "D"
    PSYCHIC = "P"


class PokemonType(Enum):
    NORMAL = "Normal"
    FIRE = "Fire"
    WATER = "Water"
    ELECTRIC = "Electric"
    GRASS = "Grass"
    FIGHTING = "Fighting"
    DARK = "Dark"
    PSYCHIC = "Psychic"
    DRAGON = "Dragon"
    FLIGHT = "Flight"


class PokemonStatus(Enum):
    NORMAL = "Normal"
    BURN = "Burn"
    POISON = "Poison"
    PARALYSIS = "Paralysis"
    SLEEP = "Sleep"
    FREEZE = "Freeze"
