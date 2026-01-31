class Monster:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
        print(f"✨ [Monster] {self.name} telah disummon ✨")
    
    def take_damage(self, damage):
        # self.hp = selp.hp - damage (codingan aslinya atau versi panjangnya)
        self.hp -= damage
        print(f"💥 {self.name} terkena {damage} damage")
        print(f"❤️ sisa HP: {self.hp}")
        if self.hp == 0:
            print(f"🚫 [Monster] {self.name} tereliminasi dari arena")

    def __str__(self):
        status = "🟢 HIDUP"
        if self.hp == 0:
            status = "💀 MATI"
        return f"{self.name} [Monster] | HP: {self.hp} | status: {status}"

