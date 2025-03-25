while True:
    r = int(input("Masukkan jumlah baris kursi (minimal 4): "))
    c = int(input("Masukkan jumlah kolom kursi (minimal 4): "))
    if r < 4 or c < 4:
        print("Ukuran minimal bioskop 4x4, silahkan masukkan ulang")
        continue
    else:
        print("Ukuran adalah", r, 'x', c)
        break
kursi_dipesan = set()
print("Layout Kursi Bioskop:")
nomor = 1
for i in range(r):
    for j in range(c):
        print(f"{nomor}", end=" ")
        if nomor % c == 0:  
            print()
        nomor += 1
while True:
    nomor_kursi = int(input("Masukkan nomor kursi yang dipesan (atau 0 untuk selesai): "))
    if nomor_kursi == 0:
        print("Terima kasih telah memesan tiket!")
        break
    elif nomor_kursi < 1 or nomor_kursi > r * c:
        print("Nomor kursi tidak tersedia, masukkan kembali")
        continue
    elif nomor_kursi in kursi_dipesan:
        print("Kursi sudah dipesan, silahkan pilih kursi lain")
        continue
    else:
        print(f"Kursi {nomor_kursi} berhasil dipesan")
    kursi_dipesan.add(nomor_kursi)
    print("Layout kursi bioskop:")
    nomor = 1
    for i in range(r):
        for j in range(c):
            if nomor in kursi_dipesan:
                print(f"{'X'}", end=" ")
            else:
                print(f"{nomor}", end=" ")
            if nomor % c == 0:  
                print()
            nomor += 1
