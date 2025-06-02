def buat_file_inventaris():
    data_buku = [
        "9781234567801,Langkah Mudah Belajar Komputer,Andi Susanto,10,40000,60000",
        "9781234567802,Dasar-Dasar Microsoft Word,Budi Hartono,5,35000,50000",
        "9781234567803,Internet Itu Gampang,Citra Dewi,8,30000,45000",
        "9781234567804,Belajar Mengetik Cepat,Dewi Lestari,3,25000,40000",
        "9781234567805,Panduan Email untuk Pemula,Eko Prasetyo,6,28000,42000",
        "9781234567806,Membuat Presentasi Menarik,Fajar Nugroho,4,45000,65000",
        "9781234567807,Mengoperasikan Laptop dengan Mudah,Gita Rahma,7,38000,55000",
        "9781234567808,Cepat Mahir Excel,Hadi Santoso,9,50000,75000",
        "9781234567809,Kenalan dengan Dunia Digital,Ika Nuraini,2,32000,47000",
        "9781234567810,Tips Aman di Internet,Joko Widodo,5,36000,52000",
    ]
    with open("inventaris_buku.txt", "w") as file:
        for data in data_buku:
            file.write(data + "\n")
def baca_inventaris():
    daftar_buku = []
    with open("inventaris_buku.txt", "r") as file:
        for baris in file:
            kolom = []
            penampung_karakter = ""

            for karakter in baris:
                if karakter == ",":
                    kolom.append(penampung_karakter)
                    penampung_karakter = ""
                elif karakter == "\n":
                    continue
                else:
                    penampung_karakter += karakter

            if penampung_karakter != "":
                kolom.append(penampung_karakter)

            buku = {
                "ISBN": kolom[0],
                "Judul": kolom[1],
                "Penulis": kolom[2],
                "Stok": int(kolom[3]),
                "Harga Beli": int(kolom[4]),
                "Harga Jual": int(kolom[5]),
                "Potensi Keuntungan": 0
            }
            daftar_buku.append(buku)
    return daftar_buku

def hitung_potensi_keuntungan(daftar_buku):
    for buku in daftar_buku:
        keuntungan = (buku["Harga Jual"] - buku["Harga Beli"]) * buku["Stok"]
        buku["Potensi Keuntungan"] = keuntungan

def simpan_laporan(daftar_buku):
    with open("laporan_inventaris.txt", "w") as file:
        header = "ISBN,Judul,Penulis,Stok,Harga Beli,Harga Jual,Potensi Keuntungan\n"
        file.write(header)

        for buku in daftar_buku:
            baris = (
                buku["ISBN"] + "," +
                buku["Judul"] + "," +
                buku["Penulis"] + "," +
                str(buku["Stok"]) + "," +
                str(buku["Harga Beli"]) + "," +
                str(buku["Harga Jual"]) + "," +
                str(buku["Potensi Keuntungan"]) + "\n"
            )
            file.write(baris)

def analisis_inventaris(daftar_buku):
    if not daftar_buku:
        print("Data inventaris kosong")
        return

    buku_tertinggi = daftar_buku[0]
    buku_terendah = daftar_buku[0]
    total_nilai_inventaris = 0
    buku_stok_kurang = []

    for buku in daftar_buku:
        if buku["Potensi Keuntungan"] > buku_tertinggi["Potensi Keuntungan"]:
            buku_tertinggi = buku
        if buku["Potensi Keuntungan"] < buku_terendah["Potensi Keuntungan"]:
            buku_terendah = buku
        total_nilai_inventaris += buku["Stok"] * buku["Harga Beli"]
        if buku["Stok"] < 5:
            buku_stok_kurang.append(buku)

    print("Buku dengan potensi keuntungan tertinggi:")
    print(f"- {buku_tertinggi['Judul']} (Potensi: Rp{buku_tertinggi['Potensi Keuntungan']})\n")
    print("Buku dengan potensi keuntungan terendah:")
    print(f"- {buku_terendah['Judul']} (Potensi: Rp{buku_terendah['Potensi Keuntungan']})\n")
    print(f"Total nilai inventaris (berdasarkan harga beli): Rp{total_nilai_inventaris}\n")

    if buku_stok_kurang:
        print("Buku yang stoknya kurang dari 5 (perlu restock):")
        for buku in buku_stok_kurang:
            print(f"- {buku['Judul']} (Stok: {buku['Stok']})")
    else:
        print("Semua stok buku mencukupi")

buat_file_inventaris()
daftar_buku = baca_inventaris()
hitung_potensi_keuntungan(daftar_buku)
simpan_laporan(daftar_buku)
analisis_inventaris(daftar_buku)