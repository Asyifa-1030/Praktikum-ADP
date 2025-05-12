x=int(input("Jumlah mahasiswa praktikum ADP: "))
nama_mahasiswa = []
nilai_mahasiswa = []

for i in range(x):
    nama = input(f"Nama mahasiswa ke-{i+1}: ")
    pretest = int(input("Nilai pretest: "))
    postest = int(input("Nilai postest: "))
    makalah = int(input("Nilai makalah: "))
    nilai = round((pretest * 0.4) + (postest * 0.4) + (makalah * 0.2), 2)
    nama_mahasiswa.append(nama)
    nilai_mahasiswa.append(nilai)
print()
print("=============== TABEL NILAI MAHASISWA ==============")
print("----------------------------------------------------")
print("|      NAMA MAHASISWA       |     NILAI AKHIR      |")
print("|---------------------------|----------------------|")

for i in range(x):
    print(f"| {nama_mahasiswa[i]:^25} | {nilai_mahasiswa[i]:^20} |")
print("----------------------------------------------------")

total_nilai = 0
i = 0
while i < x:
    total_nilai += nilai_mahasiswa[i]
    i += 1
rata_rata=round(total_nilai / x, 2)
print("Rata-rata kelas:", rata_rata)

nilai_tertinggi=nilai_mahasiswa[0]
nilai_terendah=nilai_mahasiswa[0]
nama_tertinggi=nama_mahasiswa[0]
nama_terendah=nama_mahasiswa[0]
for i in range (len(nilai_mahasiswa)):
    if nilai_mahasiswa[i] > nilai_tertinggi:
        nilai_tertinggi=nilai_mahasiswa[i]
        nama_tertinggi=nama_mahasiswa[i]
    elif nilai_mahasiswa[i] < nilai_terendah:
        nilai_terendah=nilai_mahasiswa[i]
        nama_terendah=nama_mahasiswa[i]
print("nilai tertinggi:", nama_tertinggi, nilai_tertinggi)
print("nilai terendah:",nama_terendah, nilai_terendah)
print()
for i in range(x):
    if nilai_mahasiswa[i]>rata_rata:
        diatas_rata=nilai_mahasiswa[i]
        print("mahasiswa dengan nilai diatas rata-rata kelas:",nama_mahasiswa[i], diatas_rata)
    