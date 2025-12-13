import requests
# pip --version
# pip 

target_url = "https://api.aladhan.com/v1/timingsByCity/09-12-2025?city=Jakarta&country=Indonesia&method=20"
print(f"target URL: {target_url}")

# HTTP GET (ambil data)
response = requests.get(target_url)
# konversi data ke JSON
data_json = response.json()
# print(f"Response data: {data_json}")
print("JADWAL SHOLAT")
print("="*20)
jadwal = data_json['data']['timings']
subuh = jadwal['Fajr']
dzuhur = jadwal['Dhuhr']
print(f"- subuh: {subuh}")
print(f"- dzuhur: {dzuhur}")

