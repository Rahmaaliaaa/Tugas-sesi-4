Bilangan1 = float(input("Masukan bilangan pertama: "))
Bilangan2 = float(input("Masukan bilangan kedua: "))
Bilangan3 = float(input("Masukan bilangan ketiga: "))

nilai_terbesar = max(Bilangan1, Bilangan2, Bilangan3)
nilai_terkecil = min(Bilangan1, Bilangan2, Bilangan3)

if nilai_terbesar == nilai_terkecil:
    print("Semua bilangan sama  besar.")
else: 
    print("Bilangan terbesar adalah:", nilai_terbesar)
    print("Bilangan terkecil adalah:", nilai_terkecil)    