# print = output data ke terminal 
print("Object-Oriented Programming")
print("="*100)
# tipe data python 
nama = "karim sajid" # string (str) = (text)
umur = 17 # integer (int) = (nomor)
status_nikah = True # boolean (bool) (True/Fasle)
print(f"{nama}, umur {umur} tahun, status {status_nikah} nikah")
namateman = ["nadhif", "aaqif", "dapo", "bibul", "peti"]
print ("teman saya ",namateman)
# fungsi di awali kata "def"
# def namafungsi (parameter-parameter)
def halo(name, kota):
    print(f"Halo aku {name}, asal {kota}")
    print("-" * 20)
# panggil namaFungsi diluar def
halo("nadhif", "jogja")
halo("bibul", "cilacap")
    