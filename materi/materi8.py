print("MATERI 8B - FUNCTION DASAR")
print("---------------------------")
# struktur fungsi dasar tanpa parameter
def halo_dunia():
  print("Hello World")
  print("Halo Dunia")
# cara akses function, sertakan nama dan () -nya
halo_dunia()
# fungsi dengan parameter (variable di fungsi)
def sapa_sapa_gan(nama):
  print("Halo", nama, " selamat gawe di HSI")
# fungsi dengan banyak parameter
def rumus_luas_segi_tiga(alas, tinggi):
  print("Alas:", alas)
  print("Tinggi:", tinggi)
  rumusan = 1/2 * (alas * tinggi)
  print("Hasil:", rumusan)

sapa_sapa_gan("Ujang")
sapa_sapa_gan("Asep")
# klo manual begini misalnya report
print("Halo Ujang selamat kerja di HSI")
print("Halo Asep selamat kerja di HSI")
rumus_luas_segi_tiga(10, 30)
rumus_luas_segi_tiga(50, 100)

# filter teman toxic
def filter_teman_toxic(nama, sifat):
  # ciri-ciri toxic
  sifat_toxic = [
    "julid",
    "pamer",
    "ngatain",
    "baperan",
    "manipulatif",
    "drama",
    "sombong",
  ]
  # deteksi kata sifat toxic dari parameter sifat
  if any(kata in sifat for kata in sifat_toxic):
    print(nama, "itu teman Toxic, kabooor....")
  else: 
    print(nama, "teman baek, lanjutken.....")

filter_teman_toxic("azka", "rajin baik hati tawadhu")
filter_teman_toxic("asep", "sombong manipulatif drama")