#Program Lift by LEVELUP
#Menginput data lantai awal dan tujuan untuk n penumpang, menentukan arah lift (naik/turun) berdasarkan lantai awal/tujuan terdekat, bergerak sampai lantai awal/tujuan tertinggi/terendah lalu mengubah arah lift sampai tidak ada lagi penumpang yang perlu dilayani

#definisi fungsi dan subprogram
def newreq():
    aff = input("Apakah ada permintaan baru saat ini? [y/n] ")
    while True:
        if aff.lower() == "y":
            order(q, posisi_0, lan)
            break
        elif aff.lower() == "n":
            return
        else:
            print("Input tidak valid.")

def yangmana(posisi_0, numpang, minta, state):
    if state[0] == 0:
        l = 0
    elif state[1] == 0:
        l = 1
    else:
        # Pilih lift yang lebih dekat ke lantai asal
        if abs(posisi_0[0] - numpang) <= abs(posisi_0[1] - numpang):
            l = 0
        else:
            l = 1
    print(f"Permintaan dialihkan ke lift " + str(l + 1))
    if minta > numpang:
        state[l] = 1
    else:
        state[l] = -1
    return l

def order(q, posisi_0, lan):
    global exit
    while True:
        numpang = int(input(f"Masukkan posisi penumpang [1-" + str(lan) + ", -1 untuk berhenti] : "))
        if 1 <= numpang <= lan:
            while True:
                minta = int(input(f"Masukkan lantai tujuan penumpang [1-" + str(lan) + ", -1 untuk berhenti] : "))
                if minta != numpang and 1 <= minta <= lan:
                    x = yangmana(posisi_0, numpang, minta, state)
                    q[x].append((numpang, minta))
                    pergerakan(x, numpang, minta)
                    break
                elif minta == -1:
                    exit = True
                    return
                else:
                    print("Lantai tidak valid!")
            break
        elif numpang == -1:
            exit = True
            return
        else:
            print("Lantai tidak valid")

def pergerakan(l, asal, tujuan):
    if not q[l]:
        return

    while q[l]:
        asal, tujuan = q[l].pop(0)

        # Gerakkan lift ke lantai asal
        while posisi_0[l] != asal:
            if posisi_0[l] < asal:
                posisi_0[l] += 1 
            else:
                posisi_0[l] += -1
            newreq()
            print(f"Lift {l + 1} di lantai {posisi_0[l]} (menuju asal: {asal}).")


        print(f"Lift {l + 1} menjemput penumpang di lantai {asal}.")

        # Gerakkan lift ke lantai tujuan
        while posisi_0[l] != tujuan:
            if posisi_0[l] < tujuan:
                posisi_0[l] += 1 
            else:
                posisi_0[l] += -1
            newreq()
            print(f"Lift {l + 1} di lantai {posisi_0[l]} (menuju tujuan: {tujuan}).")

        print(f"Lift {l + 1} menurunkan penumpang di lantai {tujuan}.")

    state[l] = 0
    

#algoritma
while True:
    lan = int(input("Jumlah lantai di gedung (> 1): "))
    if lan <= 1:
        print("Lift tidak akan berfungsi di gedung ini. Coba lagi.")
    else:
        break

posisi_0 = [1, 1]
state = [0, 0]
q = [[], []]
exit = False

while True:
    if exit == True:
        print("Keluar...")
        break
    # Tampilkan status lift dan permintaan saat ini
    print("Status Lift:")
    for i in range(2):
        if state[i] == 0:
            dis = "diam"
        elif state[i] == 1:
            dis = "naik"
        elif state[i] == -1:
            dis = "turun"
        print(f"Lift {i + 1}: Posisi: {posisi_0[i]}, Status: {dis}, Permintaan: {q[i]}")
    order(q, posisi_0, lan)
    