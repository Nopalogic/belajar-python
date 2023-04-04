nama = input("Masukkan nama: ")
nim = int(input("Masukkan nim: "))
smstr = input("Masukkan semester: ")
matkul = input("Masukkan mata kuliah: ")
nilai = int(input("Masukkan nilai: "))

if nilai <= 39.99:
    grade = "E"
    bobot = 0
elif nilai <= 54.99:
    grade = "D"
    bobot = 1.00
elif nilai <= 59.99:
    grade = "C"
    bobot = 2.00
elif nilai <= 64.99:
    grade = "C+"
    bobot = 2.30
elif nilai <= 69.99:
    grade = "B-"
    bobot = 2.70
elif nilai <= 74.99:
    grade = "B"
    bobot = 3.00
elif nilai <= 79.99:
    grade = "B+"
    bobot = 3.30
elif nilai <= 84.99:
    grade = "A-"
    bobot = 3.70
else:
    grade = "A"
    bobot = 4.00

print(f"""
Nama: {nama}
NIM: {nim}
Semester: {smstr}
Mata Kuliah: {matkul}
Nilai: {nilai} | Grade: {grade} | Bobot Nilai: {bobot}
""")