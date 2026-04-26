#clase stats con 6 estadisticas
class Stats:
    def __init__(
        self,
        hp: int,
        attack: int,
        defense: int,
        special_attack: int,
        special_defense: int,
        speed: int
    ):
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.special_attack = special_attack
        self.special_defense = special_defense
        self.speed = speed

    def __str__(self):
        return (
            f"HP: {self.hp}, Attack: {self.attack}, Defense: {self.defense}, "
            f"Sp. Attack: {self.special_attack}, Sp. Defense: {self.special_defense}, Speed: {self.speed}"
        )

#pokemos refactorizado
class Pokemon:
    def __init__(
        self,
        tipo: str,
        nombre: str,
        stats: Stats,
        nivel: int = 1,
        habilidad_especial: str = "ninguno"
    ):
        self.tipo = tipo
        self.nombre = nombre
        self.stats = stats
        self.nivel = nivel
        self.habilidad_especial = habilidad_especial

    def mostrar_stats(self):
        print(f"{self.nombre} → {self.stats}")