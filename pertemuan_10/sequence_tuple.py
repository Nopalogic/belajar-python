dosen = ("Nopal", "Bogor", 20)

nama, asal, usia = dosen

print('Nama: ', nama)
print('Asal: ', asal)
print('Usia: ', usia)

a = (1,2,3)
b = (50,60,70)

c = a + b
print(c)

# slicing tuple
buah = ('Pisang', 'Nanas', 'Melon', 'Durian')

print(buah[0:1])
print(buah[0:2])
print(buah[1:3])
print(buah[0:-1])
print(buah[-1:-3])
print(buah[-1:3])
print(buah[-3:-1])

# slicing tanpa batas
buah = ('Pisang', 'Nanas', 'Melon', 'Durian')

print(buah[0:])
print(buah[1:])
print(buah[2:])
print(buah[3:])
print(buah[:0])
print(buah[:1])
print(buah[:2])
print(buah[:3])
print(buah[:4])