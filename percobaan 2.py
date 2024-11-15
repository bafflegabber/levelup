#Program Lift prototipe 2
posisi_0 = 1

# Program utama
while True: #Selama tidak ada perintah berhenti, program akan berjalan
    n = int(input("Jumlah orang di seluruh lantai yang akan naik lift (-1 untuk keluar): "))
    numpang = [0 for i in range (0, n)]
    minta = [0 for i in range (0, n)]
    dalam = [False for i in range (0, n)]
    if not n == -1: #Selama pengguna tidak memasukkan -1, program berjalan
        for i in range (0, n):
            while True:
                print("Masukkan posisi penumpang ke-" + str(i + 1) + " [1-10]: ", end="")
                numpang[i] = int(input())
                if not (numpang[i] < 0 or numpang[i] > 10):
                    while True:
                        print("Masukkan lantai tujuan penumpang ke-" + str(i + 1) + " [1-10]: ", end="")
                        minta[i] = int(input())
                        if minta[i] == numpang[i]:
                            print("Mohon pilih lantai yang lain!")
                        elif not (minta[i] < 0 or minta[i] > 10):
                            break
                        else:
                            print("Lantai tidak valid")
                    break
                else:
                    print("Lantai tidak valid")

        high = max(max(numpang), max(minta))
        low = min(min(numpang), min(minta))

        if posisi_0 <= numpang[0]:
            while posisi_0 <= high: #lift akan naik hanya sampai lantai penumpang/tujuan tertinggi
                print(posisi_0)
                for i in range (0, n):
                    if posisi_0 == numpang[i] and dalam[i] == False:
                        dalam[i] = True
                        print("Penumpang " + str(i+1) + " naik ke lift")
                
                for i in range (0, n):
                    if posisi_0 == minta[i] and dalam[i] == True:
                        dalam[i] = False
                        numpang[i] = minta[i]
                        print("Penumpang " + str(i+1) + " turun dari lift")
                if not posisi_0 == high:
                    posisi_0 += 1
                else:
                    break
            
            if not low == numpang[0] or low == minta[0]:
                while posisi_0 >= low:
                    print(posisi_0)
                    for i in range (0, n):
                        if posisi_0 == numpang[i] and dalam[i] == False:
                            dalam[i] = True
                            print("Penumpang " + str(i+1) + " naik ke lift")
                    
                    for i in range (0, n):
                        if posisi_0 == minta[i] and dalam[i] == True:
                            dalam[i] = False
                            print("Penumpang " + str(i+1) + " turun dari lift")
                    posisi_0 -= 1
        else:
            while posisi_0 >= low:
                print(posisi_0)
                for i in range (0, n):
                    if posisi_0 == numpang[i] and dalam[i] == False:
                        dalam[i] = True
                        print("Penumpang " + str(i+1) + " naik ke lift")
                
                for i in range (0, n):
                    if posisi_0 == minta[i] and dalam[i] == True:
                        dalam[i] = False
                        print("Penumpang " + str(i+1) + " turun dari lift")
                posisi_0 -= 1
            
            if not high == numpang[0] or high == minta[0]:
                while posisi_0 <= high: #lift akan naik hanya sampai lantai penumpang/tujuan tertinggi
                    print(posisi_0)
                    for i in range (0, n):
                        if posisi_0 == numpang[i] and dalam[i] == False:
                            dalam[i] = True
                            print("Penumpang " + str(i+1) + " naik ke lift")
                    
                    for i in range (0, n):
                        if posisi_0 == minta[i] and dalam[i] == True:
                            dalam[i] = False
                            numpang[i] = minta[i]
                            print("Penumpang " + str(i+1) + " turun dari lift")
                    if not posisi_0 == high:
                        posisi_0 += 1
                    else:
                        break

    else: #Saat pengguna memasukkan -1, break loop
        break
        print("Keluar...")
