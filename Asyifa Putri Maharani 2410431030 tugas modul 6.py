while True:
    baris_a=int(input("jumlah baris A:"))
    kolom_a=int(input("jumlah kolom A:"))
    matriks_a=[]
    for i in range(baris_a):
        baris=[]
        for j in range(kolom_a):
            elemen=int(input('masukkan elemen:'))
            baris.append(elemen)
        matriks_a.append(baris)
    matriks_b=[]
    baris_b=int(input("jumlah baris B:"))
    kolom_b=int(input("jumlah kolom B:"))
    for i in range(baris_b):
        baris=[]
        for j in range(kolom_b):
            elemen=int(input('masukkan elemen:'))
            baris.append(elemen)
        matriks_b.append(baris)

    print("masukkan pilihan operasi:")
    print("1.Penjumlahan matriks")
    print("2.Pengurangan matriks")
    print("3.Perkalian matriks")
    print("4.Determinan matriks")
    print("5.Invers matriks")
    print("6.Transpose matriks")
    pilihan=int(input('masukkan pilihan operasi(1/2/3/4/5/6)'))
    if pilihan==1:
        if baris_a!=baris_b or kolom_a!=kolom_b:
            print("ukuran matriks tidak sama")
        else:
            for i in range(baris_a):
                hasil = []
                for j in range(kolom_a):
                    hasil.append(matriks_a[i][j]+matriks_b[i][j])
                print(hasil)
    elif pilihan==2:
        if baris_a!=baris_b or kolom_a!=kolom_b:
            print("ukuran matriks tidak sama")
        else:
            for i in range(baris_a):
                hasil = []
                for j in range(kolom_a):
                    hasil.append(matriks_a[i][j]-matriks_b[i][j])
                print(hasil)
    elif pilihan==3:
        if kolom_a!=baris_b:
            print("ukuran matriks tidak sama")
        else:
            hasil=[]
            for i in range(baris_a):
                baris=[]
                for j in range(kolom_b):
                    total=0
                    for k in range(kolom_a):
                        total+=matriks_a[i][k] * matriks_b[k][j]
                    baris.append(total)
                hasil.append(baris)
        for r in hasil:
            print(r)
    elif pilihan==4:
        if baris_a!=kolom_a and baris_b!=kolom_b:
            print("kedua matriks harus berbentuk persegi")
        else:
            if baris_a==kolom_a:
                if baris_a==2:
                    det_a = matriks_a[0][0]*matriks_a[1][1] - matriks_a[0][1]*matriks_a[1][0] 
                    print("determinan matriks A=", det_a)
                elif baris_a==3:
                    a=matriks_a
                    det_aa=(a[0][0]*a[1][1]*a[2][2] + 
                            a[0][1]*a[1][2]*a[2][0] +
                            a[0][2]*a[1][0]*a[2][1] -
                            a[0][2]*a[1][1]*a[2][0] -
                            a[0][0]*a[1][2]*a[2][1] -
                            a[0][1]*a[1][0]*a[2][2])
                    print('determinan matriks A=',det_aa)
            if baris_b==kolom_b:
                if baris_b==2:
                    det_b=matriks_b[0][0]*matriks_b[1][1] - matriks_b[0][1]*matriks_b[1][0]
                    print("determinan matriks B=", det_b)
                elif baris_b==3:
                    b=matriks_b
                    det_bb=(b[0][0]*b[1][1]*b[2][2] +
                            b[0][1]*b[1][2]*b[2][0] +
                            b[0][2]*b[1][0]*b[2][1] -
                            b[0][2]*b[1][1]*b[2][0] -
                            b[0][0]*b[1][2]*b[2][1] -
                            b[0][1]*b[1][0]*b[2][2])
                    print("determinan matriks B=", det_bb)
    elif pilihan==5:
        if baris_a == kolom_a:
            if baris_a==2:
                a = matriks_a
                det = a[0][0]*a[1][1] - a[0][1]*a[1][0]
                if det == 0:
                    print("Matriks A tidak memiliki invers")
                else:
                    invers = [[ a[1][1]/det, -a[0][1]/det],
                            [-a[1][0]/det,  a[0][0]/det]]           
                    print("Invers Matriks A:")
                for baris in invers:
                    print(baris)
            if baris_a== 3:
                n = baris_a
                simpan= []
                for i in range(n):
                    baris = []
                    for j in range(n):
                        baris.append(a[i][j])
                    simpan.append(baris)

                identitas = []
                for i in range(n):
                    baris = []
                    for j in range(n):
                        if i == j:
                            baris.append([1][0])
                        else:
                            baris.append([0][0])
                    identitas.append(baris)

                for i in range(n):
                    if simpan[i][i] == 0:
                        tukar = False
                        for k in range(i+1, n):
                            if simpan[k][i] != 0:
                                simpan[i], simpan[k] = simpan[k], simpan[i]
                                identitas[i], identitas[k] = identitas[k], identitas[i]
                                tukar = True
                                break
                        if not tukar:
                            print("Matriks A tidak memiliki invers (determinan = 0)")
                            break
                    pembagi = simpan[i][i]
                    for j in range(n):
                        simpan[i][j] /= pembagi
                        identitas[i][j] /= pembagi

                    for k in range(n):
                        if k != i:
                            faktor = simpan[k][i]
                            for j in range(n):
                                simpan[k][j] -= faktor *simpan[i][j]
                                identitas[k][j] -= faktor * identitas[i][j]
                    else:
                        print("Invers Matriks A:")
                        for i in range(n):
                            print("[", end=" ")
                            for j in range(n):
                                print(f"{identitas[i][j]:^8.2f}", end=" ")
                            print("]")
            else:
                print("Matriks harus persegi dan berukuran 2x2 atau 3x3 untuk menghitung invers.")
        if baris_b == kolom_b:
            if baris_b==2:
                b= matriks_b
                det = b[0][0]*b[1][1] - b[0][1]*b[1][0]
                if det == 0:
                    print("Matriks B tidak memiliki invers (determinan = 0)")
                else:
                    invers = [[ b[1][1]/det, -b[0][1]/det],
                            [-b[1][0]/det,  b[0][0]/det]]           
                    print("Invers Matriks B:")
                for baris in invers:
                    print(baris)
            if baris_b== 3:
                n = baris_b
                simpan= []
                for i in range(n):
                    baris = []
                    for j in range(n):
                        baris.append(b[i][j])
                    simpan.append(baris)

                identitas = []
                for i in range(n):
                    baris = []
                    for j in range(n):
                        if i == j:
                            baris.append([1][0])
                        else:
                            baris.append([0][0])
                    identitas.append(baris)

                for i in range(n):
                    if simpan[i][i] == 0:
                        tukar = False
                        for k in range(i+1, n):
                            if simpan[k][i] != 0:
                                simpan[i], simpan[k] = simpan[k], simpan[i]
                                identitas[i], identitas[k] = identitas[k], identitas[i]
                                tukar = True
                                break
                        if not tukar:
                            print("Matriks B tidak memiliki invers (determinan = 0)")
                            break
                    pembagi = simpan[i][i]
                    for j in range(n):
                        simpan[i][j] /= pembagi
                        identitas[i][j] /= pembagi

                    for k in range(n):
                        if k != i:
                            faktor = simpan[k][i]
                            for j in range(n):
                                simpan[k][j] -= faktor * simpan[i][j]
                                identitas[k][j] -= faktor * identitas[i][j]
                    else:
                        print("Invers Matriks B:")
                        for i in range(n):
                            print("[", end=" ")
                            for j in range(n):
                                print(f"{identitas[i][j]:^8.2f}", end=" ")
                            print("]")
            else:
                print("Matriks harus persegi dan berukuran 2x2 atau 3x3")
    elif pilihan==6:
        for i in range(kolom_a):
            barisA=[]
            for j in range(baris_a):
                barisA.append(matriks_a[j][i])
            print('Transpose matriks A=',barisA)
        for i in range(kolom_b):
            barisB=[]
            for j in range(baris_b):
                barisB.append(matriks_b[j][i])
            print('Transpose matriks B=', barisB)
    else:
        print('operasi tidak tersedia')
        break

