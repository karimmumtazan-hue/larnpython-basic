import csv

print("Materi 10 - File Handling")
print("-------------------------")
# buka file
file_path = r"K:\SMA IT HSI\PYTHON\materi\materi10\pesan.txt" # sesuaikan sendiri
file_pesan = open(file_path, "r")
# baca isi file
isi_pesan = file_pesan.read()
# tampilkan output isi pesan
print(f"ISI PESAN => {isi_pesan}")
# tutup file
file_pesan.close()

print('-----READ CSV FILE -----')
file_path_csv = r"K:\SMA IT HSI\PYTHON\materi\materi10\jajan.csv"
file_jajan = open(file_path_csv, "r")
isi_table_jajan = file_jajan.read()
print(f"TABLE JAJAN => {isi_table_jajan}")
file_jajan.close()

print('-----APPEND CSV FILE -----')
jajan_baru = [6,"karim",100000]
print(f"Jajan baru: {jajan_baru}")
with open(file_path_csv, "a", newline="") as file_jajan:
  writer = csv.writer(file_jajan)
  writer.writerow(jajan_baru)