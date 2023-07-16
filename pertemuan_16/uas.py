import pprint

daftarPasien = []

paseinModel = {
    'nama': '',
    'alamat': '',
    'jenisKelamin': '',
    'bpjs': bool,
    'layanan': 0,
    'biaya': 0,
    'dokter': 0,
    'lamaWaktu': 0,
    'totalBiaya': 0,
}
pasien = dict.fromkeys(paseinModel.keys())

daftarLayanan = [
    ['Pelayanan Rawat Jalan / Poliklinik', 250_000],
    ['Pelayanan Rawat Inap', 500_000],
    ['Pelayanan Gawat Darurat', 750_000],
    ['Pelayanan Kanker Terpadu', 800_000],
    ['Pelayanan Kedokteran Nuklir', 900_000],
    ['Pelayanan Ibu dan Anak Terpadu', 600_000],
    ['Pelayanan Rawat Intensif Terpadu', 1_000_000],
    ['Pelayanan Bedah Sentral dan Anastesi', 2_000_000],
]

dafterDokter = [
    "dr. Alberto",
    "dr. Alexa",
    "dr. Brian",
    "dr. Adelwis",
    "dr. Bonerto",
    "dr. Glenn",
    "dr. Dilan",
    "dr. Brillian",
    "dr. Kawisha",
]

def pasienBaru():
    pasien['nama'] = input("Masukkan nama pasien: ")
    pasien['alamat'] = input("Masukkan alamat: ")
    pasien['jenisKelamin'] = input("Masukkan jenis kelamin: ")

    pilih = input("Apakah anda pengguna BPJS? [Y/N]: ")
    bpjs = False
    if pilih == "Y" or pilih == "y":
        bpjs = True

    pasien['bpjs'] = bpjs

    print("Layanan")
    for index, layanan in enumerate(daftarLayanan):
        print(f"{index + 1}. {layanan[0].ljust(40)}{str(layanan[1]).rjust(7)}")

    loop = True
    while loop:
        pilih = int(input("Pilih layanan: "))

        match pilih:
            case 1:
                layanan = daftarLayanan[0][0]
                biaya = daftarLayanan[0][1]
                loop = False
            case 2:
                layanan = daftarLayanan[1][0]
                biaya = daftarLayanan[1][1]
                loop = False
            case 3:
                layanan = daftarLayanan[2][0]
                biaya = daftarLayanan[2][1]
                loop = False
            case 4:
                layanan = daftarLayanan[3][0]
                biaya = daftarLayanan[3][1]
                loop = False
            case 5:
                layanan = daftarLayanan[4][0]
                biaya = daftarLayanan[4][1]
                loop = False
            case 6:
                layanan = daftarLayanan[5][0]
                biaya = daftarLayanan[5][1]
                loop = False
            case 7:
                layanan = daftarLayanan[6][0]
                biaya = daftarLayanan[6][1]
                loop = False
            case 8:
                layanan = daftarLayanan[7][0]
                biaya = daftarLayanan[7][1]
                loop = False
            case _:
                print("Layanan tidak tersedia.")

    pasien['layanan'] = layanan
    pasien['biaya'] = biaya

    print("Layanan")
    for index, dokter in enumerate(dafterDokter):
        print(f"{index + 1}. {dokter}")

    loop = True
    while loop:
        pilih = int(input("Pilih dokter: "))

        match pilih:
            case 1:
                dokter = dafterDokter[0]
                loop = False
            case 2:
                dokter = dafterDokter[1]
                loop = False
            case 3:
                dokter = dafterDokter[2]
                loop = False
            case 4:
                dokter = dafterDokter[3]
                loop = False
            case 5:
                dokter = dafterDokter[4]
                loop = False
            case 6:
                dokter = dafterDokter[5]
                loop = False
            case 7:
                dokter = dafterDokter[6]
                loop = False
            case 8:
                dokter = dafterDokter[7]
                loop = False
            case _:
                print("Pilihan tidak tersedia")

    pasien['dokter'] = dokter

    lamaWaktu = int(input("Masukkan lama waktu: "))

    if(lamaWaktu == 1):
        biayaPelayanan = 100_000
    elif(lamaWaktu == 2):
        biayaPelayanan = 150_000
    elif(lamaWaktu > 3):
        biayaPelayanan = 250_000
    elif(lamaWaktu > 7):
        biayaPelayanan = 600_000

    if bpjs == True:
        biayaPelayanan = 0

    pasien['lamaWaktu'] = lamaWaktu
    pasien['biayaPelayanan'] = biayaPelayanan

    totalBiaya = (pasien['biaya'] * lamaWaktu) + biayaPelayanan
    pasien['totalBiaya'] = totalBiaya


    daftarPasien.append(pasien)

pasienBaru()
pprint.pprint(daftarPasien)

# def jadwalCheckup():
