from hero import Hero

class Mage(Hero):
    def __init__(self, name, hp):
        # super() = mengakses parent class (Hero)
        super().__init__(name, hp, job="Mage")

    def ultimate(self, enemy):
        dmg = 25
        print(f"⚔️ {self.name} menggunakan ulti : PAYUNG NJEBLUG")
        print(f"skill ulti {dmg*4} DMG")
        # musuh terkena damage
        enemy.take_damage(dmg)
        enemy.take_damage(dmg)
        enemy.take_damage(dmg)
        enemy.take_damage(dmg)