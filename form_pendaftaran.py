def form_pendaftaran():
    nama = input("Masukan nama anda: ")
    tempat_lahir = input("masukan tempat lahir anda: ")
    tanggal_lahir = input("Masukan tanggal lahir anda: ")
    tahun_lahir = int(input("Masukan tahun lahir anda: "))
    nilai_english = float(input("Masukan nilai english anda: "))
    nilai_mtk = float(input("Masukan nilai matematika anda: "))
    nilai_bahasa_indonesia = float(input("Masukan nilai bahasa indonesia anda: "))
    jenis_kelamin = input("Masukan jenis kelamin anda: ")

    rata_rata_nilai = (nilai_english + nilai_mtk + nilai_bahasa_indonesia) / 3

    if rata_rata_nilai >= 80 and jenis_kelamin == "Laki-laki":
        print("Dia disarankan untuk masuk ke Jurusan Teknik Informatika")
    elif rata_rata_nilai >= 80 and jenis_kelamin == "Perempuan":
        print("Dia disarankan untuk masuk ke Jurusan Sistem Informasi")
    else:
        print("Dia disarankan untuk masuk ke Jurusan DKV")

    umur = 2024 - tahun_lahir
    if umur >= 25:
        print("Mahasiswa yang diterima hanya yang dibawah umur 25 tahun")
    else:
        print("Mahasiswa diterima")

form_pendaftaran()