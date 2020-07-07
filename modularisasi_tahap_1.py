"""
Program menghitung luas segitiga
luas segitiga = alas * tinggi/2
"""
print('\nMenghitung luas segitiga 1')
alas = 10
tinggi = 6
luas_segitiga = alas * tinggi/2
print(f'Segitiga dengan alas={alas} dan tinggi={tinggi} memiliki luas {luas_segitiga}')

print('\nMenghitung luas segitiga 2 dengan CP')
alas = 15
tinggi = 5
luas_segitiga = alas * tinggi/2
print(f'Segitiga dengan alas={alas} dan tinggi={tinggi} memiliki luas {luas_segitiga}')

print('\nMembuat fungsi hitung_luas_segitiga')
def hitung_luas_segitiga(alas, tinggi):
    luas_segitiga = alas * tinggi / 2
    return  luas_segitiga

alas = 10
tinggi = 6
print(f'Dengan fungsi, segitiga dengan alas={alas} dan tinggi={tinggi} memiliki luas{hitung_luas_segitiga(alas, tinggi)}')
print(f'Menghitung segitiga dengan fungsi, hasilnya ={hitung_luas_segitiga(15, 5)}')
print(f'Menghitung segitiga dengan fungsi, hasilnya ={hitung_luas_segitiga(55, 15)}')