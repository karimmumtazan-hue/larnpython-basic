from hero import Hero

class Assasin(Hero):
    def __init__(self, name, hp):
        # super() = mengakses parent class (Hero)
        super().__init__(name, hp, job="Assasin")

    def ultimate(self, enemy):
        dmg = 90
        print(f"{self.name} menggunakan skill 1: SHADOW KILL")
        print(f"dengan damage {dmg} DMG")
        # monster terkena damage
        enemy.take_damage(dmg)
