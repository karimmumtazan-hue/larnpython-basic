from hero import Hero

class Tank(Hero):
    def __init__(self, name, hp):
        # super() = mengakses parent class (Hero)
        super().__init__(name, hp, job="Tank")

    def ultimate(self, enemy):
        dmg = 100
        print(f"⚔️ {self.name} menggunakan ulti : JEJAK BARA")
        print(f"dengan damage {dmg} DMG")
        # musuh terkena damage
        enemy.take_damage(dmg)