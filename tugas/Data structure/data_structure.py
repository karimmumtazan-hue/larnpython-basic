# Tantangan 1: Jadwal Piket Harian 🕌
piket_hari_ini = ['Ali', 'Budi', 'Aisyah']

print("Jadwal piket hari ini:")
for nama in piket_hari_ini:
    print("-", nama)

print()  # baris kosong biar rapi

# Tantangan 2: Rukun Islam ✨
rukun_islam = ('Syahadat', 'Shalat', 'Zakat', 'Puasa', 'Haji')

print("Daftar Rukun Islam:")
for rukun in rukun_islam:
    print("-", rukun)

print()

# Tantangan 3: Kitab-Kitab Pelajaran 📚
kitab_pelajaran = {'Kitab Tajwid', 'Kitab Fiqh', 'Kitab Aqidah'}

print("Kitab-kitab yang dipelajari:")
for kitab in kitab_pelajaran:
    print("-", kitab)

print()

# Tantangan 4: Biodata Santri 🎓
biodata = {
    'nama': 'Fatimah',
    'kelas': 'X-A',
    'hafalan_juz': 5
}

print("Biodata Santri:")
for key, value in biodata.items():
    print(f"{key}: {value}")
