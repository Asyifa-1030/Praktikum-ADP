print("===================================Selamat Datang===================================")
nama=input("Nama :")
umur=int(input("Umur :"))
jenis_kelamin=input("Jenis Kelamin :")
print("kode 3012 | Padang-Jakarta | Ekonomi=800.000 | Bisnis=850.000 | First Class=900.000")
print("kode 4015 | Padang-Batam   | Ekonomi=500.000 | Bisnis=550.000 | First Class=700.000")
print("kode 4050 | Padang-Bandung | Ekonomi=700.000 | Bisnis=750.000 | First Class=850.000")
kode=int(input("Masukkan kode maskapai :"))
if kode==3012:
    print("Tujuan maskapai adalah Padang-Jakarta")
    kelas=input("Masukkan kelas(ekonomi/bisnis/first class):")
    jumlah_tiket=int(input("Masukkan jumlah tiket:"))
    if kelas=="ekonomi":
        harga=800000
    elif kelas=="bisnis":
        harga=850000
    elif kelas=="first class":
        harga=900000   
    else:
        print("kelas tidak ditemukan")
elif kode==4015:
    print("Tujuan maskapai adalah Padang-Batam")
    kelas=input("Masukkan kelas(ekonomi/bisnis/first class):")
    jumlah_tiket=int(input("Masukkan jumlah tiket:"))
    if kelas=="ekonomi":
        harga=500000
    elif kelas=="bisnis":
        harga=550000
    elif kelas=="first class":
        harga=700000
    else:
        print("kelas tidak ditemukan")
elif kode==4050:
    print("Tujuan maskapai anda adalah Padang-Bandung")
    kelas=input("Masukkan kelas(ekonomi/bisnis/first class):")
    jumlah_tiket=int(input("Masukkan jumlah tiket:"))
    if kelas=="ekonomi":
        harga=700000
    elif kelas=="bisnis":
        harga=750000
    elif kelas=="first class":
        harga=850000
    else:
        print("kelas tidak ditemukan")
else:
    print("Tujuan tidak ditemukan")
if jumlah_tiket>3:
    diskon=harga*jumlah_tiket*20/100
    total=(harga*jumlah_tiket)-diskon
    print("Total harga=",total)
else:
    total=harga*jumlah_tiket
    print("Total harga=",total)
print("===================================Terimakasih=====================================")
        
    

    
