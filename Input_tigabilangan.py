Bilangan1 = float(input("Masukan bilangan pertama: "))
Bilangan2 = float(input("Masukan bilangan kedua: "))
Bilangan3 = float(input("Masukan bilangan ketiga: "))

bilangan_terkecil = Bilangan1

if Bilangan2 < bilangan_terkecil:
    bilangan_terkecil = Bilangan2

if Bilangan3 < bilangan_terkecil:
    bilangan_terkecil = Bilangan3

print("Bilangan terkecil adalah:", bilangan_terkecil)    

