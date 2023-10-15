#Tapsiriq 4
saat=str(input("Saati daxil et:"))
nc1=[1,2,0]
nc2=[0,1,2,3,4,5,6,7,8,9]
nc3=[0,1,2,3,4,5]
a1=0
a2=0
a3=0
for j in range(len(nc1)):
    if nc1[j]==int(saat[0]):
        print("ilk eded dogrudur")
        a1=1
        for i in range(len(nc2)):
            if nc2[i]==int(saat[1]) and nc1[j]!=2:
                print("ikinci eded dogrudur")
                a2=1
                for g in range(len(nc3)):
                    if nc3[i]==int(saat[3]):
                        print("ucuncu eded dogrudur")
                        print("Saatiniz normaldi")
                        if nc3[g]==int(saat[3]):
                            a3=1
                        elif a3!=1 and i==5:
                            print("Eded Sehvdir")
            elif nc2[i]<5 and nc2[i]==int(saat[1]) and nc1[j]==2:
                print("ikinci eded dogrudur")
                a2=1
                for g in range(len(nc3)):
                    if nc3[i]==int(saat[3]):
                        print("ucuncu eded dogrudur")
                        print("Saatiniz normaldi")
                        exit(1)
            elif saat[1]==0:
                print("ikinci eded dogrudur")
                a2=1
                for g in range(len(nc3)):
                    if nc3[g]==int(saat[3]):
                        print("ucuncu eded dogrudur")
                        print("Saatiniz normaldi")
                        exit(1)
            elif a2!=1 and i==9:
                print("Eded sehvdir")
                exit(1)
    elif a1!=1 and 2==j:
        print("Eded Sehvdir") 
         