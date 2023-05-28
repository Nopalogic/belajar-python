print("="*42)
header = "UJIAN TENGAH SEMESTER".center(42)
print(header)
print("Nama : Naufal Adhi Ramadhan")
print("="*42)

nisn = int(input("Masukkan NISN : "))
nama = input("Masukkan Nama Lengkap : ")
noTelpon = int(input("Masukkan No. Hp : "))
alamat = input("Masukkan Alamat Domisili : ")
fakultas = input("Pilih Fakultas [FTI/FBIS] : ")
jurusan = input("Pilih Jurusan [TI/TE/TS/TM/MJ/AKT/BING/ILKOM] : ")
kelas = input("Pilih Kelas [Reguler 1/Reguler 2] : ")

if jurusan == "TI" or jurusan == "ti":
    jurusan = "Teknik Informatika"
    biaya = 4900000
elif jurusan == "TE" or jurusan == "te":
    jurusan = "Teknik Elektro"
    biaya = 4600000
elif jurusan == "TS" or jurusan == "ts":
    jurusan = "Teknik Sipil"
    biaya = 4800000
elif jurusan == "TM" or jurusan == "tm":
    jurusan = "Teknik Mesin"
    biaya = 4700000
elif jurusan == "MJ" or jurusan == "mj":
    jurusan = "Manajemen"
    biaya = 4200000
elif jurusan == "AKT" or jurusan == "akt":
    jurusan = "Akuntansi"
    biaya = 4150000
elif jurusan == "BING" or jurusan == "bing":
    jurusan = "Bahasa Inggris"
    biaya = 4100000
elif jurusan == "ILKOM" or jurusan == "ilkom":
    jurusan = "Ilmu Komunikasi"
    biaya = 4250000
else:
    print(f'{jurusan}: jurusan tidak ditemukan')

if kelas == "Reguler 2" or kelas == "reguler 2":
    biayaTambahan = 700000  
    total = biaya + biayaTambahan
else:
    biayaTambahan = 0

print("="*42)
header = "Formulir Pendaftaran Mahasiswa".center(42)
print("="*42)
print("NISN\t\t: ", nisn)
print("Nama Lengkap\t: ", nama)
print("No. Hp\t\t: ", noTelpon)
print("Alamat\t\t: ", alamat)
print("Jurusan\t\t: ", jurusan)
print(f"Biaya\t\t:  Rp.{biaya}")
print("Kelas\t\t: ", kelas)
print(f"Biaya Tambahan\t:  Rp.{biayaTambahan}")
print(f"Jumlah Biaya\t:  Rp.{total}")
print("="*42)