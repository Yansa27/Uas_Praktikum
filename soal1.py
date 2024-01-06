# 1.Ada 3 orang: Ali, Budi, dan Chandra, di mana masing-masing membawa 3 kartu dengan angka berbeda. Ali mengatakan bahwa jumlah angka pada kartu-kartunya lebih dari 10. Budi mengatakan bahwa jumlah angka pada kartu-kartunya lebih kecil dari 10. Chandra mengatakan bahwa jumlah angka pada kartu-kartunya adalah 6. Jika diketahui bahwa hanya satu dari mereka yang berbohong, berapa total angka pada kartu-kartu Ali?

Ali = [8, 9 , 10] 
Budi = [1, 2, 3]
Chandra = [2, 3, 1]

def chehck_statements(Ali, Budi, Chandra):
    return ali>10, budi<10, ali + budi + chandra == 6

for ali in Ali:
    for budi in Budi:
        for chandra in Chandra:
            truth = chehck_statements(Ali, Budi, Chandra)
            if truth.count(True) == 1 and truth.count(False) == 2:
                print(f"Total angka pada kartu ali {ali}")

