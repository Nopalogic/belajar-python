from datetime import datetime
import os
import random


def header():
    equalLine()
    print("CHRISTOPHER SALON".center(48))
    equalLine()

def dashLine():
    print('-'*48)

def equalLine():
    print('='*48)


customerModel = {
    'number': 0,
    'nama': 'nama',
    'services': [],
    'isMember': bool,
    'diskon': 0,
    'totalBiaya': 0,
    'metode': 'metode',
    'bayar': 0,
    'kembalian': 0,
    'mulai': ''
}

dataMenu = ['Potong Rambut','Pedicure','Hair Bleaching','Hair Colouring']
dataPegawai = ['Galih', 'Adit', 'Hamid','Asep','Cahyo']
customerQueue = []
queueNumber = 0

def newCustomer():
    try:
        os.system('cls')
        header()
        global queueNumber

        customer = dict.fromkeys(customerModel.keys())
        customer['number'] = queueNumber + 1
        queueNumber += 1
        customer['nama'] = input("Nama Pelanggan: ")

        services = []
        loop = True
        while(loop):
            loopAgain = True
            while(loopAgain):
                for index, menu in enumerate(dataMenu):
                    print(f"{index + 1}. {menu}")

                inputLayanan = int(input("Masukkan pilihan: "))

                if inputLayanan > len(dataMenu) or inputLayanan == 0:
                    print("pilihan tidak tersedia.\n")
                else:
                    loopAgain = False

            match inputLayanan:
                case 1:
                    layanan = 'Potong Rambut'
                    pegawai = dataPegawai[random.randint(0, len(dataPegawai) - 1)]
                    harga = 100000
                case 2:
                    layanan = 'Pedicure'
                    pegawai = dataPegawai[random.randint(0, len(dataPegawai) - 1)]
                    harga = 200000
                case 3:
                    layanan = 'Hair Bleaching'
                    pegawai = dataPegawai [random.randint(0, len(dataPegawai)-1)]
                    harga = 150000
                case 4: 
                    layanan = 'Hair Colouring'
                    pegawai = dataPegawai [random.randint(0, len(dataPegawai)-1)]
                    harga = 200000
                
            
            services.append([layanan, pegawai, harga])

            more = input('Ada lagi? [Y/N]: ')
            if more == 'y' or more == 'Y':
                loop = True
            else:
                loop = False

        member = input("Member [Y/N]: ")

        totalHarga = 0
        for harga in services:
            totalHarga += harga[2]

        isMember = False
        discount = 0
        if member == 'Y' or member == 'y':
            isMember = True
            discount += (totalHarga * 10 / 100)

        totalBiaya = totalHarga - discount

        customer['services'] = services
        customer['isMember'] = isMember
        customer['diskon'] = discount
        customer['totalBiaya'] = totalBiaya
        customer['mulai'] = datetime.now().replace(microsecond=0)

        customerQueue.append(customer)
        print('Success\n')
        input("Press Enter for go to menu...")
    except:
        queueNumber -= 1
        print('error')
# ==============================================

def payment():
    try:
        os.system('cls')
        header()
        if len(customerQueue) == 0:
            print("Antrian Kosong")
        else:
            search = int(input('Masukkan no antrean: '))
            customerNumber = [customer for customer in customerQueue if customer['number'] == search]

            for customer in customerNumber:
                customer['selesai'] = datetime.now().replace(microsecond=0)
                print(f"\nNama: {customer['nama']}")
                dashLine()
                for service in customer['services']:
                    print(f"{service[0].ljust(25)}{service[1].ljust(12)}{''.center(5)}{service[2]}")
                if customer['isMember'] == True:
                    print(f"DISCOUNT 10% (MEMBER){''.center(21)}-{int(customer['diskon'])}")
                dashLine()
                print(f"Total: {int(customer['totalBiaya'])}")

                loop = True
                while(loop):
                    print('\nPilih pembayaran')
                    print('1. TUNAI')
                    print('2. M-BANKING')
                    print('3. DEBIT')

                    pilih = int(input("Masukan pilihan pembayaran: "))

                    if pilih > 3 or pilih == 0:
                        print('Pembayaran tidak tersedia.')
                    else:
                        loop = False

                match pilih:
                    case 1:
                        metode = 'Tunai'
                        loop = True
                        while(loop):
                            bayar = int(input("Masukan jumlah bayar: "))

                            if bayar < customer['totalBiaya']:
                                print('Kurang')
                            else:
                                loop = False
                    case 2:
                        metode = 'Transfer'
                        bayar = customer['totalBiaya']
                    case 3:
                        metode = 'Debit'
                        bayar = customer['totalBiaya']

                kembalian = bayar - customer['totalBiaya']

                customer['metode'] = metode
                customer['bayar'] = bayar
                customer['kembalian'] = kembalian
                print('Success\n')
        input("Press Enter for go to menu...")
    except:
        print('error')
# ==============================================

def showQueue():
    os.system('cls')
    header()
    if len(customerQueue) == 0:
        print("Antrian Kosong")
    else:
        print("Antrian saat ini:")
        for customer in customerQueue:
            print(f"{customer['number']}. {customer['nama']}")

    input("Press Enter for go to menu...")
# ==============================================

def invoice(cashier):
    os.system('cls') 
    header()
    if len(customerQueue) != 0:
        search = int(input('Masukkan no antrean: '))
        
        customerNumber = [customer for customer in customerQueue if customer['number'] == search]

        os.system('cls') 
        header()
        for customer in customerNumber:
            print(f"Nama Tamu\t: {customer['nama']}")
            print(f"No. Antre\t: {customer['number']}")
            print(f"Mulai\t\t: {customer['mulai']}")
            print(f"Selesai\t\t: {customer['selesai']}")

            member = 'CHRISTOPER' if customer['isMember'] else 'PELANGGAN'

            print(f"Member\t\t: {member}")
            print(f"Kasir\t\t: {cashier}")
            dashLine()

            for service in customer['services']:
                print(f"{service[0].ljust(25)}{service[1].ljust(12)}{''.center(5)}{service[2]}")

            if customer['isMember'] == True:
                print(f"DISCOUNT 10% (MEMBER){''.center(21)}-{int(customer['diskon'])}")

            dashLine()
            print(f"Total\t\t: {int(customer['totalBiaya'])}")

            if customer['metode'] == 'Tunai': 
                bayar = customer['bayar']
                kembalian = customer['kembalian']
            else:
                bayar = customer['metode']
                kembalian = ''
            
            print(f"Bayar\t\t: {bayar}")
            print(f"Kembalian\t: {kembalian}")
            equalLine()
        customerQueue.pop(0)
    else:
        print('Antrean kosong\n')
    input("Press Enter for go to menu...")
# ==============================================

header()
kasir = input("Kasir: ")
while True:
    os.system('cls')
    header()
    print(
    """
    Menu
    1. Tambah Customer
    2. Pembayaran
    3. Tampil Antrean
    4. Cetak Invoice
    5. Keluar
    """
    )

    choose = int(input('Masukan pilihan: '))

    match choose:
        case 1:
            newCustomer()
        case 2:
            payment()
        case 3:
            showQueue()
        case 4:
            invoice(kasir)
        case 5:
            print('Dosen Pengampu: Bias Yulisa Geni, S.Kom., M.Kom.')
            print('Naufal Adhi Ramadhan 411221126')
            print('Galih Dika Saputra 411221118')
            print('Muhammad Yusuf Hiqmal Miko 411221124')
            break
        case _:
            print('Pilihan tidak tersedia.')
            input("Press Enter for go to menu...")