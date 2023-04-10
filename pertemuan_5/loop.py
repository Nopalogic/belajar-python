# while loop
i=2
x = int(input("Masukan bilangan bulat: "))

while i  <= x:
    print(i)
    i += 1

# for loop
nilai_awal = int(input("Nilai awal: "))
nilai_akhir = int(input("Nilai akhir: "))

print("""
Tampilkan bilangan
1. Ganjil
2. Genap
""")

pilihan = int(input("Pilihan: "))
if pilihan not in [1,2]:
    print("Pilihan salah")
else:
    for x in range(nilai_awal, nilai_akhir + 1):
        if pilihan == 1 and x % 2 == 1:
            print(x, end=' ')
        elif pilihan == 2 and x % 2 == 0:
            print(x, end=' ')
    else:
        print('')

## Break & Continue
# break
for i in range(10,20):
    if i == 15:
        break
    print(i)

# continue
for i in range(10,20):
    if i == 15:
        continue
    print(i)
