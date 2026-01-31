class Hero:
    #pertama kali dipanggil (summon)
    def __init__(self, name, hp, job):
        self.name = name
        self.job = job
        self.hp = hp
        print(f"✨hero [{job}] {self.name} telah disummon ✨")

    def heal(self):
        print(f"✨ {self.name} heal...")
        heal_amount = 20
        self.hp = heal_amount
        print(f"HP {self.name} bertambah +{heal_amount}")
    
    def take_damage(self, damage):
        # self.hp = selp.hp - damage (codingan aslinya atau versi panjangnya)
        self.hp -= damage
        print(f"💥 {self.name} terkena {damage} damage")
        print(f"❤️ sisa HP: {self.hp}")
        if self.hp == 0:
            print(f"🚫 {self.name} tereliminasi dari arena")
    
    def attack(self, enemy, damage):
        print(f"⚔️ {self.name} menyerang {enemy.name}")
        # panggil method lain dari dalam
        enemy.take_damage(damage)

    def __str__(self):
        status = "🟢 HIDUP"
        if self.hp == 0:
            status = "💀 MATI"
        return f"{self.name} {self.job} | HP: {self.hp} | status: {status}"
    
    def ultimate(self, enemy, damage):
        print(f"⚔️ {self.name} bengong!")