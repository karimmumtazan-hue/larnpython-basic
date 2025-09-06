import csv

# baca semua data dari csv

with open("keuangan.csv", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    data = list(reader)
print(data)

print("\n")
#mulai tugas
# 1. tampikan semua data 
print("semua data : ")
for row in data:
    print(f" {row['Tanggal']} | {row['Keterangan']} | {row['Kategori']} | Rp.{row['Jumlah']} ")

# 2. hitung semua pengeluaran
total = sum(int(row['Jumlah']) for row in data)
print(f" total pengeluaran: Rp.{total}")

# 3. hitung total per kategori
kategori_total = {}
for row in data:
    kategori = row['Kategori']
    jumlah = int(row['Jumlah'])
    if kategori not in kategori_total:
        kategori_total[kategori] = 0
    kategori_total[kategori] += jumlah

print("pengeluaran per kategori: ")
for kategori, jumlah in kategori_total.items():
    print(f"- {kategori} : Rp.{jumlah}")