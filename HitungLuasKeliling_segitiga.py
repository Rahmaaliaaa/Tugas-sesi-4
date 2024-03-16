def Hitung_luas(a, b, c):

    s = (a + b + c) / 2

    Luas = (s * (s - a) * (s - b) * (s -c)) ** 0.5
    return Luas

def Hitung_keliling(a, b, c):
    keliling = a + b + c
    return keliling

a = float(input("Masukan panjang sisi pertama: "))
b = float(input("Masukan panjang sisi kedua: "))
c = float(input("Masukan panjang sisi ketiga: "))

luas = Hitung_luas(a, b, c)
keliling = Hitung_keliling(a, b, c)

print("Luas segitiga adalah:", luas)
print("Keliling segitiga adalah:", keliling)
