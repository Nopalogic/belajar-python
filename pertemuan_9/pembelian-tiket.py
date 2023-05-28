print("LIST PENERBANGAN")
print("Kode Penerbangan       | Tujuan      | Harga tiket     ")
print("+ =======================+=============+================+")
print("| A01                    | AUS         | Rp. 5.000.000  |")
print("| B02                    | US          | Rp. 7.000.000  |")
print("| C03                    | JPN         | Rp. 7.500.000  |")
print("| D04                    | MLY         | Rp. 1.000.000  |")
print("+ =======================+=============+================+")

print()
nama = input("Nama Pembeli: ")
nomor = input("No. Hp: ")
asal = input("Asal Negara: ")
jurusan = input("Kode Tujuan Penerbangan: ")
tujuan = []
harga = []

if jurusan == "A01":
    tujuan.append("AUSTRALIA")
    harga = 5000000
elif jurusan == "B02":
    tujuan.append("UNITE STATE")
    harga = 7000000
elif jurusan == "B02":
    tujuan.append("JEPANG")
    harga = 7500000
elif jurusan == "B02":
    tujuan.append("MALAYSIA")
    harga = 1000000
else:
    tujuan.append("Kode tidak ditemukan.")

jumlah = int(input("Jumlah pembelian: "))
print()

if jumlah == 2:
    potongan = (jumlah*harga) * 0.1
elif jumlah == 3:
    potongan = (jumlah*harga) * 0.12
elif jumlah == 4:
    potongan = (jumlah*harga) * 0.25
else:
    potongan = 0
    
total = int(jumlah*harga)-potongan
pajak = 0.05
jumlahBayar = total + pajak

def line():
    print("=====================================================")

line()
print("PEMBELIAN TIKET")
line()
print("Nama Pembelian: ", nama)
print("No. Hp: ", nomor)
print("Asal Negara: ", asal)
print("Kode Negara: ", jurusan)
print("Negara Tujuan: ", tujuan)
print("Jumlah Beli: ", jumlah)
print()
print("Harga Tiket: ", harga)
print("Potongan: ", potongan)
print("PPN %: ", pajak)
line()
print("Pelunasan Pembayaran Tiket")
print("Jumlah bayar: ", jumlahBayar)
uang = int(input("Masukkan Pembayaran: "))
kembalian = uang - jumlahBayar
print("Kembalian: ", kembalian)
line()