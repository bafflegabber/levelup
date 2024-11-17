#Program Lift by LEVELUP
#Menginput data lantai awal dan tujuan untuk n penumpang, menentukan arah lift (naik/turun) berdasarkan lantai awal/tujuan terdekat, bergerak sampai lantai awal/tujuan tertinggi/terendah lalu mengubah arah lift sampai tidak ada lagi penumpang yang perlu dilayani
posisi_0 = 1 # Posisi awal lift (untuk run ke-1 program) adalah di lantai 1

# Program utama
while True: #Selama tidak ada perintah berhenti, program akan berjalan
    n = int(input("Jumlah orang di seluruh lantai yang akan naik lift (-1 untuk keluar): "))
    numpang = [0 for i in range (0, n)]
    minta = [0 for i in range (0, n)]
    dalam = [False for i in range (0, n)] # Asumsikan lift kosong untuk setiap awal perulangan
    sudah = [False for i in range (0, n)] # Asumsikan belum ada penumpang yang naik lift pada awal perulangan
    if not n == -1: #Selama pengguna tidak memasukkan -1, program berjalan
        for i in range (0, n):
            while True:
                print("Masukkan posisi penumpang ke-" + str(i + 1) + " [1-10]: ", end="")
                numpang[i] = int(input()) # Input lantai awal penumpang ke-i
                if not (numpang[i] < 0 or numpang[i] > 10):
                    while True:
                        print("Masukkan lantai tujuan penumpang ke-" + str(i + 1) + " [1-10]: ", end="")
                        minta[i] = int(input()) # Input lantai tujuan penumpang ke-i
                        if minta[i] == numpang[i]:
                            print("Mohon pilih lantai yang lain!") # Lantai awal dan tujuan tidak boleh sama
                        elif not (minta[i] < 0 or minta[i] > 10):
                            break
                        else:
                            print("Lantai tidak valid")
                    break
                else:
                    print("Lantai tidak valid")

        high = max(max(numpang), max(minta)) # Lantai tertinggi dari awal/tujuan
        low = min(min(numpang), min(minta)) # Lantai terendah dari awal/tujuan

        # Menentukan arah awal
        if posisi_0 <= low:
            naik = True # Lift naik saat posisi awal lift lebih rendah dari low
        elif posisi_0 >= high:
            naik = False # Lift turun saat posisi awal lift lebih tinggi dari high
        else:
            # Cari penumpang terdekat dari posisi lift
            terdekat = min(numpang + minta, key=lambda i: abs(i - posisi_0)) #tinjau dari jarak absolut
            naik = terdekat > posisi_0 #menentukan arah dari posisi lantai terdekat

        while any(not sudah[i] for i in range(n)): # Cek kalau ada penumpang yang belum dilayani
            if naik:
                print("[NAIK]")
                for lantai in range(posisi_0, high + 1):
                    print("Lantai " + str(posisi_0))
                    posisi_0 = lantai

                    # Proses naik/turun penumpang
                    for i in range(0, n): # Cek setiap sampai satu lantai
                        if numpang[i] == lantai and not dalam[i] and not sudah[i]: # Cek penmpang yang mau naik
                            dalam[i] = True # Penumpang di lantai naik jika dan hanya jika penumpang di luar dan belum pernah naik
                            print("Penumpang " + str(i+1) + " naik")
                        if minta[i] == lantai and dalam[i]: # Cek penumpang yang mau turun
                            dalam[i] = False
                            sudah[i] = True # Penumpang dinyatakan sudah pernah naik (mencegah bug agar tidak naik lagi)
                            print("Penumpang " + str(i+1) + " turun")
                naik = False  # Ganti arah setelah mencapai high
            else:
                print("[TURUN]")
                for lantai in range(posisi_0, low - 1, -1):
                    print("Lantai " + str(posisi_0))
                    posisi_0 = lantai
    
                    # Proses naik/turun penumpang
                    for i in range(0, n): # Cek setiap sampai satu lantai
                        if numpang[i] == lantai and not dalam[i] and not sudah[i]: # Cek penmpang yang mau naik
                            dalam[i] = True # Penumpang di lantai naik jika dan hanya jika penumpang di luar dan belum pernah naik
                            print("Penumpang " + str(i+1) + " naik")
                        if minta[i] == lantai and dalam[i]: # Cek penumpang yang mau turun
                            dalam[i] = False
                            sudah[i] = True # Penumpang dinyatakan sudah pernah naik (mencegah bug agar tidak naik lagi)
                            print("Penumpang " + str(i+1) + " turun")
                naik = True  # Ganti arah setelah mencapai dasar
    else: #Saat pengguna memasukkan -1, break loop
        print("Keluar...")
        break
