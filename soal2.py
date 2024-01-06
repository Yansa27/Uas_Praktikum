# 2.	Sebuah kapal berlayar ke arah utara selama 3 jam, kemudian berbelok ke barat selama 4 jam, dan berbelok lagi ke selatan selama 5 jam. Jika kecepatan kapal selalu sama, berapakah jarak total yang telah ditempuh kapal tersebut?
def hitung_jarak(kecepatan, waktu_utara, waktu_barat, waktu_selatan):
    jarak_utara = kecepatan * waktu_utara
    jarak_barat = kecepatan * waktu_barat
    jarak_selatan = kecepatan * waktu_selatan

    jarak_total = (jarak_utara**2 + jarak_barat**2 + jarak_selatan**2)**0.5
    return jarak_total


# kecepatan dan wkatu 
kecepatan_kapal = 30
utara = 3
barat = 4
selatan = 5

jarak_total = hitung_jarak(kecepatan_kapal, utara, barat, selatan)

#menampilkan output
print(f"Jarak toal yang telah di tempuh kapal adallah : {int(jarak_total)} kilometer")





