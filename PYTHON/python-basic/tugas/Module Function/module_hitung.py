def tambah_bonus(uang_list):
    return list(map(lambda x: x + 5000, uang_list))

def filter_boros(uang_list):
    return list(filter(lambda x: x >= 50000, uang_list))
