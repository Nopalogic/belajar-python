# make function
def hello():
    print("""
Hello world
untuk mahasiswa Teknik Informatka
Universitas Dian Nusantara    
    """)

hello()

def function():
    print("Ini fungsi")

function()

# function argumen
def sayHi(listPeserta):
    dataPeserta = listPeserta.copy()
    for peserta in dataPeserta:
        print(f"Yang terhormat {peserta}")

mhs = ["NOPAL", "ADHI", "RAMADHAN"]
sayHi(mhs)

# return function
def kuadrat(number):
    result = number ** 2
    return result

print(kuadrat(3))

def calculte(a,b):
    tambah = a + b
    kurang = a - b
    kali = a * b
    bagi = a / b
    return tambah, kurang, kali, bagi

x, y, i, j = calculte(10, 5)
print(x)
print(y)
print(i)
print(j)