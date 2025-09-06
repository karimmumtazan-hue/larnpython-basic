# Import semua module
import module_doa
import module_hitung
import module_ranking
import module_emoji
import module_ngaji

# ==== Tugas 1 ====
print("\n--- Tugas 1: Doa Harian ---")
module_doa.doa_tidur()
module_doa.doa_bangun()
module_doa.doa_makan()

# ==== Tugas 2 ====
print("\n--- Tugas 2: Hitung Uang Jajan ---")
jajan = [50000, 30000, 15000, 70000, 10000]
jajan_bonus = module_hitung.tambah_bonus(jajan)
print("Setelah Bonus:", jajan_bonus)
jajan_boros = module_hitung.filter_boros(jajan)
print("Uang Boros (≥ 50rb):", jajan_boros)

# ==== Tugas 3 ====
print("\n--- Tugas 3: Ranking Nilai ---")
nilai = [75, 90, 60, 88, 100, 55]
print("Nilai Descending:", module_ranking.urutkan_nilai(nilai))
print("Nilai Tertinggi:", module_ranking.nilai_tertinggi(nilai))
print("Nilai Terendah:", module_ranking.nilai_terendah(nilai))

# ==== Tugas 4 ====
print("\n--- Tugas 4: Emoji Mood ---")
mood_siswa = ["senang", "sedih", "semangat", "biasa", "marah"]
emoji_list = module_emoji.convert_mood(mood_siswa)
print("Emoji Mood:", emoji_list)

# ==== Tugas 5 ====
print("\n--- Tugas 5: Tracker Ngaji ---")
halaman_minggu = [5, 6, 4, 7, 3, 5, 6]  # total = 36
total = module_ngaji.total_ngaji(halaman_minggu)
print("Total Halaman Ngaji:", total)
print("Cek Target:", module_ngaji.cek_target(total))
