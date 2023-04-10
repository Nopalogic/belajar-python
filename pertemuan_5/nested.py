# nested for
for i in range(3):
    print("Perulangan luar [i] = ", i)

    for j in range(5):
        print(f"Perulangan dalam [i, j] = {str(i)}, {str(j)}")

listKota = ["Jakarta","Surabaya","Bogor"]

# nested while
for kota in listKota:
    print(kota)

    listTempat = ["Taman","Lapangan","Mall"]

    while listTempat:
        print("--->", listTempat.pop(0))