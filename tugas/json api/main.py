import requests
import arabic_reshaper
from bidi.algorithm import get_display



alamat_url = f"https://api.alquran.cloud/v1/ayah/2:255/quran-simple"
importan = requests.get(alamat_url)
datajson1 = importan.json()
arabnya = datajson1['data']["text"]

reshaped_text = arabic_reshaper.reshape(arabnya)
bidi_text = get_display(reshaped_text)


print("=" * 50)
print("ayat kursi font arabic")
print(bidi_text)

url = f"https://api.alquran.cloud/v1/ayah/2:255/en.asad"
dari_txt = requests.get(url)
datajson2 = dari_txt.json()
inggrisnya = datajson2['data']

print("=" * 50)
print("TERJEMAH ENGLISH :")
print(f"{inggrisnya['text']}")