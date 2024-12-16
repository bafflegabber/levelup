#Program Lift by LEVELUP
#Menginput data lantai awal dan tujuan untuk n penumpang, menentukan arah lift (naik/turun) berdasarkan lantai awal/tujuan terdekat, bergerak sampai lantai awal/tujuan tertinggi/terendah lalu mengubah arah lift sampai tidak ada lagi penumpang yang perlu dilayani

#definisi fungsi dan subprogram
def penumpangan(n, lan):
    numpang = [0 for i in range(n)]
    minta = [0 for i in range(n)]
    
    for i in range(n):
        while True:
            numpang[i] = int(input(f"Masukkan posisi penumpang ke-{i + 1} [1-" + str(lan) + "] : "))
            if 1 <= numpang[i] <= lan:
                while True:
                    minta[i] = int(input(f"Masukkan lantai tujuan penumpang ke-{i + 1} [1-" + str(lan) + "] : "))
                    if minta[i] != numpang[i] and 1 <= minta[i] <= lan:
                        break
                    else:
                        print("Mohon pilih lantai yang lain atau lantai tidak valid!")
                break
            else:
                print("Lantai tidak valid")
    
    return numpang, minta

def tentukan_arah(posisi_0, low, high, numpang, minta):
    if posisi_0 <= low:
        return True  # Naik
    elif posisi_0 >= high:
        return False  # Turun
    else:
        terdekat = min(numpang + minta, key=lambda i: abs(i - posisi_0))
        return terdekat > posisi_0  # Naik jika terdekat lebih tinggi

def masukkeluar(i, numpang, dalam, sudah, minta, lantai):
    if numpang[i] == lantai and not dalam[i] and not sudah[i]: # Cek penmpang yang mau naik
        dalam[i] = True # Penumpang di lantai naik jika dan hanya jika penumpang di luar dan belum pernah naik
        print("Penumpang " + str(i+1) + " naik")
    if minta[i] == lantai and dalam[i]: # Cek penumpang yang mau turun
        dalam[i] = False
        sudah[i] = True # Penumpang dinyatakan sudah pernah naik (mencegah bug agar tidak naik lagi)
        print("Penumpang " + str(i+1) + " turun")

def naikturun(posisi_0, high, low, numpang, minta):
    n = len(numpang)
    dalam = [False] * n
    sudah = [False] * n
    naik = tentukan_arah(posisi_0, low, high, numpang, minta)

    while any(not sudah[i] for i in range(n)):
        if naik:
            print("[NAIK]")
            for lantai in range(posisi_0, high + 1):
                print(f"Lantai {lantai}")
                posisi_0 = lantai
                for i in range(n):
                    masukkeluar(i, numpang, dalam, sudah, minta, lantai)
            naik = False  # Ganti arah setelah mencapai high
        else:
            print("[TURUN]")
            for lantai in range(posisi_0, low - 1, -1):
                print(f"Lantai {lantai}")
                posisi_0 = lantai
                for i in range(n):
                    masukkeluar(i, numpang, dalam, sudah, minta, lantai)
            naik = True  # Ganti arah setelah mencapai dasar

#algoritma
posisi_0 = 1  # Posisi awal lift
while True:
    lan = int(input("Jumlah lantai di gedung: "))
    if lan <= 1:
        print("Terus liftnya buat apa bro?")
    else:
        break

while True:
    n = int(input("Jumlah orang di seluruh lantai yang akan naik lift (-1 untuk keluar): "))
    if n == -1:
        print("Keluar...")
        break
    
    numpang, minta = penumpangan(n, lan)
    high = max(max(numpang), max(minta))
    low = min(min(numpang), min(minta))
    naikturun(posisi_0, high, low, numpang, minta)
