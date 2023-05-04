# from datetime import date


# if 1 kondisi
# a = 31
# b = 31
# if a != b:
#     print("Tereksekusi!")

# print("Hallo")

# if 2 kondisi
# umur = int(input("Masukkan nilai: "))
# if umur >= 17:
#     print(f"Umur anda {umur}, bikin KTP")
# else:
#     print(f"Umur anda {umur}, gaboleh bikin KTP dulu")

# input_tanggal = input("Masukkan angka dalam format YYYY-MM-DD: ")
# tahun, bulan, tanggal = map(int, input_tanggal.split('-'))
# tanggal1 = date(tahun, bulan, tanggal)
# umur = date.today().year - tanggal1.year

# print(f"Umur anda sekarang: {umur} tahun")
# if(umur >= 17):
#     print("Anda harus buat KTP")
# else:
#     print("Anda belum bisa buat KTP")
    
# if umur >= 17:
#     if tanggal1.day == date.today().day and tanggal1.month == date.today().month:
#       print("Anda mendapatkan diskon 90%")
#     else:
#       print("Anda mendapatkan diskon 50%")
# elif umur <= 5:
#     print("Anda mendapatkan diskon 20%")
# else:
#    print("Gak dapet diskon")
    
# if 3 kondisi
nilai =  int(input("Berapa nilai Anda: "))

if nilai >= 90:
    grade = "A"
elif nilai >= 80:
    grade =  "B+"
elif nilai >= 70:
    grade =  "B"
elif nilai >=60:
    grade =  "C+"
else:
    grade = "D"

print(f"Grade: {grade}")