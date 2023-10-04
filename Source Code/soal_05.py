from collections import deque

class AntrianBank:
    def __init__(self):
        self.Antrian = deque()

    def masuk(self, pelanggan):
        self.Antrian.append(pelanggan)
        print(f"{pelanggan} masuk ke dalam antrian bank.")

    def keluar(self):
        if not self.is_empty():
            melayani_pelanggan = self.Antrian.popleft()
            print(f"{melayani_pelanggan} keluar dari antrian bank.")
            return melayani_pelanggan
        else:
            print("Antrian bank kosong.")
            return None

    def is_empty(self):
        return len(self.Antrian) == 0

    def ukuran(self):
        return len(self.Antrian)

# Contoh penggunaan
bank = AntrianBank()

bank.masuk("Customer 1")
bank.masuk("Customer 2")
bank.masuk("Customer 3")

print("Ukuran Antrian Bank:", bank.ukuran())

served_customer = bank.keluar()
print("Pelanggan yang Dilayani:", served_customer)
print("Ukuran Antrian Bank:", bank.ukuran())

served_customer = bank.keluar()
print("Pelanggan yang Dilayani:", served_customer)
print("Ukuran Antrian Bank:", bank.ukuran())

served_customer = bank.keluar()
print("Pelanggan yang Dilayani:", served_customer)
print("Ukuran Antrian Bank:", bank.ukuran())

served_customer = bank.keluar()  # Mencoba mengeluarkan dari antrian kosong
