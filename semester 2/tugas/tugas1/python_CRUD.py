print("TUGAS PYTHON CRUD (Create,Read,Update,Delete)")
print("="*100)

daftar_siswa = []

def tambah():
    id_siswa = input("Masukkan ID: ")
    nama = input("Masukkan Nama: ")
    siswa = {"id": id_siswa, "nama": nama}
    daftar_siswa.append(siswa)
    print("Data berhasil ditambahkan.")
    print("="*70)

def tampilkan():
    print("\n--- Data Siswa ---")
    if len(daftar_siswa) == 0:
        print("Data kosong.")
    else:
        for siswa in daftar_siswa:
            print(f"ID: {siswa['id']}, Nama: {siswa['nama']}")
            print("="*70)

def ubah():
    id_cari = input("Masukkan ID data yang akan diubah: ")
    for siswa in daftar_siswa:
        if siswa['id'] == id_cari:
            siswa['nama'] = input("Masukkan Nama Baru: ")
            print("Data berhasil diubah.")
            return
    print("ID tidak ditemukan.")
    print("="*70)

def hapus():
    id_cari = input("Masukkan ID data yang akan dihapus: ")
    for siswa in daftar_siswa:
        if siswa['id'] == id_cari:
            daftar_siswa.remove(siswa)
            print("Data berhasil dihapus.")
            print("="* 70)
            return
    print("ID tidak ditemukan.")
    print("="*70)

while True:
    print("\n--- MENU CRUD ---")
    print("1. Tambah Data")
    print("2. Menampilkan Data")
    print("3. Mengubah Data")
    print("4. Menghapus Data")
    print("5. Keluar")

    print("(untuk menampilakn,mengubah atau menghapus data, silahkan tambahkan data terlebih dahulu)")

    pilihan = input("Pilih menu (1-5): ")
 
    if pilihan == "1":
        tambah()
    elif pilihan == "2":
        tampilkan()
    elif pilihan == "3":
        ubah()
    elif pilihan == "4":
        hapus()
    elif pilihan == "5":
        print("Program selesai.")
        print("="*100)
        break
    else:
        print("Pilihan tidak tersedia.")
