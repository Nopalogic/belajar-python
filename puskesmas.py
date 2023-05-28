
def header():
    print("""
    ++======================++
    || PUSKESMAS KARYA MAJU ||
    ++======================++""")

def footer():
    print("""
    ++=============================================================++
    || Terima Kasih Telah Memakai Layanan Kami Semoga Lekas Sembuh ||
    ++=============================================================++
    """)

header()
print("""
    + ====================== +
    |   Pendaftaran Pasien   |
    + ====================== +""")

print("""
    Apakah anda memiliki bpjs?
    1. Ya
    2. Tidak""")
isMember = int(input("Pilihan anda: "))

if isMember != 1 and isMember != 2:
    print("Error")
elif isMember == 2:
    print("Pembayaran pribadi (Cash/M-Banking/Debit)")

print("Silahkan masukkan data dengan benar.")
nama = input("Nama\t\t: ")
alamat = input("Alamat\t\t: ")
nik = int(input("NIK\t\t: "))
gender = input("Jenis kelamin\t: ")
noTelpon = int(input("Nomor telpon\t: "))

if isMember == 1:
    idMember = int(input("Masukkan nomor kartu bpjs: "))
    statusAccount = int(input("-  : "))

print("""
    + =============================== +
    | Data Pasien di Buku Rekap Medis |
    + =============================== +""")

print("Nama: ", nama)
print("NIK: ", nik)