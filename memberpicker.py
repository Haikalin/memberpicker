JKT48gen7 = ['Fiony','Flora','Oniel','Lulu','Adel']
Unfav = []
for i in range(len(JKT48gen7)) :
    Unfav.append([])


def initiate () :
    for i in range (len(JKT48gen7)//2) :
        angka = i*2
        print("""Pilih member: 
1. """+JKT48gen7[angka]+"""
2. """+JKT48gen7[angka+1])
        print("Masukkan pilhan:")
        pilihan = int(input())
        if pilihan == 1 :
            Unfav[angka].append(JKT48gen7[angka+1])
        else :
            Unfav[angka+1].append(JKT48gen7[angka])
            
def exe() :
    for i in range(len(JKT48gen7)) :
        for j in range(len(JKT48gen7)) :
            member1 = set()
            member2 = set()
            if i != j :
                if len(Unfav[i]) == len(Unfav[j]) :
                    member1.add(JKT48gen7[i])
                    member2.add(JKT48gen7[j])
                    if member1.issubset(set(Unfav[j])) or member2.issubset(set(Unfav[i])) :
                        if member1.issubset(set(Unfav[j])) :
                            unfavmem2 = set(Unfav[j]).union(set(Unfav[i]))
                            Unfav[j] = list(unfavmem2)
                            print(Unfav)
                        else :
                            unfavmem1 = set(Unfav[i]).union(set(Unfav[j]))
                            Unfav[i] = list(unfavmem1)
                            print(Unfav)
                    else :
                        print("""Pilih member: 
1. """+(JKT48gen7[i])+"""
2. """+(JKT48gen7[j]))
                        print("Masukkan pilihan: ")
                        pilihan = int(input())
                        if pilihan == 1 :
                            Unfav[i].append(JKT48gen7[j])
                            x = set(Unfav[i]).union(set(Unfav[j]))
                            Unfav[i] = list(x)
                            print(JKT48gen7)
                            print(Unfav)
                        else :
                            Unfav[j].append(JKT48gen7[i])
                            x = set(Unfav[j]).union(set(Unfav[i]))
                            Unfav[j] = list(x)
                            print(JKT48gen7)
                            print(Unfav)
                                                
initiate()
selesai = "false"
while selesai == "false" :
	cek = 0
	exe()
	jumlah = [0,0,0,0,0]
	for i in range(len(Unfav)) :
		jumlah[len(Unfav[i])] += 1
	for i in range(0,len(jumlah)) :
		if jumlah[i] != 1 :
			cek += 1
	if cek == 0 :
		selesai = "true"
print(Unfav)