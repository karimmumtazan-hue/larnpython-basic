from monster import Monster
from mage import Mage
from tank import Tank
from marksman import Marksman
from assasin import Assasin

baxia = Tank("baxia", 100)
kagura = Mage("kagura", 100)
granger = Marksman("granger", 100)
joy = Assasin("joy", 100)
lord = Monster("lord", 1000)

baxia.ultimate(lord)
print(baxia)
print(kagura)
print(granger)
print(joy)
print(lord)