Bilangan = int(input("Masukan sebuah bilangan: "))

if Bilangan % 2 == 0:
    print(Bilangan, "adalah bilangan genap.")
else:
    print(Bilangan, "adalah bilangan ganjil.")  

if Bilangan > 0:
    print(Bilangan, "adalah bilangan positif.")
elif Bilangan < 0:
    print(Bilangan, "adalah bilangan negatif.")
else: 
    print(Bilangan, "adalah nol.")          