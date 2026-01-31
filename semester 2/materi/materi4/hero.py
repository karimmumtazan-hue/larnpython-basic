class Hero:
    # pertama kali dipanggil (summon)
    # self = dirinya sendiri / internal
    def __init__(self, name, hp, job):
        self.name = name
        self.job = job
        self.__hp = hp
        print(f"✨ [{job}] Hero {self.name} telah di summon!")

    # getter (ambil data attr yang private)
    def get_hp(self):
        return self.__hp
    
    # setter (update data yang private biar gak bisa di kasih cheat)
    def set_hp(self, number):
        self.__hp += number

    def heal(self):
        print(f"🧪 {self.name} meminum potion...")
        heal_amount = 20
        self.__hp += heal_amount
        print(f"💚 HP {self.name} bertambah +{heal_amount}")

    def take_damage(self, damage):
        # self.__hp = self.__hp - damage (aslinya)
        self.__hp -= damage
        print(f"💥 {self.name} terkena {damage} damage\n")
        # print(f"💚 Sisa HP: {self.__hp}")
        if self.__hp == 0:
            print(f"🚫 {self.name} tereliminasi dari arena!")
    
    def attack(self, enemy, damage):
        print(f"⚔️ {self.name} menyerang {enemy.name}!")
        # panggil method lain dari dalam
        enemy.take_damage(damage)

    # fungsi cek status terkini 
    def __str__(self):
        status = "🟢 HIDUP" 
        if self.__hp == 0:
            status = "💀 MATI" 

        return f"[{self.job}] {self.name} | HP: {self.__hp} | {status}"
    
    # skill ultimate (dasar)
    def ultimate(self, enemy):
        print(f"⚔️ {self.name} bengong!")


# untuk contoh (self.__hp), ini dikasih underscore dua, biar gak bisa di kasih cheat nyawanya (misalkan = nyawanya jadi : HP: 999999999)