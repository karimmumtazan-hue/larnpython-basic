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