print("===============TEBAK ANGKA BOM===============")
print("Pemain 1")
a=int(input("Masukkan batas angka positif:"))
b=int(input("Angka BOM:"))
for a in range (1, a+1):
    if a%b==0:
        print("BOM", end=" ")
    else:
        print(a, end=" ")
print("\n")
print("Pemain 2 tebak angka BOM dari 1 sampai", a)
while True:
    c=int(input("Masukkan angka tebakan:"))
    if c<1 or c>a+1:
        print("Masukkan angka dari 1 sampai", a)
        continue
    elif c%b==0:
        print(c, "adalah angka BOM. Kamu kalah!")
        break
    else:
        print(c,"bukan angka BOM, yeay kamu menang!")
        break

