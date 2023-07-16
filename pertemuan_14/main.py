from tkinter import *
from tkinter import messagebox

app = Tk()
app.title('Aplikasi Toko Buku')

# variabel
ap = StringVar()
std = StringVar()
ksi = StringVar()
db = StringVar()
al = StringVar()
kwu = StringVar()
pk = StringVar()
cd = StringVar()
kl = StringVar()
rpl = StringVar()
tekstotal = StringVar()
teksDiskon = StringVar()
teksPajak = StringVar()
teksBiaya = StringVar()
teksuang = StringVar()
total = 0

# buat function
def totalbeli():
    global ap, std, ksi, db, al, kwu, pk, cd,kl, rpl, tekstotal, teksPajak, teksDiskon, total
    hap = int(ap.get()) * 100000
    hstd = int(std.get()) * 165000
    hksi = int(ksi.get()) * 123000
    hdb = int(db.get()) * 119000
    hal = int(al.get()) * 119000
    hkwu = int(kwu.get()) * 255000
    hpk = int(pk.get()) * 152000
    hcd = int(cd.get()) * 135000
    hkl = int(kl.get()) * 234000
    hrpl = int(rpl.get()) * 460000

    total = hap + hstd + hksi + hdb + hal + hkwu + hpk + hcd + hkl + hrpl

    if total >= 500000:
        diskon = total * 5 / 100
    elif total >= 1000000:
        diskon = total * 10 / 100
    else:
        diskon = 0

    tekstotal.set(str(int(total)))
    
    total -= diskon

    pajak = total * 10 / 100
    biaya = total + pajak

    teksDiskon.set(str(int(diskon)))
    teksPajak.set(str(int(pajak)))
    teksBiaya.set(str(int(biaya)))

def kembalian():
    global total
    uang = int(teksuang.get())

    if uang >= total:
        kembalian = uang - total
        messagebox.showinfo(message='Kembalian kamu sebesar {}'.format(str(kembalian)))
    else:
        messagebox.showerror(message='maaf uang kamu kurang')

def clear():
        ap.set('0')
        std.set('0')
        ksi.set('0')
        db.set('0')
        al.set('0')
        kwu.set('0')
        pk.set('0')
        cd.set('0')
        kl.set('0')
        rpl.set('0')
        tekstotal.set('0')
        teksPajak.set('0')
        teksDiskon.set('0')
        teksBiaya.set('0')
        teksuang.set('0')


app.geometry('1000x1000') # membuat ukuran
app.configure(bg='#0f0e17') # membuat backgroung warna

# membuat properti tulisan title
Label(app, text='KASIR TOKO BUKU', bg='#0f0e17', foreground='#ff8906', font='Poppins 18 bold').place(x=200,y=30)

# membuat label nama menu
Label(app, text='1.  Tutorial Django', bg='#0f0e17', foreground='#ff8906', font='Poppins 12 bold').place(x=100,y=100)
Label(app, text='2.  Tips Jadi Pintar', bg='#0f0e17', foreground='#ff8906', font='Poppins 12 bold').place(x=100,y=140)
Label(app, text='3.  Keamanan Jaringan', bg='#0f0e17', foreground='#ff8906', font='Poppins 12 bold').place(x=100,y=180)
Label(app, text='4.  Database', bg='#0f0e17', foreground='#ff8906', font='Poppins 12 bold').place(x=100,y=220)
Label(app, text='5.  Aljabar Boolean', bg='#0f0e17', foreground='#ff8906', font='Poppins 12 bold').place(x=100,y=260)
Label(app, text='6.  Kewirausahaan', bg='#0f0e17', foreground='#ff8906', font='Poppins 12 bold').place(x=100,y=300)
Label(app, text='7.  Pendidikan Karakter', bg='#0f0e17', foreground='#ff8906', font='Poppins 12 bold').place(x=100,y=340)
Label(app, text='8.  Clean Code', bg='#0f0e17', foreground='#ff8906', font='Poppins 12 bold').place(x=100,y=380)
Label(app, text='9.  Kalkulus', bg='#0f0e17', foreground='#ff8906', font='Poppins 12 bold').place(x=100,y=420)
Label(app, text='10. Rekayasa Genitika', bg='#0f0e17', foreground='#ff8906', font='Poppins 12 bold').place(x=100,y=460)

# membuat label harga
Label(app, text='Rp. 100000', bg='#0f0e17', foreground='#ff8906', font='Poppins 12 bold').place(x=350,y=100)
Label(app, text='Rp. 165000', bg='#0f0e17', foreground='#ff8906', font='Poppins 12 bold').place(x=350,y=140)
Label(app, text='Rp. 123000', bg='#0f0e17', foreground='#ff8906', font='Poppins 12 bold').place(x=350,y=180)
Label(app, text='Rp. 119000', bg='#0f0e17', foreground='#ff8906', font='Poppins 12 bold').place(x=350,y=220)
Label(app, text='Rp. 119000', bg='#0f0e17', foreground='#ff8906', font='Poppins 12 bold').place(x=350,y=260)
Label(app, text='Rp. 255000', bg='#0f0e17', foreground='#ff8906', font='Poppins 12 bold').place(x=350,y=300)
Label(app, text='Rp. 152000', bg='#0f0e17', foreground='#ff8906', font='Poppins 12 bold').place(x=350,y=340)
Label(app, text='Rp. 135000', bg='#0f0e17', foreground='#ff8906', font='Poppins 12 bold').place(x=350,y=380)
Label(app, text='Rp. 234000', bg='#0f0e17', foreground='#ff8906', font='Poppins 12 bold').place(x=350,y=420)
Label(app, text='Rp. 460000', bg='#0f0e17', foreground='#ff8906', font='Poppins 12 bold').place(x=350,y=460)

# membuat spinbox
Spinbox(app, from_=0, to=100, width=4, font='Poppins 10', textvariable=ap, command=totalbeli).place(x=550,y=100)
Spinbox(app, from_=0, to=100, width=4, font='Poppins 10', textvariable=std, command=totalbeli).place(x=550,y=140)
Spinbox(app, from_=0, to=100, width=4, font='Poppins 10', textvariable=ksi, command=totalbeli).place(x=550,y=180)
Spinbox(app, from_=0, to=100, width=4, font='Poppins 10', textvariable=db, command=totalbeli).place(x=550,y=220)
Spinbox(app, from_=0, to=100, width=4, font='Poppins 10', textvariable=al, command=totalbeli).place(x=550,y=260)
Spinbox(app, from_=0, to=100, width=4, font='Poppins 10', textvariable=kwu, command=totalbeli).place(x=550,y=300)
Spinbox(app, from_=0, to=100, width=4, font='Poppins 10', textvariable=pk, command=totalbeli).place(x=550,y=340)
Spinbox(app, from_=0, to=100, width=4, font='Poppins 10', textvariable=cd, command=totalbeli).place(x=550,y=380)
Spinbox(app, from_=0, to=100, width=4, font='Poppins 10', textvariable=kl, command=totalbeli).place(x=550,y=420)
Spinbox(app, from_=0, to=100, width=4, font='Poppins 10', textvariable=rpl, command=totalbeli).place(x=550,y=460)

# membuat label pembayaran
Label(app, text='Masukan uang anda', bg='#0f0e17', foreground='#ff8906', font='Poppins 12 ').place(x=100,y=540)
Label(app, text='Jumlah', bg='#0f0e17', foreground='#ff8906', font='Poppins 12 ').place(x=350,y=540)
Label(app, text='Pajak', bg='#0f0e17', foreground='#ff8906', font='Poppins 12 ').place(x=460,y=540)
Label(app, text='diskon ', bg='#0f0e17', foreground='#ff8906', font='Poppins 12 ').place(x=555,y=540)
Label(app, text='total ', bg='#0f0e17', foreground='#ff8906', font='Poppins 12 ').place(x=670,y=540)

# membuat entry jumlah uang
Entry(app, textvariable=teksuang).place(x=100,y=580)

# membuat label total
Label(app, text='Rp. ', bg='#0f0e17', foreground='#ff8906', font='Poppins 12 bold').place(x=350,y=580)
Label(app, textvariable=tekstotal, bg='#0f0e17', foreground='#ff8906', font='Poppins 12 bold').place(x=380,y=580)

Label(app, text='Rp. ', bg='#0f0e17', foreground='#ff8906', font='Poppins 12 bold').place(x=460,y=580)
Label(app, textvariable=teksPajak, bg='#0f0e17', foreground='#ff8906', font='Poppins 12 bold').place(x=490,y=580)

Label(app, text='Rp. ', bg='#0f0e17', foreground='#ff8906', font='Poppins 12 bold').place(x=555,y=580)
Label(app, textvariable=teksDiskon, bg='#0f0e17', foreground='#ff8906', font='Poppins 12 bold').place(x=585,y=580)

Label(app, text='Rp. ', bg='#0f0e17', foreground='#ff8906', font='Poppins 12 bold').place(x=670,y=580)
Label(app, textvariable=teksBiaya, bg='#0f0e17', foreground='#ff8906', font='Poppins 12 bold').place(x=700,y=580)

# membuat tombol
Button(app, text='Bayar', foreground='white', bg='#36ae7c', width=10, command=kembalian).place(x=100,y=640)
Button(app, text='Clear', foreground='white', bg='#ff1e1e', width=10, command=clear).place(x=250,y=640)

# footer text
Label(app, text='Created by Naufal Adhi Ramadhan', bg='#0f0e17', foreground='#ff8906', font='Poppins 10 ').place(x=300,y=680)

app.mainloop() # menampilkan aplikasi