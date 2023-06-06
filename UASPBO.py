
import tkinter as tk 

def pesan_makanan():
    # Mendapatkan input pengguna
    nama = entry_nama.get()
    alamat = entry_alamat.get()
    pesanan = entry_pesanan.get()
    
    # Menampilkan pesanan
    label_pesanan.config(text=f"Nama: {nama}\nAlamat: {alamat}\nPesanan: {pesanan}")
                         
# Data makanan
data_makanan = {
    "Nasi Goreng": 15000,
    "Mie Goreng": 12000,
    "Ayam Bakar": 20000,
    "Sate Ayam": 18000,
    "Bakso": 10000
}

# Membuat jendela utama
window = tk.Tk()
window.title("Aplikasi Pemesanan Makanan")

# Membuat elemen antarmuka pengguna
label_judul = tk.Label(window, text="Selamat Datang di Aplikasi Pemesanan Makanan", font=("Arial", 16))
label_judul.pack(pady=10)

# Membuat label dan entry untuk nama
label_nama = tk.Label(window, text="Nama:")
label_nama.pack()
entry_nama = tk.Entry(window)
entry_nama.pack()

# Membuat label dan entry untuk alamat
label_alamat = tk.Label(window, text="Alamat:")
label_alamat.pack()
entry_alamat = tk.Entry(window)
entry_alamat.pack()

# Membuat label dan entry untuk pesanan
label_pesanan = tk.Label(window, text="Pesanan:")
label_pesanan.pack()
entry_pesanan = tk.Entry(window)
entry_pesanan.pack()

# Membuat label untuk daftar makanan
label_makanan = tk.Label(window, text="Daftar Makanan:")
label_makanan.pack()

# Menambahkan checkbox untuk setiap makanan
var_makanan = []
for makanan in data_makanan:
    var = tk.IntVar()
    checkbutton = tk.Checkbutton(window, text=f"{makanan} - Rp {data_makanan[makanan]}", variable=var)
    checkbutton.pack()
    var_makanan.append(var)
    
# Membuat tombol pesan
tombol_pesan = tk.Button(window, text="Pesan", command=pesan_makanan)
tombol_pesan.pack()

# Menampilkan pesanan
label_pesanan = tk.Label(window, text="")
label_pesanan.pack()

# Menjalankan aplikasi
window.mainloop()