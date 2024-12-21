# Episode input user

# data yang dimasukan pasti string
data = input("Masukan data: ")

print("data = ",data,",type =",type(data))

# jika kita ingin mengambil int, maka
angka1 = float(input("masukan angka: "))
angka2 = int(input("masukan angka: "))

print("data = ",angka1,",type =",type(angka1))
print("data = ",angka2,",type =",type(angka2))

# bagaimana dengan boolean
biner = bool(int(input("masukan nilai boolean: ")))

print("data = ",biner,",type =",type(biner))

binerSTR = bool(input("masukan nilai boolean: "))

print("data = ",binerSTR,",type =",type(binerSTR))



# ##################################################################################################
# try: 
#     angka = int(input('Masukkan data: '))
# except ValueError:
#     print('Nilai yang anda masukkan bukan angka! coba lagi')
#     angka = int(input('Masukkan data: '))



# while True:  # Loop untuk terus meminta input hingga valid
#     try: 
#         angka = int(input('Masukkan data: '))
#         break  # Keluar dari loop jika input valid
#     except ValueError:
#         print('Nilai yang anda masukkan bukan angka! Coba lagi.')
