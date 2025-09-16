def total_ngaji(halaman_list):
    return sum(halaman_list)

def cek_target(total, target=35):
    return "Tercapai 🎉" if total >= target else "Belum tercapai 😔"
