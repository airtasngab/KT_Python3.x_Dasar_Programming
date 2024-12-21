'''
00
print -> print()

02
*install requirements
1. python interpreter
2. code editor

*learn about environment, setup python interpreter (choices), and venv migration.

03
*single & multi-line comments
'''''' & #

-python -> interpreter, tapi bisa dicompile menggunakan bytecode:
di terminal dgn command:
***python -m py_compile main.py (file-name.py)***

-compile menjalankan program lebih cepat dari pada cara interpreter, akan terasa signifikan apabila baris program semakin banyak.

04
-variabel -> tempat menyimpan nilai
penamaan var. -> tdk boleh diawali angka & tdk boleh memiliki spasi, untuk cara penamaan lainnya dpt berubah2 peraturannya berdasarkan versi pythonnya. penamaan normal gunakan camell case/ gris bawah.

05
tipe data -> jenis suatu data, terdiri dari:
-integer as int: bil. bulat
-float as float: bil. pecahan .x
-string as str: kumpulan char/ teks
-bool as bool: bil.logika
-tipe data khusus 
--complex as complex: bil. imajiner?
--tipe data C, dari library ctypes import seperti c_double, c_char, c_long, dll.

06
-casting tipe data -> mengkonversi tipe data:
notes: 
False -> 0 (int), 0.0 (float)
True -> 1 (int), 1.0 (float)
*konversi string ke bool akan selalu true kecuali tidak ada string / karakter yang ditulis (string kosong.)
*konversi string berisi alfabet akan error jika dikonver ke int or float.

07
-konver input user: 
data input dari user secara default bertipe data string, untuk mengatur tipe data yang yang diinput oleh user agar sesuai dengan tipe data yang kita inginkan, maka gunakan casting tipe data. Jika kita menginginkan tipe data int atau float tetapi user mengisi alphabet atau simbol maka akan menimbulkan error, hal ini bisa diatasi dengan menggunakan exception atau error handling (ini akan dibahas di chapt. selanjutnya karena membutuhkan pemahaman mengenai pengkondisian)

*overview contoh penggunaan exception untuk memberitahu user untuk memasukkan input angka:
while(True):
    try:
        int(input('Masukkan angka: '))
        break
    except ValueError:
        print('Nilai yang anda masukkan bukan angka!')


08
-operasi aritmatika
*ada tujuh operator:
**;
/, //, %, *;
+, -.

*Pangkat (**) dieksekusi terlebih dahulu, diikuti oleh pembagian (/), pembagian bulat (//), dan sisa pembagian (%), kemudian perkalian (*), dan terakhir penjumlahan (+) dan pengurangan (-).
Jika ada beberapa operator dengan prioritas yang sama, mereka dieksekusi dari kiri ke kanan.
Anda dapat menggunakan tanda kurung () untuk mengubah urutan eksekusi sesuai kebutuhan, yang dapat membantu meningkatkan kejelasan dan menghindari kebingungan.

09
-latihan konvertor suhu
celcius (5): 4/5R, 9/5(C+32), C + 273
reamur (4): 5/4C, 9/4(R+32), 4/5R + 273
fahrenheit +-32: 5/9F(C-32)
kelvin: C - 273

'''
