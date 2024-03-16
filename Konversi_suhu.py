def konversi_suhu():
    suhu_celsius = float(input("Masukkan suhu dalam derajat Celsius: "))
    konversi_fahrenheit = (suhu_celsius * 9 / 5) + 32
    print(f"{suhu_celsius} derajat Celsius sama dengan {konversi_fahrenheit} derajat Fahrenheit.")

    suhu_kelvin = suhu_celsius + 273.15
    print(f"{suhu_celsius} derajat Celsius sama dengan {suhu_kelvin} derajat Kelvin.")

    suhu_reamur = suhu_celsius * 4 / 5
    print(f"{suhu_celsius} derajat Celsius sama dengan {suhu_reamur} derajat Reamur.")

konversi_suhu()

   
    