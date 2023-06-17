# # Kasus 1
# print("ini adalah program pembagian")

# while True:
#     try:
#         # import panda
#         pembilang = int(input("masukan angka pembilang: "))
#         penyebut = int(input("masukan angka penyebut: "))
#         hasil = pembilang / penyebut
#         break
#     except ValueError:
#         print("yang anda masukan bukan angka\n")
#     except ZeroDivisionError:
#         print("angka pembilang yang anda masukan adalah nol, pilih yang lain ya bro/sist\n")
#     except ImportError:
#         print("gak ada modulnya bro")
#     except Exception as err:
#         print(err)

# """
#     type of exception errors:
#     1. IOError
#     2. ImportError
#     3. ValueError
#     4. Division by zero
#     5. KeyboardInterupted
#     6. EOFError
# """

# print("berhasil, hasil pembagian adalah:", hasil)
# print()

# # Kasus 2
# ukuranSepatu = input("Berapa Ukuran Sepatu Anda? ")

# try:
#     ukuranSepatu = int(ukuranSepatu)

#     print("Terimakasih , ukuran sepatu anda adalah", ukuranSepatu)
#     print("Kami akan mencari ukuran sepatu yang sesuai untuk anda")
# except:
#     print("Maaf, ukuran yang anda masukkan tidak valid")
# print()

# Kasus 3
# from datetime import datetime as dtm

# tanggalValid = False

# while not tanggalValid:
#     dtInput = input('Masukkan tanggal lahir anda dengan format seperti contoh berikut: DD MM YYYY\n')

#     try:
#         tanggalLahir = dtm.strptime(dtInput, '%d %m %Y')
#         tanggalValid = True
#         timestamp = dtm.now().replace(microsecond=0)
#     except:
#         print('Anda memasukkan nilai dengan format yang salah')

# print(f"{tanggalLahir}\n{timestamp}")
