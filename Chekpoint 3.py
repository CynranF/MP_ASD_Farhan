class WebtoonNode:
    def __init__(self, judul, genre, tahun, rating, penulis):
        self.judul = judul
        self.genre = genre
        self.tahun = tahun
        self.rating = rating
        self.penulis = penulis
        self.next = None

class WebtoonLinkedList:
    def __init__(self):
        self.head = None

    def tambah_webtoon_di_awal(self, judul, genre, tahun, rating, penulis):
        webtoon_baru = WebtoonNode(judul, genre, tahun, rating, penulis)
        webtoon_baru.next = self.head
        self.head = webtoon_baru
        print(f"Webtoon '{judul}' berhasil ditambahkan di awal!")

    def tambah_webtoon_di_akhir(self, judul, genre, tahun, rating, penulis):
        webtoon_baru = WebtoonNode(judul, genre, tahun, rating, penulis)
        if not self.head:
            self.head = webtoon_baru
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = webtoon_baru
        print(f"Webtoon '{judul}' berhasil ditambahkan di akhir!")

    def tambah_webtoon_di_antara(self, judul, genre, tahun, rating, penulis, posisi):
        if posisi <= 0:
            self.tambah_webtoon_di_awal(judul, genre, tahun, rating, penulis)
        elif posisi > self.hitung_jumlah_webtoon():
            self.tambah_webtoon_di_akhir(judul, genre, tahun, rating, penulis)
        else:
            webtoon_baru = WebtoonNode(judul, genre, tahun, rating, penulis)
            current = self.head
            for _ in range(posisi - 2):
                current = current.next
            webtoon_baru.next = current.next
            current.next = webtoon_baru
            print(f"Webtoon '{judul}' berhasil ditambahkan di posisi {posisi}!")

    def hapus_webtoon_di_awal(self):
        if self.head is None:
            print("Belum ada webtoon yang tersedia.")
        else:
            deleted_webtoon = self.head
            self.head = self.head.next
            print(f"Webtoon '{deleted_webtoon.judul}' berhasil dihapus di awal!")

    def hapus_webtoon_di_akhir(self):
        if self.head is None:
            print("Belum ada webtoon yang tersedia.")
        elif self.head.next is None:
            deleted_webtoon = self.head
            self.head = None
            print(f"Webtoon '{deleted_webtoon.judul}' berhasil dihapus di akhir!")
        else:
            current = self.head
            while current.next.next:
                current = current.next
            deleted_webtoon = current.next
            current.next = None
            print(f"Webtoon '{deleted_webtoon.judul}' berhasil dihapus di akhir!")

    def hapus_webtoon_di_antara(self, posisi):
        if self.head is None:
            print("Belum ada webtoon yang tersedia.")
        elif posisi <= 0:
            print("Posisi harus lebih besar dari 0.")
        elif posisi == 1:
            self.hapus_webtoon_di_awal()
        elif posisi >= self.hitung_jumlah_webtoon():
            print("Posisi melebihi jumlah webtoon yang ada.")
        else:
            current = self.head
            for _ in range(posisi - 2):
                current = current.next
            deleted_webtoon = current.next
            current.next = current.next.next
            print(f"Webtoon '{deleted_webtoon.judul}' berhasil dihapus di antara node!")

    def tampilkan_daftar_webtoon(self):
        current = self.head
        if not current:
            print("Belum ada webtoon yang tersedia.")
        else:
            print("Daftar Webtoon:")
            nomor = 1
            while current:
                print(f"{nomor}. {current.judul} ({current.tahun}), Genre: {current.genre}, Rating: {current.rating}, Penulis: {current.penulis}")
                current = current.next
                nomor += 1

    def hitung_jumlah_webtoon(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next
        return count

    def update_webtoon(self, posisi, judul, genre, tahun, rating, penulis):
        if posisi <= 0 or posisi > self.hitung_jumlah_webtoon():
            print("Posisi tidak valid untuk pembaruan.")
            return
        current = self.head
        for _ in range(posisi - 1):
            current = current.next
        current.judul = judul
        current.genre = genre
        current.tahun = tahun
        current.rating = rating
        current.penulis = penulis
        print(f"Webtoon pada posisi {posisi} berhasil diperbarui!")

    def lihat_berdasarkan_nama_atas(self):
        sorted_head = self.quick_sort_by_name(self.head, ascending=True)
        self.tampilkan_daftar_setelah_sort(sorted_head, "Daftar Webtoon berdasarkan Nama (A-Z)")

    def lihat_berdasarkan_nama_bawah(self):
        sorted_head = self.quick_sort_by_name(self.head, descending=True)
        self.tampilkan_daftar_setelah_sort(sorted_head, "Daftar Webtoon berdasarkan Nama (Z-A)")

    def lihat_berdasarkan_rating_atas(self):
        sorted_head = self.quick_sort_by_rating(self.head, ascending=True)
        self.tampilkan_daftar_setelah_sort(sorted_head, "Daftar Webtoon berdasarkan Rating (Tertinggi)")

    def lihat_berdasarkan_rating_bawah(self):
        sorted_head = self.quick_sort_by_rating(self.head, descending=True)
        self.tampilkan_daftar_setelah_sort(sorted_head, "Daftar Webtoon berdasarkan Rating (Terendah)")

    def quick_sort_by_name(self, head, ascending=True, descending=False):
        if not head or not head.next:
            return head

        pivot = head
        less_than_pivot_head = less_than_pivot_tail = WebtoonNode(None, None, None, None, None)
        greater_than_pivot_head = greater_than_pivot_tail = WebtoonNode(None, None, None, None, None)

        current = head.next
        while current:
            if (current.judul.lower() <= pivot.judul.lower()) if ascending else (current.judul.lower() >= pivot.judul.lower()):
                less_than_pivot_tail.next = current
                less_than_pivot_tail = less_than_pivot_tail.next
            else:
                greater_than_pivot_tail.next = current
                greater_than_pivot_tail = greater_than_pivot_tail.next

            current = current.next

        less_than_pivot_tail.next = greater_than_pivot_tail.next = None

        sorted_less_than_pivot = self.quick_sort_by_name(less_than_pivot_head.next, ascending=ascending)
        sorted_greater_than_pivot = self.quick_sort_by_name(greater_than_pivot_head.next, ascending=ascending)

        pivot.next = sorted_greater_than_pivot
        if sorted_less_than_pivot:
            return sorted_less_than_pivot
        else:
            return pivot

    def quick_sort_by_rating(self, head, ascending=True, descending=False):
        if not head or not head.next:
            return head

        pivot = head
        less_than_pivot_head = less_than_pivot_tail = WebtoonNode(None, None, None, None, None)
        greater_than_pivot_head = greater_than_pivot_tail = WebtoonNode(None, None, None, None, None)

        current = head.next
        while current:
            if (current.rating <= pivot.rating) if ascending else (current.rating >= pivot.rating):
                less_than_pivot_tail.next = current
                less_than_pivot_tail = less_than_pivot_tail.next
            else:
                greater_than_pivot_tail.next = current
                greater_than_pivot_tail = greater_than_pivot_tail.next

            current = current.next

        less_than_pivot_tail.next = greater_than_pivot_tail.next = None

        sorted_less_than_pivot = self.quick_sort_by_rating(less_than_pivot_head.next, ascending=ascending)
        sorted_greater_than_pivot = self.quick_sort_by_rating(greater_than_pivot_head.next, ascending=ascending)

        pivot.next = sorted_greater_than_pivot
        if sorted_less_than_pivot:
            return sorted_less_than_pivot
        else:
            return pivot

    def tampilkan_daftar_setelah_sort(self, sorted_head, message):
        current = sorted_head
        print(f"\n{message}:")
        nomor = 1
        while current:
            print(f"{nomor}. {current.judul} ({current.tahun}), Genre: {current.genre}, Rating: {current.rating}, Penulis: {current.penulis}")
            current = current.next
            nomor += 1

def main():
    webtoon_list = WebtoonLinkedList()

    while True:
        print("\n========= Menu =========")
        print("| [1] Tambah Webtoon      |")
        print("| [2] Hapus Webtoon       |")
        print("| [3] Lihat Webtoon       |")
        print("| [4] Update Webtoon      |")
        print("| [5] Keluar              |")
        print("========================")
        pilihan = input("Masukkan pilihan (1-5): ")

        if pilihan == '1':
            print("\n========= Pilihan Tambah Webtoon =========")
            print("| [1] Tambah Webtoon di Awal               |")
            print("| [2] Tambah Webtoon di Akhir              |")
            print("| [3] Tambah Webtoon di Antara Node        |")
            print("==========================================")
            pilihan_tambah = input("Masukkan pilihan tambah webtoon (1-3): ")
            judul = input("Masukkan judul webtoon: ")
            genre = input("Masukkan genre webtoon: ")
            tahun = int(input("Masukkan tahun terbit webtoon: "))
            rating = float(input("Masukkan rating webtoon: "))
            penulis = input("Masukkan penulis webtoon: ")

            if pilihan_tambah == '1':
                webtoon_list.tambah_webtoon_di_awal(judul, genre, tahun, rating, penulis)
            elif pilihan_tambah == '2':
                webtoon_list.tambah_webtoon_di_akhir(judul, genre, tahun, rating, penulis)
            elif pilihan_tambah == '3':
                posisi = int(input("Masukkan posisi penambahan webtoon: "))
                webtoon_list.tambah_webtoon_di_antara(judul, genre, tahun, rating, penulis, posisi)
            else:
                print("Pilihan tidak valid.")
        elif pilihan == '2':
            print("\n========= Pilihan Hapus Webtoon =========")
            print("| [1] Hapus Webtoon di Awal                |")
            print("| [2] Hapus Webtoon di Akhir               |")
            print("| [3] Hapus Webtoon di Antara Node         |")
            print("==========================================")
            pilihan_hapus = input("Masukkan pilihan hapus webtoon (1-3): ")

            if pilihan_hapus == '1':
                webtoon_list.hapus_webtoon_di_awal()
            elif pilihan_hapus == '2':
                webtoon_list.hapus_webtoon_di_akhir()
            elif pilihan_hapus == '3':
                print("\n")
                webtoon_list.tampilkan_daftar_webtoon()
                print("\n")
                posisi = int(input("Masukkan nomor posisi webtoon yang ingin dihapus: "))
                webtoon_list.hapus_webtoon_di_antara(posisi)
            else:
                print("Pilihan tidak valid.")
        elif pilihan == '3':
            print("\n========= Pilihan Lihat Webtoon =========")
            print("| [1] Lihat Semua Webtoon                 |")
            print("| [2] Lihat berdasarkan Nama (A-Z)        |")
            print("| [3] Lihat berdasarkan Nama (Z-A)        |")
            print("| [4] Lihat berdasarkan Rating (Tertinggi)|")
            print("| [5] Lihat berdasarkan Rating (Terendah) |")
            print("| [6] Kembali                             |")
            print("==========================================")
            pilihan_lihat = input("Masukkan pilihan lihat webtoon (1-6): ")

            if pilihan_lihat == '1':
                print("\n")
                webtoon_list.tampilkan_daftar_webtoon()
                print("\n")
            elif pilihan_lihat == '2':
                webtoon_list.lihat_berdasarkan_nama_atas()
            elif pilihan_lihat == '3':
                webtoon_list.lihat_berdasarkan_nama_bawah()
            elif pilihan_lihat == '4':
                webtoon_list.lihat_berdasarkan_rating_atas()
            elif pilihan_lihat == '5':
                webtoon_list.lihat_berdasarkan_rating_bawah()
            elif pilihan_lihat == '6':
                continue
            else:
                print("Pilihan tidak valid.")
        elif pilihan == '4':
            print("\n")
            webtoon_list.tampilkan_daftar_webtoon()
            print("\n")
            posisi = int(input("Masukkan nomor posisi webtoon yang ingin diperbarui: "))
            judul = input("Masukkan judul baru webtoon: ")
            genre = input("Masukkan genre baru webtoon: ")
            tahun = int(input("Masukkan tahun baru terbit webtoon: "))
            rating = float(input("Masukkan rating baru webtoon: "))
            penulis = input("Masukkan penulis baru webtoon: ")
            webtoon_list.update_webtoon(posisi, judul, genre, tahun, rating, penulis)
        elif pilihan == '5':
            print("Terima kasih! Sampai jumpa!")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih lagi.")

if __name__ == "__main__":
    main()
