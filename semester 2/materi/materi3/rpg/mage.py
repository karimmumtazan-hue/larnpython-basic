from hero import Hero

class Mage(Hero):
    def __init__(self, name, hp):
        # super() = mengakses parent class (Hero)
        super().__init__(name, hp, job="Mage")

    def ultimate(self, enemy):
        dmg = 85
        print(f"{self.name} menggunakan skill 1: FIRE ARROW")
        print(f"dengan damage {dmg} DMG")
        # monster terkena damage
        enemy.take_damage(dmg)

    # method baru khusus mage aja
    def combo(self, enemy):
        dmg = 20
        print(f"{self.name} menggunakan skill combo: WATER CANON x3 {dmg*3} DMG")
        # monster terkena damage
        enemy.take_damage(dmg)
        enemy.take_damage(dmg)
        enemy.take_damage(dmg)
