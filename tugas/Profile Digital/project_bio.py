from datetime import datetime

# Input data
nama = input("Nama lengkap: ")
umur = int(input("Umur: "))
kelas = input("Kelas: ")
cita = input("Impian: ")
hobi = input("Hobi favorit: ")
belajar = input("Belajar enaknya pas (pagi/malam): ")

# Hitung tahun lahir
tahun_lahir = datetime.now().year - umur

# Pilih gaya digital
print("\nPilih gaya digital:")
print("1. Wibu\n2. Gamer\n3. K-Popers\n4. Anak Konten\n5. Anak Nongki")
tipe = int(input("Pilihan (1-5): "))

# Pertanyaan tambahan & komentar
if tipe == 1:
    tambahan = input("Waifu/husbando kamu: ")
    komentar = "Waifu is life! 🗾💖"
elif tipe == 2:
    tambahan = input("Game favorit: ")
    komentar = f"GG gaming! 🎮🔥"
elif tipe == 3:
    tambahan = input("Bias kamu: ")
    komentar = "Oppa style! 💅🎤"
elif tipe == 4:
    tambahan = input("Platform favorit: ")
    komentar = "Konten kamu pasti viral! 📱🎥"
elif tipe == 5:
    tambahan = input("Tempat nongkrong favorit: ")
    komentar = "Vibes nongki-nya dapet banget 😎☕"
else:
    tambahan = "-"
    komentar = "Gaya digitalmu misterius banget,calon daftar hitam digital ya"

# Pertanyaan bonus
bau = input("Teman sebelah bau? (ya/tidak): ")
reaksi = "masukin kandang mas boy🙊" if bau == "ya" else "Udara aman 😌"

# Output
print("\n===== PROFIL DIGITAL KAMU =====")
print(f"Nama: {nama}")
print(f"Umur: {umur} tahun")
print(f"Kelas: {kelas}")
print(f"Hobi: {hobi}")
print(f"Cita-cita: {cita}")
print(f"Belajar paling enak pas: {belajar}")
print(f"Tahun lahir: {tahun_lahir}")

print("\n=== TIPE DIGITAL ===")
tipe_dict = ["Wibu", "Gamer", "K-Popers", "Anak Konten", "Anak Nongki"]
print(f"Tipe: {tipe_dict[tipe-1] if 1 <= tipe <= 5 else 'Tidak diketahui'}")
print(f"Jawaban tambahan: {tambahan}")
print(f"Komentar: {komentar}")

print("\n=== FUN CHECK ===")
print(f"Teman sebelah bau? {bau}")
print(reaksi)
print("================================")