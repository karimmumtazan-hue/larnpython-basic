import json

file_path_json = r"C:\SMA IT HSI\PYTHON\python-basic\tugas\json api\data_buku.json"
# Baca file JSON lokal
with open(file_path_json, "r") as file_materi:
    data_materi=json.load(file_materi)

total_pinjam = 1
belum_kembali = 0

print("Belum kembali:")
for anggota in data_materi["anggota"]:
    for buku in anggota["pinjam"]:
        total_pinjam += 1
        if buku["kembali"] == False:  
            belum_kembali += 1
            print(f"- {anggota['nama']} : {buku['judul']} ({buku['tanggal']})")

print(f"Total dipinjam: {total_pinjam} | Belum kembali: {belum_kembali}")