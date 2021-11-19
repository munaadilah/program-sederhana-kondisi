nama = input("Masukkan Nama Anda: ")
umur = int(input("Masukkan Umur Anda: "))

if (umur > 30):
    print(nama + " Sudah Tua")
elif (umur >= 18  and umur <= 30):
    print(nama + " Sudah Dewasa")
elif (umur >= 13 and umur <= 17):
    print(nama + " Sudah Remaja")
elif (umur >= 5  and umur <= 12):
    print(nama + " Masih Anak - Anak")
elif (umur >= 0  and umur <= 4):
    print(nama + " Masih Balita")

else:
    print("Umur Tidak Valid")