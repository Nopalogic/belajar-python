# implementasi tipe data, variabel, operator dan operator I/O

name = input("Masukkan nama: ")
numb1 = int(input("Masukkan angka pertama: "))
numb2 = int(input("Masukkan angka kedua: ")) #jangan input 0, nanti error
    
print(numb1,"+",numb2,"=", numb1 + numb2)

more = int(input("Ketik 1 untuk melihat hasil lainnya: "))

if more == 1:
    print(numb1,"*",numb2,"=", numb1 * numb2)
    print(numb1,"/",numb2,"=", numb1 / numb2)
    print(numb1,"%",numb2,"=", numb1 % numb2)
else:
    print("Kan tadi disuruhnya Ketik 1, kok malah ketik", more)

print("WK"*len(name))