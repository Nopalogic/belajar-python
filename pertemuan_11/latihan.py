import os, random, datetime, string

template = {
    'nama': 'nama',
    'nim': '00000000',
    'sks_lulus': 0,
    'lahir': datetime.datetime(1111, 1, 11)
}

dataMahasiswa = {}

while True:
    os.system('cls')
    print(f"{'SELAMAT DATANG':^20}")
    print(f"{'DATA MAHASISWA':^20}")
    print('-'*20)

    mahasiswa = dict.fromkeys(template.keys())
    mahasiswa['nama'] = input("Nama Mahasiswa: ")
    mahasiswa['nim'] = input("NIM Mahasiswa: ")
    mahasiswa['sks_lulus'] = input("SKS Lulus: ")
    TAHUN_LAHIR = int(input("Tahun lahir (YYYY): "))
    BULAN_LAHIR = int(input("Bulan lahir (1-12): "))
    TANGGAL_LAHIR = int(input("Tanggal lahir (1-31): "))
    mahasiswa['lahir'] = datetime.datetime(TAHUN_LAHIR, BULAN_LAHIR, TANGGAL_LAHIR)

    KEY = ''.join((random.choice(string.ascii_lowercase) for i in range(6)))
    dataMahasiswa.update({KEY:mahasiswa})    

    print(f"\n{'KEY':<10}{'Nama':<24}{'NIM':<8}{'SKS Lulus':<10}{'Tanggal Lahir':<8}")
    print('-'*20)

    for mahasiswa in dataMahasiswa:
        KEY = mahasiswa

        NAMA = dataMahasiswa[KEY]['nama']
        NIM = dataMahasiswa[KEY]['nim']
        SKS = dataMahasiswa[KEY]['sks_lulus']
        LAHIR = dataMahasiswa[KEY]['lahir'].strftime("%x")

        print(f"\n{KEY:<10}{NAMA:<24}{NIM:<8}{SKS:<10}{LAHIR:<8}")

    print()
    is_done = input("Mau tambah lagi? [y/n]")
    if is_done == 'n':
        break
    
    