#Program Lift prototipe 2
x = 0 #x menandakan program berjalan atau tidak
posisi_0 = 1

# Program utama
while not x == -1: #Selama x bukan -1, program akan berjalan
    n = int(input("Jumlah orang di seluruh lantai yang akan naik lift: "))
    #isi list dengan 0 sebagai default
    numpang = [0 for i in range (0, n)] #posisi awal penumpang
    minta = [0 for i in range (0, n)] #tujuan
    dalam = [False for i in range (0, n)] #penumapng di dalam lift atau tidak
    if not n == -1: #Selama pengguna tidak memasukkan -1, x tidak akan menjadi -1
        for i in range (0, n):
            ok = False #nanti diganti break
            while ok == False:
                print("Masukkan posisi penumpang ke-" + str(i + 1) + " [1-10]: ", end="")
                numpang[i] = int(input())
                if not (numpang[i] < 0 or numpang[i] > 10): #memastikan lantai penumpang valid
                    while ok == False:
                        print("Masukkan lantai tujuan penumpang ke-" + str(i + 1) + " [1-10]: ", end="")
                        minta[i] = int(input())
                        if minta[i] == numpang[i]: #menghindari bug karena lantai awal dan tujuan sama
                            print("Mohon pilih lantai yang lain!")
                        elif not (minta[i] < 0 or minta[i] > 10):
                            ok = True #lanjut ke penumpang berikutnya, nanti ganti break
                        else:
                            print("Lantai tidak valid")

        high = max(max(numpang), max(minta)) #lantai tertinggi lift
        low = min(min(numpang), min(minta)) #dummy, belum jelas gunanya

        while posisi_0 <= high: #elevator terus naik ke high
            print(posisi_0)
            for i in range (0, n): #setiap lantai cek lantai awal dan tujuan penumpang
                if posisi_0 == numpang[i] and dalam[i] == False: #kalau ada penumpang di lantai ini, ambil
                    dalam[i] = True
                    print("Penumpang " + str(i+1) + " naik ke lift")
            
            for i in range (0, n):
                if posisi_0 == minta[i] and dalam[i] == True: #kalau ada tujuan di lantai ini, keluarkan
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
                    
