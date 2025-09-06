import requests


alamat_url = f"https://api.alquran.cloud/v1/ayah/2:255/quran-simple"
importan = requests.get(alamat_url)
datajson1 = importan.json()
arabnya = datajson1['data']

print("=" * 50)
print("ayat kursi font arabic")
print(f"{arabnya["text"]}")

urli = f"https://api.alquran.cloud/v1/ayah/2:255/en.asad"
dari_txt = requests.get(urli)
datajson2 = dari_txt.json()
inggrisnya = datajson2['data']

print("=" * 50)
print("TERJEMAH ENGLISH :")
print(f"{inggrisnya['text']}")