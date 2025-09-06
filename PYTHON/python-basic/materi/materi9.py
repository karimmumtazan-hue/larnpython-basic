print("MATERI 9 - PYTHON 3 FUNCTION")
print("-----------------------------")
# fungsi biasa dengan `def` jika lebih dari 1 baris
def hello_world(name):
    print("Hello Mr.", name)
    print(f"How you doing {name}?") # f (formatting string)

hello_world("Azka")
hello_world("Haris")
print("------------> LAMBDA <-----------")
# fungsi anonim dengan `lambda` jika 1 baris saja
greeting = lambda name: print(f"Hello, {name} with lambda")
greeting("Azmi")
greeting("Karim")

print("----- KONVERSI TIPE DATA ----")
# "" artinya string walaupun dia isinya angka
nilai_string = "1000" # tipe datanya string
nilai_integer = int(nilai_string) # int (ubah jadi integer)
kalikan_dua_salah = nilai_string * 2
kalikan_dua_bener = nilai_integer * 2
print(kalikan_dua_salah, kalikan_dua_bener)
print("----- MAP ----")
# map() untuk mentransformasi data dari list
# map([fungsi_perubahan_data], [sumber_data])
nilai_mentah = [1.9, 0.82, 4.5, 8.9, 2.1, 0.95, 2.46]
nilai_kali_seratus = map(lambda nilai: nilai * 100, nilai_mentah)
# konversi map object menjadi list
list_nilai_kali_seratus = list(nilai_kali_seratus) 
print(f"Nilai mentahan: {nilai_mentah}")
print(f"Nilai x 100: {list_nilai_kali_seratus}")
print("----- SORT ----")
# sorted () mengurutkan data
daftar_siswa = [
  {"nama": "Haris", "angka": 8},
  {"nama": "Zaky", "angka": 77},
  {"nama": "Abdul Ubuntu", "angka": 25},
  {"nama": "Hanif", "angka": 26},
]
print("DAFTAR ANGKA ASLI", daftar_siswa)
daftar_siswa_terurut = sorted(daftar_siswa, key=lambda siswa: siswa['angka'])
# for loop -> mengeluarkan seluruh isi daftar
for siswa in daftar_siswa_terurut:
  print(siswa)
# sorting list
daftar_nama_kelas_b = ["hanif", "wildan", "syamil", "ziyad", "royyan","abdul","azmi"]
daftar_nama_terutut = sorted(daftar_nama_kelas_b) # a ke z (kecil-besar)
daftar_nama_terbalik = sorted(daftar_nama_kelas_b, reverse=True) # z ke a (besar-kecil)
for nama in daftar_nama_terutut: 
  print(nama)
print("------------ ####### -----------")
for nama in daftar_nama_terbalik:
  print(nama)

print("------------ FILTER -----------")
# filter() menyaring data
transaksi = [25000, 18000, 13000, 10000, 125000, 200000]
transaksi_besar = filter(lambda angka: angka >= 25000, transaksi)
list_transaksi_besar = list(transaksi_besar)
print("Data transaksi:", transaksi)
print("Transkasi diatas 25rb:", list_transaksi_besar)