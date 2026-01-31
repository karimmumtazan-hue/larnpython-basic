from hero import Hero

class Assasin(Hero):
    def __init__(self, name, hp):
        # super() = mengakses parent class (Hero)
        super().__init__(name, hp, job="Assasin")

    def ultimate(self, enemy):
        dmg = 35
        print(f"⚔️ {self.name} menggunakan ulti : THUNDERBOLT")
        print(f"skill ulti {dmg*3} DMG")
        # musuh terkena damage
        enemy.take_damage(dmg)
        enemy.take_damage(dmg)
        enemy.take_damage(dmg)