#Nama    : M.IQBAL FIRMANSYAH RAMADAHAN
#JURUSAN : SISTEM INFORMASI
#NIM     : SI20230025

# Daftar Barang Beserta Harganya
daftar_barang = {
    "Beras" : 16000,
    "Gula" : 20000,
    "Minyak Goreng" : 18000,
    "Garam" : 4000,
    "Roti" : 8000,
    "Ayam" : 40000
}
# Menampilkan daftar barang
print("xxxxxxxxxxxxxxxxxxxxx")
print("xx Daftar Barang : xx")
print("xxxxxxxxxxxxxxxxxxxxx")
for barang, harga in daftar_barang.items():
    print(f"{barang}: Rp.{harga}")

# Input jumlah barang yang dibeli
total_belanja = 0
jumlah_barang = int(input("Masukkan jumlah barang yang anda beli : "))

# Menghitung total belanjaan
for i in range(jumlah_barang) :
        barang = input(f"Masukkan nama barang ke {i+1} : ")
        if barang in daftar_barang:
            total_belanja += daftar_barang[barang]
        else:
            print(f"{barang} barang yang anda cari tidak ada didalam daftar.")

# Menampilkan total belanjaan
print("\n============= Struk Belanja==================")
print(f"total belanjaan anda: Rp {total_belanja}")
Bayar = int(input("Jumlah Nominal uang Rp."))
kembalian = (Bayar - total_belanja)
print("uang kembaliannya Rp.", kembalian)
