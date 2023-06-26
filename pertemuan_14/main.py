from tkinter import *
from tkinter import messagebox

app = Tk()
app.title("APLIKASI TOKO BUKU")

# variable declaration
ap = StringVar()
std = StringVar()
ksi = StringVar()
db = StringVar()
teksTotal = StringVar()
teksUang = StringVar()
total = 0

def totalBeli():
    global ap, std, ksi, db, teksTotal, total
    hap = int(ap.get()) * 189000
    hstd = int(std.get()) * 165000
    hksi = int(ksi.get()) * 123000
    hdb = int(db.get()) * 119000

    total = hap + hstd + hksi + hdb
    teksTotal.set(str(total))

def kembalian():
    global total
    uang = int(teksUang.get())

    if uang >= total:
        kembalian = uang - total
        messagebox.showinfo(message='Kembalian kamu sebesar {}'.format(str(kembalian)))
    else:
        messagebox.showerror(message='Maaf uang kamu kurang')

def clear():
    ap.set('0')
    ksi.set('0')
    std.set('0')
    db.set('0')
    teksTotal.set('0')
    teksUang.set('0')

app.geometry('500x600')
app.configure(bg='black')

Label(
    app, 
    text='KASIR TOKO BUKU',
    bg='pink',
    foreground='pink',
    font='Poppins 18 bold',
    ).place(x=200,y=30)

Label(
    app, 
    text='1. Algoritma dan Pemrograman',
    bg='pink',
    foreground='pink',
    font='Poppins 12 bold',
    ).place(x=100,y=100)
Label(
    app, 
    text='2. Struktur Data dan Algoritma',
    bg='pink',
    foreground='pink',
    font='Poppins 12 bold',
    ).place(x=100,y=140)
Label(
    app, 
    text='3. Keamanan Sistem Informasi',
    bg='pink',
    foreground='pink',
    font='Poppins 12 bold',
    ).place(x=100,y=120)
Label(
    app, 
    text='4. DataBase',
    bg='pink',
    foreground='pink',
    font='Poppins 12 bold',
    ).place(x=100,y=220)

Label(
    app, 
    text='Rp. 189000',
    bg='pink',
    foreground='pink',
    font='Poppins 12 bold',
    ).place(x=100,y=100)
Label(
    app, 
    text='Rp. 165000',
    bg='pink',
    foreground='pink',
    font='Poppins 12 bold',
    ).place(x=100,y=140)
Label(
    app, 
    text='Rp. 123000',
    bg='pink',
    foreground='pink',
    font='Poppins 12 bold',
    ).place(x=100,y=120)
Label(
    app, 
    text='Rp. 119000',
    bg='pink',
    foreground='pink',
    font='Poppins 12 bold',
    ).place(x=100,y=220)

Spinbox(
    app,
    from_=0,
    to=100,
    width=4,
    font='Poppins 10',
    textvariable=ap,
    command=totalBeli
        ).place(x=550, y=100)
Spinbox(app, from_=0, to=100, width=4, font='Poppins 10', textvariable=std, command=totalBeli).place(x=550, y=140)
Spinbox(app, from_=0, to=100, width=4, font='Poppins 10', textvariable=ksi, command=totalBeli).place(x=550, y=180)
Spinbox(app, from_=0, to=100, width=4, font='Poppins 10', textvariable=db, command=totalBeli).place(x=550, y=220)

Label(app, text='masukkan uang anda', bg='pink', foreground='pink', font='Poppins 12').place(x=100, y=280)

Entry(app, textvariable=teksUang).place(x=100, y=300)

Label(app, text='Rp.', bg='pink', foreground='pink', font='Poppins 12 bold').place(x=350, y=300)
Label(app, textvariable=teksTotal, bg='pink', foreground='pink', font='Poppins 12 bold').place(x=380, y=300)

Button(app, text='Total', foreground='white', bg='pink', width=10, command=kembalian).place(x=100, y=400)
Button(app, text='Clear', foreground='white', bg='pink', width=10, command=clear).place(x=250, y=400)

