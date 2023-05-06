header = "INPUT GAJI KARYAWAN".center(44,"=")
print(header)
jumlahKaryawan= int(input("Masukkan jumlah karyawan\t: "))
bulan = int(input("Masukkan bulan [1-12]\t\t: "))

listKaryawan = []

i = 0
while i < jumlahKaryawan:
    print(f"\nData karyawan ke-{i+1}")
    namaKaryawan = input("Nama Karyawan\t\t: ")
    nipKaryawan = int(input("NIP Karyawan\t\t: "))
    kodeJabatan = int(input("Kode Jabatan [1/2]\t: "))
    kodeStatus = input("Kode Status [M/S]\t: ")
    i += 1

    if kodeJabatan == 1:
        jabatan = "Administrasi"
        gajiPokok = 1700000
    elif kodeJabatan == 2:
        jabatan = "Operasional"
        gajiPokok = 2000000
    else:
        print(f"{kodeJabatan}: kode tidak ditemukan.")
        break

    if kodeStatus == "M" or kodeStatus == "m":
        status = "Menikah"
        if kodeJabatan == 1:
            tunjangan = 500000
        else:
            tunjangan = 700000
    elif kodeStatus == "S" or kodeStatus == "s":
        status = "Single"
        if kodeJabatan == 1:
            tunjangan = 250000
        else:
            tunjangan = 350000
    else:
        print(f"{kodeStatus}: kode tidak ditemukan.")
        break

    totalGaji = gajiPokok + tunjangan

    karyawanBaru = [nipKaryawan, namaKaryawan, jabatan, status, gajiPokok, tunjangan, totalGaji]
    listKaryawan.append(karyawanBaru)

print("\n                                      DAFTAR GAJI KARYAWAN")
print("                                             PT. BEYEGE")
print(f" Bulan = {bulan}")
print("+ ============================================================================================================ +")
print("|  No  |  NIP Karywan  |  Nama Karyawan  |    Jabatan    |  Status  |  Gaji Pokok  |  Tunjugan  |  Total Gaji  |")
print("+ ============================================================================================================ +")

for indeks, karyawan in enumerate(listKaryawan):
    print("|  %i   |      %i      |     %s      |  %s  |  %s  |    %i   |   %i   |    %i   |" % (indeks+1, karyawan[0], karyawan[1], karyawan[2], karyawan[3], karyawan[4], karyawan[5], karyawan[6]))

total = 0
for karyawan in listKaryawan:
    total += karyawan[6]

print("+ ============================================================================================================ +")
print(f"                                                                              Total Gaji Karyawan Rp.{total}")


