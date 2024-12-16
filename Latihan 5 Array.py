def input_penumpang(n):
    numpang = [0 for _ in range(n)]
    minta = [0 for _ in range(n)]
    
    for i in range(n):
        while True:
            numpang[i] = int(input(f"Masukkan posisi penumpang ke-{i + 1} [1-10]: "))
            if 1 <= numpang[i] <= 10:
                while True:
                    minta[i] = int(input(f"Masukkan lantai tujuan penumpang ke-{i + 1} [1-10]: "))
                    if minta[i] != numpang[i] and 1 <= minta[i] <= 10:
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

def proses_lift(posisi_0, high, low, numpang, minta):
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
                    if numpang[i] == lantai and not dalam[i] and not sudah[i]:
                        dalam[i] = True
                        print(f"Penumpang {i + 1} naik")
                    if minta[i] == lantai and dalam[i]:
                        dalam[i] = False
                        sudah[i] = True
                        print(f"Penumpang {i + 1} turun")
            naik = False  # Ganti arah setelah mencapai high
        else:
            print("[TURUN]")
            for lantai in range(posisi_0, low - 1, -1):
                print(f"Lantai {lantai}")
                posisi_0 = lantai
                for i in range(n):
                    if numpang[i] == lantai and not dalam[i] and not sudah[i]:
                        dalam[i] = True
                        print(f"Penumpang {i + 1} naik")
                    if minta[i] == lantai and dalam[i]:
                        dalam[i] = False
                        sudah[i] = True
                        print(f"Penumpang {i + 1} turun")
            naik = True  # Ganti arah setelah mencapai dasar

def main():
    posisi_0 = 1  # Posisi awal lift
    while True:
        n = int(input("Jumlah orang di seluruh lantai yang akan naik lift (-1 untuk keluar): "))
        if n == -1:
            print("Keluar...")
            break
        
        numpang, minta = input_penumpang(n)
        high = max(max(numpang), max(minta))
        low = min(min(numpang), min(minta))
        proses_lift(posisi_0, high, low, numpang, minta)

if __name__ == "__main__":
    main()