print("MATERI 7B - PYTHON DATA STRUCTURE")
print("==================================")
# Set -> { } -> tidak berurutan, berubah, tidak duplikat
game_azka = {"valorant", "dark soul"}
game_evan = {"valorant", "genshin", "mlbb"}
print("Azka games: ", game_azka)
print("Evan games: ", game_evan)
# .add() -> menambahkan item baru
game_azka.add("elden ring")
game_azka.add("valorant") # tidak akan bertambah
# .remove() -> menghapus item
game_evan.remove("mlbb")
# len() menghitung jumlah item
print("Azka ada ", len(game_azka)," games: ", game_azka)
print("Evan ada ", len(game_evan)," games: ", game_evan)
# .union() -> menggabung 2 set berbeda
game_berdua = game_azka.union(game_evan)
total_game = len(game_berdua)
print("Semua game ada ", total_game," games: ", game_berdua)
# intersection() -> mencari item yg kembar
# difference() -> mencari item yg beda
game_kembar = game_azka.intersection(game_evan)
game_beda = game_azka.difference(game_evan)
total_game_kembar = len(game_kembar)
total_game_beda = len(game_beda)
print("Game yg kembar ", total_game_kembar," games: ", game_kembar)
print("Game yg beda ", total_game_beda," games: ", game_beda)
print("\n -------- DICT -------- \n")
# Dict (dictionary) -> {key:value} / {kunci:isinya}
# berurutan berdasarkan key, berubah, 
# key tidak boleh duplikat
koleksi_anime = {
  "re_zero": "subaru",
  "onePiece": "usop",
  "waifu": {
    "re_zero": "rem-chan", # tdk masalah key sama klo struktur beda
    "demon_slayer": "nezuko"
  }
}
print("Koleksi Anime: ", koleksi_anime)
print("MC One piece:", koleksi_anime["onePiece"])
print("Waifu re zero:", koleksi_anime["waifu"]["re_zero"])
# menambah atau mengubah data dict
koleksi_anime["naruto"] = "boruto"
koleksi_anime["onePiece"] = "zoro"
koleksi_anime["waifu"]["re_zero"] = "rem kanan"
print("Koleksi Anime Skrg: ", koleksi_anime)