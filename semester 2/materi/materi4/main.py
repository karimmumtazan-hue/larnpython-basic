from monster import Monster
from warrior import Warrior
from mage import Mage
from archer import Archer
from assasin import Assasin

print("== SUMMON SEMUA HERO ==")
alucard = Warrior("Alucard", 100)
eudora = Mage("Eudora", 100)
betrix = Archer("Betrix", 100)
hayabusa = Assasin("Hayabusa", 100)
print("\n== SUMMON BOSS ==")
dragon = Monster("Dragon King", 1000)

print("\n== RAID DIMULAI! ==")
alucard.ultimate(dragon)
print(f"ambil hp hero: {alucard}")

eudora.ultimate(dragon)
eudora.heal()
eudora.combo(dragon)
hayabusa.ultimate(dragon)
betrix.combo(dragon)
betrix.ultimate(dragon)

print("\n== CEK STATUS ==")
print(alucard)
print(eudora)
print(betrix)
print(hayabusa)
print(dragon)

running = True
while running:
    print("=== STATUS BOS LANTAI ===")
    print(dragon)
    print("\nPILIH AKSI:")
    print("1. ATTACK")
    print("2. HEAL")
    print("3. ULTIMATE")
    print("4. EXIT\n")

aksi = int(input(">> AKSI MU : "))
#buat list party
raid_party = [ alucard, eudora, betrix, hayabusa]
# atk_party = [ 30, 10, 15, 20] alternatif atk beda2
aksi = 0
try:
    # ambil inputan user
    aksi = int(input(">> AKSI MU : "))
except ValueError:
    # tangkp eror
    print("AKSI harus angka bulat(integer) 1-4!")

if aksi == 1: # attack mode
    for party in raid_party:
        party.attack(dragon, 10)
    # cek HP dragon kalau 0 berarti udah mati/selesai
    if dragon.hp <= 0:
        running = False
        print("=== BOSS TELAH MATI, GAME BERAKHIR ===\n")

elif aksi == 2: # healing mode
    for party in raid_party:
        party.heal()

elif aksi == 3:
    

elif aksi == 4: # exit mode
    running = False
    print("=== GAME BERAKHIR, DADAH NOOB! ===")