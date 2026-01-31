class Monster:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
        print(f"✨ Monster {self.name} telah di summon!")

    def take_damage(self, damage):
        self.hp -= damage
        print(f"💥 {self.name} terkena {damage} damage\n")
        if self.hp == 0:
            print(f"🚫 {self.name} tereliminasi dari arena!")

    # fungsi cek status terkini 
    def __str__(self):
        status = "🟢 HIDUP" 
        if self.hp == 0:
            status = "💀 MATI" 

        return f"[Monster] {self.name} | HP: {self.hp} | {status}"