#Program Lift prototipe 2
posisi_0 = 1

# Program utama
while True: #Selama tidak ada perintah berhenti, program akan berjalan
    n = int(input("Jumlah orang di seluruh lantai yang akan naik lift (-1 untuk keluar): "))
    numpang = [0 for i in range (0, n)]
    minta = [0 for i in range (0, n)]
    dalam = [False for i in range (0, n)]
    sudah = [False for i in range (0, n)]
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

        while True:
            print("[NAIK]")
            print("Lantai " + str(posisi_0))
            for i in range (0, n):
                if numpang[i] == posisi_0 and not dalam[i] and not sudah[i]:
                    dalam[i] = True
                    print("Penumpang " + str(i+1) + " naik")
                
                if minta[i] == posisi_0 and dalam[i]:
                    dalam[i] = False
                    sudah[i] = True
                    print("Penumpang " + str(i+1) + " turun")
            
            if not any(dalam) and not any(posisi_0 < i for i in numpang + minta if i > posisi_0):
                break

            if posisi_0 < high:
                posisi_0 += 1
            else:
                break

        while True:
            print("[TURUN]")
            print("Lantai " + str(posisi_0))
            for i in range (0, n):
                if numpang[i] == posisi_0 and not dalam[i] and not sudah[i]:
                    dalam[i] = True
                    print("Penumpang " + str(i+1) + " naik")
                
                if minta[i] == posisi_0 and dalam[i]:
                    dalam[i] = False
                    sudah[i] = True
                    print("Penumpang " + str(i+1) + " turun")
            
            # Jika tidak ada penumpang lagi, keluar dari loop
            if not any(dalam) and not any(posisi_0 > i for i in numpang + minta if i < posisi_0):
                break
            
            if posisi_0 > low:
                posisi_0 -= 1
            else:
                break
    else: #Saat pengguna memasukkan -1, break loop
        print("Keluar...")
        break
