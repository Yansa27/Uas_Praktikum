# 3.Ada 5 kota yang saling terhubung oleh jalan setapak. Ada berapa rute berbeda yang bisa diambil untuk perjalanan dari kota A ke kota E, jika tidak boleh melalui kota yang sama lebih dari sekali?

def dfs(graf, saat_ini, dikunjunggi, jalur):
    dikunjunggi[saat_ini] = True
    jalur.append(saat_ini)

    if saat_ini == 'E' :
        print("Rute: ", ' -> '.join(jalur))
    else :
        for tetanga in graf[saat_ini]:
            if not dikunjunggi[tetanga]:
                dfs(graf, tetanga, dikunjunggi.copy(), jalur.copy())    


graf = {
    'A' : ['B'],
    'B' : ['A', 'C', 'D'],
    'C' : ['B', 'E'],
    'D' : ['B', 'E'],
    'E' : ['C', 'D']
}

kota_awal = 'A'
dikunjungi = {kota: False for kota in graf}
jalur = []


print('Rute-rute yang mungkin : ')
dfs(graf, kota_awal, dikunjungi, jalur)