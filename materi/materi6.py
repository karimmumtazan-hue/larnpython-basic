print("Materi 6B - Python Data Structure")
print("===================================")
# List -> [] -> berurutan, berubah, duplikat
daftar_belanjaan = [
  "es teh desa", # index 0
  "olive chicken", # index 1
  "gorengan", # index 2
]
print("Daftar Belanjaan:", daftar_belanjaan)
print(daftar_belanjaan[2]) # akses index ke 2
# append() menambah item ke akhir list
daftar_belanjaan.append("gabin")
# insert() menambah item ke spesifik index
daftar_belanjaan.insert(0, "naspad kawan lamo")
print("Daftar Belanjaan Skrg:", daftar_belanjaan)
# remove() menghapus item berdasarkan value
daftar_belanjaan.remove("olive chicken")
print("Daftar Belanjaan Akhir:", daftar_belanjaan)
# [no_index:no_urut_item]
print("Potong list: ", daftar_belanjaan[1:3])
# menggabungkan list +
jajanan_bilal = ["basreng", "macaroni"]
jajanan_zaky = ["pisang kembung", "pentol"]
gabungan_jajanan = jajanan_zaky + jajanan_bilal
print("Gabungan Jajanan: ", gabungan_jajanan)
print("Bilal nambah:", jajanan_bilal * 3)

# Tuple -> () -> berurutan, berubah, tidak duplikat
ttl = ("Depok", 10, "July", 2001)
print("TTL Hamka:", ttl)
print("Tgl lahir:", ttl[1])
# unpacking tuple ke variable baru
# harus berurutan sesuai value nya
tempat_lahir, tgl_lahir, bln_lahir, thn_lahir = ttl
print("Tempat lahir:", tempat_lahir)
print("Tahun lahir:", thn_lahir)
# list multi dimensi / bertingkat
# cara akses [baris_index][kolom_index]
daftar_minuman = [
  ["kopi", "teh", "susu jahe", "ronde"], # baris 0
  ["jus apel", "jus jeruk"], # baris 1
  ["es doger", "es campur", "es teler"] # baris 2
]
print(daftar_minuman)
print("Es paporit Ali:",  daftar_minuman[2][0])
print("Wedang paporit zaky:", daftar_minuman[0][3])