listMataKuliah = ["Algoritma dan Pemrograman 2", "Struktur Data dan Algoritma", "Sistem Keamanan Informasi"]

for x in listMataKuliah:
  print(x)

listUsedFor = [i**3 for i in range(10)]
print(listUsedFor)

listUsedForIf = [i for i in range(10) if i != 5]
print(listUsedForIf)

listUsedForIf = [i for i in range(10) if i%2 == 0]
print(listUsedForIf)

listUsedForIf = [i for i in range(10) if i%2 != 0]
print(listUsedForIf)

dataAngka = [10,12,10,15,15,64,12,46,74,71,64,23,72,23]
print(f"Data angka = \n {dataAngka}")

jumlahData = dataAngka.count(10)
print(f"Jumlah angka 10 = {jumlahData}")

dataMerkMobil = ["Honda", "Mazda", "Toyota", "Nissan"]
# print(f"Data merk = {dataMerkMobil}")
indeksHonda = dataMerkMobil.index("Honda")
print(f"Index merk honda adaalah {indeksHonda}")

for indeks, merkMobil in enumerate(dataMerkMobil):
    print(f"{indeks}: {merkMobil}")

# sorting list
print(f"Data angka = \n {dataAngka}")
dataAngka.sort()
print(f"Data angka yang telah di sort = \n {dataAngka}")

print(f"Data Merk Mobil = \n {dataMerkMobil}")
dataMerkMobil.sort()
print(f"Data merk mobil yang telah di sort = \n {dataMerkMobil}")

# invers sort list
dataAngka.reverse()
dataMerkMobil.reverse()
print(f"Data invers = \n {dataAngka} \n {dataMerkMobil}")

# listMataKuliah = ["Algoritma dan Pemrograman 2", "Struktur Data dan Algoritma", "Sistem Keamanan Informasi"]
# listTanggal = [1,2,3,4,5,6,7,8,9]

# print("List mata kuliah [0] = ", listMataKuliah[0])

# Update list
listNamaMahasiswa = ["asep","galih","ucup","soleh"]
print("List nama mahasiswa [2] = ", listNamaMahasiswa[2])

listNamaMahasiswa[2] = "ade"
print("Update list nama mahasiswa [2] = ", listNamaMahasiswa[2])

# delete list
del listNamaMahasiswa[2]
print("List nama mahasiswa[2] = ", listNamaMahasiswa[2])

# duplikasi nilai list
b = listNamaMahasiswa[0]
print(b)

## manipulasi list
dataMerkMobil = ["Honda", "Mazda", "Toyota", "Nissan"]
# mengambil data dari list
dataPertama = dataMerkMobil[0]
print(f"Data pertama = {dataPertama}")

dataTerakhir = dataMerkMobil[-1]
print(f"Data Terakhir = {dataPertama}")

# 
dataLength = len(dataMerkMobil)
print(f"Panjang data adalah {dataLength}")

print(f"Data sebelum ditambah  = {dataMerkMobil}")
dataMerkMobil.insert(4, "BMW")
print(f"Data setelah ditambah  = {dataMerkMobil}")

dataMerkMobil.append("Ferrari")
print(f"Data setelah ditambah  = {dataMerkMobil}")

