class Hero:
    def __init__(self, name, job, hp, damage, hero_type="hero", heal_power=0):
        self.name = name
        self.job = job
        self.hp_max = hp 
        self.hp = hp
        self.dmg = damage 
        self.heal_power = heal_power 
        self.type = hero_type 
        self.is_rage = False 
        self.is_alive_status = True
        print(f"✨ {self.name} ({self.job}) join ke battle!")

    def is_alive(self):
        return self.is_alive_status

    def attack(self, target):
        if not self.is_alive():
            print(f"❌ {self.name} udah mati, gak bisa nyerang.")
            return
        
        if not target.is_alive():
            print(f"❌ {target.name} udah tepar, jangan digebukin terus.")
            return

        final_dmg = self.dmg

        # FITUR RAGE MODE (State-based logic: HP <= 20%)
        if self.type == "boss" and self.hp <= (self.hp_max * 0.2):
            if not self.is_rage:
                self.is_rage = True
                print(f"\n😈 {self.name} memasuki RAGE MODE!")
            
            final_dmg *= 2 
            print(f"💥 CRITICAL HIT!")

        print(f"⚔️ {self.name} nyerang {target.name} | Damage: {final_dmg}")
        target.take_damage(final_dmg)

    def take_damage(self, damage):
        self.hp -= damage
        if self.hp <= 0:
            self.hp = 0
            self.is_alive_status = False
            print(f"💀 {self.name} mati!")
        else:
            print(f"🩸 {self.name} sisa HP: {self.hp}/{self.hp_max}")

    def heal(self, target):
        if not self.is_alive():
            print(f"❌ {self.name} mati, mana bisa nge-heal.")
            return
        
        if self.heal_power > 0:
            target.hp += self.heal_power
            if target.hp > target.hp_max:
                target.hp = target.hp_max
            print(f"💖 {self.name} nge-heal {target.name}. HP sekarang: {target.hp}")
        else:
            print(f"❌ {self.name} bukan healer, gak punya skill-nya.")

# --- Objek Karakter ---
baxia = Hero("Baxia", "Tank", 250, 15)
cecilion = Hero("Cecilion", "Mage", 100, 70)
rafaela = Hero("Rafaela", "Healer", 120, 10, heal_power=50)
goblin = Hero("Goblin Kroco", "Minion", 50, 10, "normal")
boss = Hero("Raja Iblis", "Boss", 400, 40, "boss")

print("\n=== MULAI PETUALANGAN ===")
baxia.attack(goblin)
cecilion.attack(goblin) 

print("\n=== LAWAN FINAL BOSS ===")
baxia.attack(boss)
boss.attack(baxia)
rafaela.heal(baxia)

print("\n--- Boss dipukulin sampai HP <= 20% (80 HP) ---")
cecilion.attack(boss) # HP 330
cecilion.attack(boss) # HP 260
cecilion.attack(boss) # HP 190
cecilion.attack(boss) # HP 120
cecilion.attack(boss) # HP 50 (Trigger Rage Mode di serangan berikutnya)

# Boss menyerang dalam mode Rage
boss.attack(cecilion)

# Serangan terakhir untuk membunuh Boss
print("\n--- Serangan Terakhir ---")
cecilion.attack(boss) 

print("\n=== STATUS TERAKHIR ===")
print(f"Status {baxia.name}: {baxia.hp} HP")
print(f"Status {cecilion.name}: {cecilion.hp} HP")
print(f"Status {boss.name}: {'💀MATI' if not boss.is_alive() else str(boss.hp) + ' HP'}")
