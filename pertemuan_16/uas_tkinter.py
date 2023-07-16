import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

dataPasien = []

gender = [
    "Laki-laki",
    "Perempuan",
]

dataLayanan = [
    ['Rawat Jalan / Poliklinik', 250000],
    ['Rawat Inap', 500000],
    ['Gawat Darurat', 750000],
    ['Kanker Terpadu', 800000],
    ['Kedokteran Nuklir', 900000],
    ['Ibu dan Anak Terpadu', 600000],
    ['Rawat Intensif Terpadu', 1000000],
    ['Bedah Sentral dan Anastesi', 2000000],
]

dataDokter = [
    "dr. Alberto",
    "dr. Alexa",
    "dr. Brian",
    "dr. Adelwis",
    "dr. Bonerto",
    "dr. Glenn",
    "dr. Dilan",
    "dr. Brillian",
    "dr. Kawisha",
]

def clear():
    entryNama.delete(0, tk.END)
    entryAlamat.delete(0, tk.END)
    comboGender.set('')
    checkBPJS.set(False)
    comboLayanan.set('')
    comboDokter.set('')
    entryLama.delete(0, tk.END)

def tambahPasien():
    nama = entryNama.get()
    alamat = entryAlamat.get()
    gender = comboGender.get()
    bpjs = checkBPJS.get()
    layanan = comboLayanan.get()
    dokter = comboDokter.get()
    lama = int(entryLama.get())

    biaya = 0
    for item in dataLayanan:
        if item[0] == layanan:
            biaya = item[1]
            break

    biayaLayanan = 0
    if lama == 1:
        biayaLayanan = 100000
    elif lama == 2:
        biayaLayanan = 150000
    elif lama > 3:
        biayaLayanan = 250000
    elif lama > 7:
        biayaLayanan = 600000

    if bpjs:
        biayaLayanan = 0

    total = biaya + biayaLayanan

    pasien = {
        'nama': nama,
        'alamat': alamat,
        'gender': gender,
        'layanan': layanan,
        'biaya': biaya,
        'dokter': dokter,
        'lama': lama,
        'total': total,
        'bpjs': bpjs,
        'biayaLayanan': biayaLayanan,
        'pembayaran': 0,
    }

    dataPasien.append(pasien)
    updateTable()
    clear()

    messagebox.showinfo("Success", "Data pasien berhasil ditambahkan.")

def updateTable():
    tree.delete(*tree.get_children())
    for i, pasien in enumerate(dataPasien, start=1):
        tree.insert("", "end", values=(i, pasien['nama'], pasien['alamat'], pasien['gender'], pasien['layanan'], pasien['biaya'], pasien['dokter'], pasien['lama'], pasien['total'], pasien['pembayaran']))

def bayarPasien():
    selected_item = tree.selection()
    if not selected_item:
        messagebox.showwarning("Peringatan", "Silakan pilih pasien terlebih dahulu.")
        return

    pasien_index = int(tree.item(selected_item, 'text')) - 1
    pasien = dataPasien[pasien_index]

    # Display payment dialog
    dialog = tk.Toplevel()
    dialog.title("Pembayaran")
    dialog.geometry("300x150")

    label_total = ttk.Label(dialog, text=f"Total biaya: {pasien['total']}")
    label_total.pack()

    label_pembayaran = ttk.Label(dialog, text="Jumlah pembayaran:")
    label_pembayaran.pack()

    entry_pembayaran = ttk.Entry(dialog)
    entry_pembayaran.pack()

    def prosesPembayaran():
        try:
            pembayaran = int(entry_pembayaran.get())
            if pembayaran < pasien['total']:
                messagebox.showerror("Error", "Jumlah pembayaran tidak mencukupi.")
            else:
                kembalian = pembayaran - pasien['total']
                pasien['pembayaran'] = pembayaran
                updateTable()
                dialog.destroy()
                messagebox.showinfo("Pembayaran Berhasil", f"Pembayaran sebesar {pembayaran} diterima. Kembalian: {kembalian}")
        except ValueError:
            messagebox.showerror("Error", "Masukkan angka yang valid untuk pembayaran.")

    btn_proses = ttk.Button(dialog, text="Proses Pembayaran", command=prosesPembayaran)
    btn_proses.pack()

# GUI
app = tk.Tk()
app.title("Aplikasi Pendaftaran Pasien")

# Frame utama
mainFrame = ttk.Frame(app, padding="20")
mainFrame.grid(row=0, column=0, sticky="nsew")

# Label dan Entry Nama
labelNama = ttk.Label(mainFrame, text="Nama:")
labelNama.grid(row=0, column=0, sticky="w")
entryNama = ttk.Entry(mainFrame)
entryNama.grid(row=0, column=1, pady=5, sticky="w")

# Label dan Entry Alamat
labelAlamat = ttk.Label(mainFrame, text="Alamat:")
labelAlamat.grid(row=1, column=0, sticky="w")
entryAlamat = ttk.Entry(mainFrame)
entryAlamat.grid(row=1, column=1, pady=5, sticky="w")

# Label dan Combobox Jenis Kelamin
labelJenisKelamin = ttk.Label(mainFrame, text="Jenis kelamin:")
labelJenisKelamin.grid(row=2, column=0, sticky="w")
comboGender = ttk.Combobox(mainFrame, values=[item for item in gender])
comboGender.grid(row=2, column=1, pady=5, sticky="w")

# Checkbutton BPJS
checkBPJS = tk.BooleanVar()
chkBPJS = ttk.Checkbutton(mainFrame, text="Punya BPJS", variable=checkBPJS)
chkBPJS.grid(row=3, column=0, columnspan=2, pady=5, sticky="w")

# Label dan Combobox Layanan
labelLayanan = ttk.Label(mainFrame, text="Layanan:")
labelLayanan.grid(row=4, column=0, sticky="w")
comboLayanan = ttk.Combobox(mainFrame, values=[item[0] for item in dataLayanan])
comboLayanan.grid(row=4, column=1, pady=5, sticky="w")

# Label dan Combobox Dokter
labelDokter = ttk.Label(mainFrame, text="Dokter:")
labelDokter.grid(row=5, column=0, sticky="w")
comboDokter = ttk.Combobox(mainFrame, values=dataDokter)
comboDokter.grid(row=5, column=1, pady=5, sticky="w")

# Label dan Entry Lama Waktu
labelLama = ttk.Label(mainFrame, text="Lama Waktu:")
labelLama.grid(row=6, column=0, sticky="w")
entryLama = ttk.Entry(mainFrame)
entryLama.grid(row=6, column=1, pady=5, sticky="w")

# Button Tambah Pasien
btnTambah = ttk.Button(mainFrame, text="Tambah Pasien", command=tambahPasien)
btnTambah.grid(row=7, column=0, columnspan=2, pady=10)

# Button Bayar Pasien
btnBayar = ttk.Button(mainFrame, text="Bayar Pasien", command=bayarPasien)
btnBayar.grid(row=7, column=1, columnspan=2, pady=10)

# Tabel untuk menampilkan data pasien
tree = ttk.Treeview(mainFrame, columns=("No.", "Nama", "Alamat", "Jenis Kelamin", "Layanan", "Biaya", "Dokter", "Lama Waktu", "Total"), show="headings")
tree.grid(row=8, column=0, columnspan=2, pady=10)

tree.heading("No.", text="No.")
tree.heading("Nama", text="Nama")
tree.heading("Alamat", text="Alamat")
tree.heading("Jenis Kelamin", text="Jenis Kelamin")
tree.heading("Layanan", text="Layanan")
tree.heading("Biaya", text="Biaya")
tree.heading("Dokter", text="Dokter")
tree.heading("Lama Waktu", text="Lama Waktu")
tree.heading("Total", text="Total")

tree.column("No.", width=50, anchor="center")
tree.column("Biaya", width=80, anchor="center")
tree.column("Lama Waktu", width=80, anchor="center")
tree.column("Total", width=80, anchor="center")

updateTable()

app.mainloop()
