from hero import Hero

class Marksman(Hero):
    def __init__(self, name, hp):
        # super() = mengakses parent class (Hero)
        super().__init__(name, hp, job="Marksman")

    def ultimate(self, enemy):
        dmg = 50
        print(f"⚔️ {self.name} menggunakan ulti : RUDAL")
        print(f"skill ulti {dmg*2} DMG")
        # musuh terkena damage
        enemy.take_damage(dmg)
        enemy.take_damage(dmg)