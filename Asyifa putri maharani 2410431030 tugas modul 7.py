def data():
    x=int(input('jumlah mahasiswa:'))
    data_mahasiswa=[]
    total_uts=total_uas=total_tugas=total_akhir=0
    for i in range(x):
        nama = input("Nama mahasiswa:")
        nim=int(input('Nim:'))
        nilai_uts = float(input("Nilai UTS: "))
        nilai_uas= float(input("Nilai UAS: "))
        nilai_tugas= float(input("Nilai tugas: "))
        nilai_akhir=nilai_uas*0.35+nilai_uts*0.35+nilai_tugas*0.30
        data_mahasiswa.append((nama, nim, nilai_uts, nilai_uas, nilai_tugas, nilai_akhir))
        total_uts+=nilai_uts
        total_uas+=nilai_uas
        total_tugas+=nilai_tugas
        total_akhir+=nilai_akhir
    rata_uts=total_uts/x
    rata_uas=total_uas/x
    rata_tugas=total_tugas/x
    rata_akhir=total_akhir/x
    for i in range(x):
        for j in range(i+1, x):
            if data_mahasiswa[j][5] > data_mahasiswa[i][5]:
                data_mahasiswa[i], data_mahasiswa[j] = data_mahasiswa[j], data_mahasiswa[i]
    print('-------------------------------------------------------------------------------------------------')
    print(f"|{'Nama':^20}|{'NIM':^15}|{'Nilai UTS':^10}|{'Nilai UAS':^10}|{'Nilai Tugas':^12}|{'Nilai Akhir':^12}|{'Peringkat':^10}|")
    print('-------------------------------------------------------------------------------------------------')
    peringkat = 1
    for r in data_mahasiswa:
        print(f"|{r[0]:^20}|{r[1]:^15}|{r[2]:^10.2f}|{r[3]:^10.2f}|{r[4]:^12.2f}|{r[5]:^12.2f}|{peringkat:^10}|")
        peringkat += 1
    print('-------------------------------------------------------------------------------------------------')
    print(f"|{'':<20}|{'':^15}|{'Rata2 UTS':^10}|{'Rata2 UAS':^10}|{'Rata2 Tugas':^12}|{'Rata2 Akhir':^12}|{'' :^10}|")
    print(f"|{'':<20}|{'':^15}|{rata_uts:^10.2f}|{rata_uas:^10.2f}|{rata_tugas:^12.2f}|{rata_akhir:^12.2f}|{'' :^10}|")
    print('-------------------------------------------------------------------------------------------------')
data()
