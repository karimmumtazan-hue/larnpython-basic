import json

path_json = r"C:\SMA IT HSI\PYTHON\python-basic\tugas\json api\data_buku.json"
# Baca file JSON lokal
with open(path_json, "r") as file:
    data_materi=json.load(file)

total_pinjam = 0
belum_kembali = 0

print("Belum kembali:")
for anggota in data_materi["anggota"]:
    for buku in anggota["pinjam"]:
        total_pinjam += 1
        if buku["kembali"] == False:  
            belum_kembali += 1
            print(f"- {anggota['nama']} : {buku['judul']} ({buku['tanggal']})")

print(f"Total dipinjam: {total_pinjam} | Belum kembali: {belum_kembali}")