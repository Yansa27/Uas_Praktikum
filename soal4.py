# 4.Ada 8 bola berwarna hitam dan 8 bola berwarna putih di dalam sebuah kantong. Kita mengambil bola secara acak tanpa melihat ke dalam kantong. Hitunglah probabilitas mengambil 3 bola hitam secara berurutan.

def hitung_probabilitas():
    jumlah_bola_hitam = 8
    jumlah_bola_putih = 8

    total_bola = jumlah_bola_hitam + jumlah_bola_putih

    probabilitas_pertama = jumlah_bola_hitam / jumlah_bola_putih
    probabilitas_kedua = (jumlah_bola_hitam - 1) / (total_bola -1)
    probabilitas_ketiga = (jumlah_bola_hitam - 2) / (total_bola - 2)

    probabilitas_total = probabilitas_pertama * probabilitas_kedua * probabilitas_ketiga

    return probabilitas_total

hasil_probabilitas = hitung_probabilitas()
print(f"Probabilitas mengambil 3 bola hitam secara berurutan adallah {hasil_probabilitas:.4f}")