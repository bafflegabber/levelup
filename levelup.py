#Program Lift by LEVELUP
#Menginput lantai awal dan tujuan untuk penumpang di gedung dengan  n lantai dan 2 lift, menentukan lift yang menjemput berdasarkan status dan jarak dari lantai penumpang

#definisi fungsi dan subprogram
def newreq(): #cek permintaan baru
    aff = input("Apakah ada permintaan baru saat ini? [y/n] ")
    while True:
        if aff.lower() == "y":
            order(q, posisi_0, lan)
            break
        elif aff.lower() == "n":
            return
        else:
            print("Input tidak valid.")

def yangmana(posisi_0, numpang, minta, state): #menentukan lift yang akan menjemput
    if state[0] == 0: #utamakan lift yang diam (state[i] == 0)
        l = 0
    elif state[1] == 0:
        l = 1
    else:
        #pilih lift yang lebih dekat ke lantai asal
        if abs(posisi_0[0] - numpang) <= abs(posisi_0[1] - numpang):
            l = 0
        else:
            l = 1
    print(f"Permintaan dialihkan ke lift " + str(l + 1))
    if minta > numpang: #ganti status lift berdasarkan arah gerak
        state[l] = 1  #ke atas
    else:
        state[l] = -1 #ke bawah
    return l

def order(q, posisi_0, lan): #input permintaan
    global exit #supaya var exit berubah juga di luar fungsi ini
    while True:
        numpang = int(input(f"Masukkan posisi penumpang [1-" + str(lan) + ", -1 untuk berhenti] : ")) #seperti proyek 1
        if 1 <= numpang <= lan:
            while True: #loop jaga2 input tidak sesuai
                minta = int(input(f"Masukkan lantai tujuan penumpang [1-" + str(lan) + ", -1 untuk berhenti] : "))
                if minta != numpang and 1 <= minta <= lan: #lantai hanya boleh 1 <= x <= lantai terdefinisi
                    x = yangmana(posisi_0, numpang, minta, state) #tentukan lift yang menerima permintaan
                    q[x].append((numpang, minta)) #masukkan permintaan ke list permintaan lift tersebut (q[i])
                    pergerakan(x, numpang, minta) #lift bergerak ke permintaan
                    break
                elif minta == -1: #-1 untuk keluar
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

def pergerakan(l, asal, tujuan): #pergerakan lift (disusun dengan bantuan ChatGPT)
    if not q[l]: #jika tidak ada permintaan, batalkan pergerakan
        return

    while q[l]: #selama ada permintaan, lift bergerak
        asal, tujuan = q[l].pop(0) #

        #gerakkan lift ke lantai asal
        while posisi_0[l] != asal:
            if posisi_0[l] < asal:
                posisi_0[l] += 1 
            else:
                posisi_0[l] += -1
            newreq() #cek permintaan baru di setiap lantai
            print(f"Lift {l + 1} di lantai {posisi_0[l]} (menuju asal: {asal}).")


        print(f"Lift {l + 1} menjemput penumpang di lantai {asal}.")

        #gerakkan lift ke lantai tujuan
        while posisi_0[l] != tujuan:
            if posisi_0[l] < tujuan:
                posisi_0[l] += 1 
            else:
                posisi_0[l] += -1
            newreq() #cek permintaan baru di setiap lantai
            print(f"Lift {l + 1} di lantai {posisi_0[l]} (menuju tujuan: {tujuan}).")

        print(f"Lift {l + 1} menurunkan penumpang di lantai {tujuan}.")

    state[l] = 0 #di lantai terakhir, lift [l] diam
    

#algoritma
while True: #loop jaga2 input tidak sesuai
    lan = int(input("Jumlah lantai di gedung (> 1): ")) #masukkan jumlah lantai
    if lan <= 1: #lift tidak mungkin beroperasi di gedung berlantai <=1
        print("Lift tidak akan berfungsi di gedung ini. Coba lagi.")
    else: #lanjut ke proses selanjutnya
        break

posisi_0 = [1, 1] #list menunjukkan posisi masing-masing lift (indeks 0 untuk lift 1, indeks 1 untuk lift 2)
state = [0, 0] #list menunjukkan status masing-masing lift (indeks 0 untuk lift 1, indeks 1 untuk lift 2)
q = [[], []] #list menunjukkan permintaan masing-masing lift (indeks 0 untuk lift 1, indeks 1 untuk lift 2)
exit = False #cek apakah program akan diberhentikan

while True:
    if exit == True: #untuk menghentikan program
        print("Keluar...")
        break
    #tampilkan status lift dan permintaan saat ini
    print("Status Lift:")
    for i in range(2):
        if state[i] == 0:
            dis = "diam"
        elif state[i] == 1:
            dis = "naik"
        elif state[i] == -1:
            dis = "turun"
        print(f"Lift {i + 1}: Posisi: {posisi_0[i]}, Status: {dis}, Permintaan: {q[i]}")
    order(q, posisi_0, lan) #proses input permintaan
    
