# 5.	Buatlah Soal Anda sendiri dan selesaikan sendiri.
import random

pilihan_pengguna = input("Pilih gunting, batu, kertas : ").lower()
pilihan_komputer = random.choice(['gunting', 'batu','kertas'])

print(f'Pilihan anda : {pilihan_pengguna}')
print(f'pilihan komputer :  {pilihan_komputer}')

if pilihan_pengguna == pilihan_komputer :
    print('seri')
elif (pilihan_pengguna == 'gunting' and pilihan_komputer == 'kertas') or (pilihan_pengguna == 'batu' and pilihan_komputer == 'gunting') or (pilihan_pengguna == 'kertas' and pilihan_komputer == 'batu'):
    print('Anda menang')
else:
    print('Anda kalah Dan Komputer menang')        