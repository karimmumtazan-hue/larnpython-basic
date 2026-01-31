from hero import Hero

class Archer(Hero):
    def __init__(self, name, hp):
        # super() = mengakses parent class (Hero)
        super().__init__(name, hp, job="Archer")

    def ultimate(self, enemy):
        dmg = 80
        print(f"{self.name} menggunakan skill 1: RAIN ARROW")
        print(f"dengan damage {dmg} DMG")
        # monster terkena damage
        enemy.take_damage(dmg)

    # method baru khusus archer aja
    def combo(self, enemy):
        dmg = 10
        print(f"{self.name} menggunakan skill combo: WIND ARROW x3 {dmg*3} DMG")
        # monster terkena damage
        enemy.take_damage(dmg)
        enemy.take_damage(dmg)
        enemy.take_damage(dmg)
