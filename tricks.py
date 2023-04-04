# list comperhention
angka = [1, 2, 3, 4, 5]
kuadrat = [x ** 2 for x in angka]
print(kuadrat)

# format string
nama = "Asep"
umur = 30
print(f"{nama} berumur {umur} tahun")

# enumerate
list_buah = ["apel", "mangga", "jeruk"]
for indeks, buah in enumerate(list_buah):
    print(f"{indeks}: {buah}")

# packing dan unpacking
def jumlah(a, b):
    return a + b

angka = (3, 5)
hasil = jumlah(*angka)
print(hasil)

# walrus operator :=
angka = [1, 2, 3, 4, 5]
total = 0
while(nilai := angka.pop()) > 2:
    total += nilai
print(total)
