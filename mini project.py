#Nama: Farhan Imannudin
# NIM: 2309116028
# checkpoint 1
# untuk pengembangan selanjutnya akan ada pretty table, rating dapat memakai koma,
# penyelesaian error apabila input sesuatu, untuk sekarang tahap awal saja


class WebtoonManager:
    def __init__(self):
        self.webtoons = []

    def create_webtoon(self, judul, genre, tahun, rating, penulis):
        webtoon = {
            'judul': judul,
            'genre': genre,
            'tahun': tahun,
            'rating': rating,
            'penulis': penulis
        }
        self.webtoons.append(webtoon)
        print(f"Webtoon '{judul}' berhasil ditambahkan!")

    def read_webtoons(self):
        if not self.webtoons:
            print("Belum ada webtoon yang tersedia.")
        else:
            print("Daftar Webtoon:")
            for i, webtoon in enumerate(self.webtoons, 1):
                print(f"{i}. {webtoon['judul']} ({webtoon['tahun']}), Genre: {webtoon['genre']}, Rating: {webtoon['rating']}, Penulis: {webtoon['penulis']}")

    def update_webtoon(self, index, judul, genre, tahun, rating, penulis):
        if 1 <= index <= len(self.webtoons):
            webtoon = self.webtoons[index - 1]
            webtoon['judul'] = judul
            webtoon['genre'] = genre
            webtoon['tahun'] = tahun
            webtoon['rating'] = rating
            webtoon['penulis'] = penulis
            print(f"Webtoon '{judul}' berhasil diperbarui!")
        else:
            print("Index tidak valid. Perbaruan webtoon gagal.")

    def delete_webtoon(self, index):
        if 1 <= index <= len(self.webtoons):
            deleted_webtoon = self.webtoons.pop(index - 1)
            print(f"Webtoon '{deleted_webtoon['judul']}' berhasil dihapus!")
        else:
            print("Index tidak valid. Penghapusan webtoon gagal.")

def main():
    webtoon_manager = WebtoonManager()

    while True:
        print("\n========= Menu =========")
        print("| [1] Tambah Webtoon   |")
        print("| [2] Lihat Webtoon    |")
        print("| [3] Perbarui Webtoon |")
        print("| [4] Hapus Webtoon    |")
        print("| [5] Keluar           |")
        print("========================")
        CRUD = input("Masukkan pilihan (1-5): ")

        if CRUD == '1':
            judul = input("Masukkan judul webtoon: ")
            genre = input("Masukkan genre webtoon: ")
            tahun = int(input("Masukkan tahun terbit webtoon: "))
            rating = float(input("Masukkan rating webtoon: "))
            penulis = input("Masukkan penulis webtoon: ")
            webtoon_manager.create_webtoon(judul, genre, tahun, rating, penulis)
        elif CRUD == '2':
            webtoon_manager.read_webtoons()
        elif CRUD == '3':
            index = int(input("Masukkan index webtoon yang ingin diperbarui: "))
            judul = input("Masukkan judul baru webtoon: ")
            genre = input("Masukkan genre baru webtoon: ")
            tahun = int(input("Masukkan tahun baru terbit webtoon: "))
            rating = float(input("Masukkan rating baru webtoon: "))
            penulis = input("Masukkan penulis baru webtoon: ")
            webtoon_manager.update_webtoon(index, judul, genre, tahun, rating, penulis)
        elif CRUD == '4':
            index = int(input("Masukkan index webtoon yang ingin dihapus: "))
            webtoon_manager.delete_webtoon(index)
        elif CRUD == '5':
            print("Ditunggu Manhwa Barunya :D.")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih lagi.")

if __name__ == "__main__":
    main()
