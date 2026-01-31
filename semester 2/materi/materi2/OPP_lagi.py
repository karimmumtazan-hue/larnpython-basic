class hero:
    #pertama kali dipanggil (summon)
    def __init__(self, name, job, hp):
        self.name = name
        self.job = job
        self.hp = hp
        print(f"✨ hero{self.name} telah disumaon ✨")

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


# buat objek ? smmon hero-hero ke loby
baxia = hero("baxia", "tank", 100)
poveus = hero("poveus", "tank", 100)
baxia.attack(poveus, 25)
print(poveus)
poveus.attack(baxia, 5)
poveus.attack(baxia, 5)
poveus.attack(baxia, 5)
poveus.heal()
print(baxia)
print("SKILL 2: BALANG TAMENG!")
baxia.attack(poveus, 75)
baxia.heal()
# cek status terkkini
print(baxia)
print(poveus)