#Tapsiriq 1
money=int(input("Pul membelegini daxil et:"))
convert=int(input("Pulu Avroya(1) Rubla(2) Dollara(3) cevir:"))
def moneyconverter(m,c):
    if c==1:
        print(f"Your money in Euro equals to {m*0.56}")
    elif c==2:
        print(f"Your money in Dollar equals to {m*0.59}")
    elif c==3:
        print(f"Your money in Rub equals to {m*57.47}")
    else:
        print("Please enter normal money qurrencies")
moneyconverter(money,convert)

#Tapsiriq 2
qr=int(input("Zehmet olmasa qrami daxil et:"))
if qr>0 and qr<100:
    print(f"Size endirim dusmur qiymet {qr}")
elif qr>100 and qr<200:
    print(f"Size endirim dusur qiymet {qr-((qr/100)*3)}")
elif qr>200 and qr<300:
    print(f"Size endirim dusur qiymet {qr-((qr/100)*5)}")
else:
    print(f"Size endirim dusur qiymet {qr-((qr/100)*7)}")

#Tapsiriq 3
eded=str(input("Ededi daxil et ve ededin kesr hissesinin tam olub olmadigini deyim:"))
parts = eded.split(',')
if parts[0]=="0":
    print("Ededin tam hissesi yoxdur")
else:
    print("Ededinin tam hissesi var")

#Tapsiriq 5
#Dolça bürcü tarixi – 21 yanvar – 18 fevral
#Balıqlar bürcü tarixi – 19 fevral – 20 mart
#Qoç bürcü tarixi – 21 mart – 20 aprel
#Buğa bürcü tarixi – 21 aprel – 20 may
#Əkizlər bürcü tarixi – 21 may – 21 iyun
#Xərçəng bürcü tarixi – 22 iyun – 22 iyul
#Şir bürcü tarixi – 23 iyul – 22 avqust
#Qız bürcü tarixi – 23 avqust – 22 sentyabr
#Tərəzi bürcü tarixi – 23 sentyabr – 23 oktyabr
#Əqrəb bürcü tarixi – 24 oktyabr – 22 noyabr
#Oxatan bürcü tarixi – 23 noyabr – 21 dekabr
#Oğlaq bürcü tarixi – 22 dekabr – 20 yanvar

month=input("Doguldugun ayi qeyd et:")
day=int(input("Doguldugun gunu qeyd et(0-31):"))

if month.lower()=="january":
    print("Dolça"if (day>=21) else "Oglaq")
elif month.lower()=="february":
    print("Dolça"if (day<=18) else "Baliq")
elif month.lower()=="march":
    print("Baliqlar"if (day<=20) else "Qoc")
elif month.lower()=="april":
    print("Qoc"if (day<=20) else "Buga")
elif month.lower()=="may":
    print("Buga"if (day<=20) else "Ekizler")
elif month.lower()=="june":
    print("Ekizler"if (day<=21) else "Xerceng")
elif month.lower()=="july":
    print("Xerceng"if (day<=22) else "Sir")
elif month.lower()=="august":
    print("Sir"if (day<=22) else "Qiz")
elif month.lower()=="september":
    print("Qiz"if (day<=22) else "Terezi")    
elif month.lower()=="october":
    print("Terezi"if (day<=23) else "Eqreb")
elif month.lower()=="november":
    print("Eqreb"if (day<=22) else "Oxatan")
elif month.lower()=="december":
    print("Oxatan"if (day<=21) else "Oglaq")