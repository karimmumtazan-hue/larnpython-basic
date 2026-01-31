# diawali class namaClass
class Cat:
    # self = dirinya sendiri / internal class
    # _init_ = constructor = fungsi yang pertama kali dipangil
    def __init__(self, color, weight):
        self.color = color
        self.weight = weight
    # method = fungsi di dalam class
    def sleep(self, durasi):
        print(f"turu {durasi} menit")

#buat objek dari class cat
belang = Cat("mix", 7)
oyen = Cat("oren butek", 3)
belang.sleep(60)
oyen.sleep(7)
print(f"warna si oyen: {oyen.color}")
print(f"berat si oyen: {oyen.weight} kg")
