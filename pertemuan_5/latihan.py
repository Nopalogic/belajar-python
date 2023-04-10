print("             AYAM GORENG MANTUL")
print("============================================")
print("Kode           Jenis Potong            Harga")
print("============================================")
print("D              Dada                    12000")
print("P              Paha                    10000")
print("S              Sayap                   11000")
print("============================================")

banyak_jenis = int(input("Masukkan banyak jenis: "))
kode_potong = []
banyak_potong = []
jenis_potong = []
harga = []
jumlah = []
i = 0

while i < banyak_jenis:
    print("Jenis ke-",i+1)

    kode_potong.append(input("Kode potong [D/P/S]: "))
    banyak_potong.append(int(input("Banyak potong: ")))

    if kode_potong[i] == "D" or kode_potong[i] == "d":
        jenis_potong.append("Dada")
        harga.append("12000")
        jumlah.append(banyak_potong[i]*int("12000"))
    elif kode_potong[i] == "P" or kode_potong[i] == "p":
        jenis_potong.append("Paha")
        harga.append("10000")
        jumlah.append(banyak_potong[i]*int("10000"))
    elif kode_potong[i] == "S" or kode_potong[i] == "s":
        jenis_potong.append("Sayap")
        harga.append("11000")
        jumlah.append(banyak_potong[i]*int("11000"))
    else:
        jenis_potong.append("KODE SALAH")
        harga.append('0')
        jumlah.append(banyak_potong[i]*int("0"))
    i += 1

jumlah_bayar = 0
a = 0

print("             AYAM GORENG MANTUL")
print("+ ========================================================================== +")
print("|  No  |  Jenis Potong   |  Harga Satuan   |  Banyak Beli   |  Jumlah Harga  |")
print("+ ========================================================================== +")

while a < banyak_jenis:
    jumlah_bayar =  jumlah_bayar + jumlah[a]
    print("|  %i  |       %s       |      %s      |        %i        |      %i      |" % (a+1, jenis_potong[a], harga[a], banyak_potong[a], jumlah[a]))
    a += 1

pajak = jumlah_bayar * 10 / 100
total_bayar = jumlah_bayar + pajak

print("+ ========================================================================== +")
print(f"                                                 Jumlah bayar Rp.{jumlah_bayar}")
print(f"                                                 Pajak 10%    Rp.{pajak}")
print(f"                                                 Total bayar  Rp.{total_bayar}")
print("+ ========================================================================== +")
