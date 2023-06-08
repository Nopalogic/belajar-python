# TUPLE
tup1 = ('fisika', 'kimia', 1993, 2017)
tup2 = (1, 2, 3, 4, 5)
tup3 = 'a','b','c','d'

# mengakses nilai tuple
print('tuple[0]', tup1[0])
print('tuple[1:5]', tup2[1:5])
tup1 = (12, 34.56)
tup2 = ('abc','xyz')

# Aksi seperti di bawah ini tidak bisa dilakukan pada tuple python
# karena memang nilai pada tuple python tidak bisa diubah
# tup1[0] = 100
# Jadi buatlah tuple baru sebagai berikut
tup3 = tup1 + tup2
print(tup3)
tup = ('fisika', 'kimia', 1993, 2017)
print(tup)

# menghapus tuple dengan statement del
del tup
# lalu buat kembali tuple yang baru dengan elemen yang diinginkan
tup = ('Bahasa', 'Literasi', 2020)
print('Setelah manghapus tuple: ', tup)

print('tuple[-1]', tup1[-1])