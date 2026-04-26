from typing import List

class TypeRelations:
    def __init__(self) -> None:
        self.type_chart: dict[str, dict[str, float]] = {
            "Fire": {
                "Fire": 0.5,
                "Water": 0.5,
                "Grass": 2.0,
                "Electric": 1.0,
                "Ground": 1.0
            },
            "Water": {
                "Fire": 2.0,
                "Water": 0.5,
                "Grass": 0.5,
                "Electric": 1.0,
                "Ground": 2.0
            },
            "Grass": {
                "Fire": 0.5,
                "Water": 2.0,
                "Grass": 0.5,
                "Electric": 1.0,
                "Ground": 2.0
            },
            "Electric": {
                "Fire": 1.0,
                "Water": 2.0,
                "Grass": 0.5,
                "Electric": 0.5,
                "Ground": 0.0 
            },
            "Ground": {
                "Fire": 2.0,
                "Water": 1.0,
                "Grass": 0.5,
                "Electric": 2.0,
                "Ground": 1.0
            }
        }

    def get_effectiveness(self, attack_type: str, defender_types: List[str]) -> float:
        multiplier: float = 1.0

        for defender in defender_types:
            if attack_type in self.type_chart:
                if defender in self.type_chart[attack_type]:
                    multiplier = multiplier * self.type_chart[attack_type][defender]
                else:
                    multiplier = multiplier * 1.0
            else:
                multiplier = multiplier * 1.0

        return multiplier


class Pokemon:
    def __init__(
        self,
        name: str,
        types: List[str],
        life: float = 10,
        attack: float = 1,
        defense: float = 0.5,
        level: int = 1,
        special_ability: str = "None"
    ) -> None:

        self.name = name
        self.types = types
        self.life = life
        self.attack_power = attack
        self.defense = defense
        self.level = level
        self.special_ability = special_ability

    def attack(self, target: "Pokemon", base_power: float, relations: TypeRelations) -> None:
        attack_type = self.types[0]

        multiplier = relations.get_effectiveness(attack_type, target.types)

        damage = base_power * self.attack_power * multiplier

        print(f"{self.name} attacks {target.name}")
        print(f"Effectiveness: x{multiplier}")

        target.defender(damage)

    def defender(self, damage: float) -> None:
        damage_received = damage * (1 - self.defense)

        self.life = self.life - damage_received

        if self.life < 0:
            self.life = 0

        print(f"{self.name} received {damage_received:.2f} damage")
        print(f"Remaining life: {self.life:.2f}")

    def evolve(self, new_level: int, new_ability: str) -> None:
        if new_level > self.level:
            self.level = new_level
            self.special_ability = new_ability
            print(f"{self.name} evolved to level {self.level}")
        else:
            print("Cannot evolve to same or lower level")


def main() -> None:
    relations = TypeRelations()

    charmander = Pokemon("Charmander", ["Fire"], life=20, attack=2)
    bulbasaur = Pokemon("Bulbasaur", ["Grass"], life=20, defense=0.3)
    squirtle = Pokemon("Squirtle", ["Water"], life=20)

    print("\n--- BATTLE 1 ---")
    charmander.attack(bulbasaur, base_power=5, relations=relations)

    print("\n--- BATTLE 2 ---")
    bulbasaur.attack(squirtle, base_power=5, relations=relations)

    print("\n--- BATTLE 3 ---")
    squirtle.attack(charmander, base_power=5, relations=relations)


if __name__ == "__main__":
    main()