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
# alucard.ultimate(dragon)
# print(f"ambil hp hero: {alucard.__hp}")
# alucard.set_hp(1000)
# print(f"ambil hp hero: {alucard.get_hp()}")

# eudora.ultimate(dragon)
# eudora.heal()
# eudora.combo(dragon)

# hayabusa.ultimate(dragon)
# betrix.combo(dragon)
# betrix.ultimate(dragon)

# print("\n== CEK STATUS ==")
# print(alucard)
# print(eudora)
# print(betrix)
# print(hayabusa)

running = True
while running:
    print("=" * 25) 
    print("== STATUS BOS LANTAI ==")
    print(dragon)
    print("\n== PILIHAN AKSI : ==")
    print("*** 1. ATTACK")
    print("*** 2. HEAL")
    print("*** 3. ULTIMATE")
    print("*** 4. EXIT\n")
    
    # buat validasi inputan user
    aksi = 0 # nilai awal
    try:
        # ambil inputan user    
        aksi = int(input(">>> AKSI MU : "))
    except ValueError:
        # tangkap error
        print("❌ AKSI harus angka bulat (integer) 1-4!")

    # buat list raid party
    raid_party = [alucard, eudora, betrix, hayabusa]
    # atk_party = [25, 10, 15, 20] -> alternatif at
    if aksi == 1: # attack mode
        for party in raid_party:
            party.attack(dragon, 10)
        # cek hp dragon kalau 0 selesai
        if dragon.hp == 0:
            running = False
            print("== BOS TELAH MATI, GAME SELESAI! ==\n")
    
    elif aksi == 2: # heal mode
        for party in raid_party:
            party.heal()

    elif aksi == 3: # ultimate mode
        for party in raid_party:
            party.ultimate(dragon)
        # cek hp dragon kalau 0 selesai
        if dragon.hp == 0:
            running = False
            print("== BOS TELAH MATI, GAME SELESAI! ==\n")

    elif aksi == 4: # exit mode
        running = False
        print("== GAME BERAKHIR, BYE BYE! ==\n")

    else:
        print("== ⚠️ AKSI SALAH, COBA YG LAIN 1-4! ==\n")
