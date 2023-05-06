listBuku = []

header = "INPUT DATA BUKU".center(32, "=")
while True:
    print(header)
    judulBuku = input("Inputkan judul buku\t\t: ")
    penulis = input("Inputkan nama penulis buku\t: ")
    jumlahBeli = int(input("Inputkan jumlah beli\t\t: "))
    hargaBuku = int(input("Inputkan harga buku\t\t: "))

    totalPerBuku = jumlahBeli * hargaBuku

    bukuBaru = [judulBuku, penulis, jumlahBeli, hargaBuku, totalPerBuku]
    listBuku.append(bukuBaru)

    tambahLagi = input("\nApakah anda ingin menambahkan buku lagi? [Y/N]: ")

    if tambahLagi == "Y" or tambahLagi == "y":
        print()
        continue
    elif tambahLagi == "N" or tambahLagi == "n":
        break
    else:
        print(f"{tambahLagi}: perintah tidak ditemukan.")
        break

print("\n")
header = "DATA BUKU".center(32, "=")
print(header)
for indeks, buku in enumerate(listBuku):
    print(f"| {indeks+1} | {buku[0]} | {buku[1]} | {buku[2]} | {buku[3]} | {buku[4]} |")
print("="*32)

totalHarga = 0
for buku in listBuku:
    totalHarga += buku[4]

print("Total harga\t:", totalHarga)

bayar = int(input("Bayar\t\t: "))
if bayar >= totalHarga:
    kembalian = bayar - totalHarga
    print("Kembalian\t:", kembalian)
else:
    print("KURANG, BLOK")
