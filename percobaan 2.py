#Program Lift prototipe 2
x = 0 #x menandakan program berjalan atau tidak
posisi_0 = 1

# Program utama
while not x == -1: #Selama x bukan -1, program akan berjalan
    n = int(input("Jumlah orang di seluruh lantai yang akan naik lift: "))
    numpang = [0 for i in range (0, n)]
    minta = [0 for i in range (0, n)]
    dalam = [False for i in range (0, n)]
    if not n == -1: #Selama pengguna tidak memasukkan -1, x tidak akan menjadi -1
        for i in range (0, n):
            ok = False
            while ok == False:
                print("Masukkan posisi penumpang ke-" + str(i + 1) + " [1-10]: ", end="")
                numpang[i] = int(input())
                if not (numpang[i] < 0 or numpang[i] > 10):
                    while ok == False:
                        print("Masukkan lantai tujuan penumpang ke-" + str(i + 1) + " [1-10]: ", end="")
                        minta[i] = int(input())
                        if minta[i] == numpang[i]:
                            print("Mohon pilih lantai yang lain!")
                        elif not (minta[i] < 0 or minta[i] > 10):
                            ok = True 
                        else:
                            print("Lantai tidak valid")

        high = max(max(numpang), max(minta))
        low = min(min(numpang), min(minta))

        while posisi_0 <= high:
            print(posisi_0)
            for i in range (0, n):
                if posisi_0 == numpang[i] and dalam[i] == False:
                    dalam[i] = True
                    print("Penumpang " + str(i+1) + " naik ke lift")
            
            for i in range (0, n):
                if posisi_0 == minta[i] and dalam[i] == True:
                    numpang[i] = minta[i]
                    print("Penumpang " + str(i+1) + " turun dari lift")
            posisi_0 += 1
        
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

    else: #Saat pengguna memasukkan -1, x menjadi -1 dan program berhenti
        x = -1
        print("Keluar...")
                    
