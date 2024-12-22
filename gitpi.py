# Program Dual Lift System

# Posisi awal dan status kedua lift
lift_posisi = [1, 1]  # Lift pertama dan kedua mulai di lantai 1
lift_status = ["idle", "idle"]  # Status: "idle", "moving up", "moving down"

# Daftar permintaan untuk masing-masing lift
permintaan_lift = [[], []]  # permintaan_lift[0] untuk lift pertama, permintaan_lift[1] untuk lift kedua

# Fungsi untuk memproses permintaan

def proses_permintaan():
    global lift_posisi, lift_status, permintaan_lift

    while True:
        # Tampilkan status lift dan permintaan saat ini
        print("\nStatus Lift:")
        for i in range(2):
            print(f"Lift {i + 1}: Posisi: {lift_posisi[i]}, Status: {lift_status[i]}, Permintaan: {permintaan_lift[i]}")

        # Ambil input pengguna untuk permintaan baru
        pilihan = input("Masukkan lantai asal dan tujuan (format: asal-tujuan) atau 'q' untuk keluar: ")
        if pilihan.lower() == 'q':
            print("Program selesai.")
            break

        try:
            asal, tujuan = map(int, pilihan.split('-'))
        except ValueError:
            print("Format tidak valid. Gunakan format 'asal-tujuan'.")
            continue

        # Pilih lift untuk menangani permintaan
        if lift_status[0] == "idle":
            lift = 0
        elif lift_status[1] == "idle":
            lift = 1
        else:
            # Pilih lift yang lebih dekat ke lantai asal
            lift = 0 if abs(lift_posisi[0] - asal) <= abs(lift_posisi[1] - asal) else 1

        permintaan_lift[lift].append((asal, tujuan))
        lift_status[lift] = "moving up" if tujuan > asal else "moving down"

        # Proses pergerakan lift pertama
        proses_lift(0)

        # Cek permintaan baru di sepanjang jalur lift pertama
        for lantai in range(min(lift_posisi[0], tujuan), max(lift_posisi[0], tujuan) + 1):
            permintaan_baru = input(f"Apakah ada permintaan baru di lantai {lantai}? (y/n): ")
            if permintaan_baru.lower() == 'y':
                asal_baru, tujuan_baru = map(int, input("Masukkan lantai asal dan tujuan baru (format: asal-tujuan): ").split('-'))
                if (lift_status[0] == "moving up" and tujuan_baru < lift_posisi[0]) or \
                   (lift_status[0] == "moving down" and tujuan_baru > lift_posisi[0]):
                    print("Permintaan dialihkan ke lift kedua.")
                    permintaan_lift[1].append((asal_baru, tujuan_baru))
                    lift_status[1] = "moving up" if tujuan_baru > asal_baru else "moving down"
                else:
                    permintaan_lift[0].append((asal_baru, tujuan_baru))

        # Proses lift kedua jika ada permintaan
        proses_lift(1)

def proses_lift(lift):
    global lift_posisi, lift_status, permintaan_lift

    if not permintaan_lift[lift]:
        return

    while permintaan_lift[lift]:
        asal, tujuan = permintaan_lift[lift].pop(0)

        # Gerakkan lift ke lantai asal
        while lift_posisi[lift] != asal:
            lift_posisi[lift] += 1 if lift_posisi[lift] < asal else -1
            print(f"Lift {lift + 1} di lantai {lift_posisi[lift]} (menuju asal: {asal}).")

        print(f"Lift {lift + 1} menjemput penumpang di lantai {asal}.")

        # Gerakkan lift ke lantai tujuan
        while lift_posisi[lift] != tujuan:
            lift_posisi[lift] += 1 if lift_posisi[lift] < tujuan else -1
            print(f"Lift {lift + 1} di lantai {lift_posisi[lift]} (menuju tujuan: {tujuan}).")

        print(f"Lift {lift + 1} menurunkan penumpang di lantai {tujuan}.")

    lift_status[lift] = "idle"

# Jalankan program
proses_permintaan()
