#1
def cetakSiku (x):
    for i in range (x+1):
        print ("*" *i)
#2
def gambarlahPersegiEmpat (x,y):
    for i in range (x):
        if i == 0 or i == x-1:
            print ('@'*y)
        else:
            print ('@'+' '*(y-2)+'@')
#3
def JumlahHurufVokal(string):
    vok =0
    x = "aiueoAIUEO"
    for n in string.lower ():
        if n in x:
            vok+=1
    vokal = len(string)
    return(vokal,vok)

def JumlahHurufKonsonan(x):
    con=0
    for n in x:
        if n in "qwrtypsdfghjklzxcvbnmQWRTYPSDFGHJKLZXCVBNM":
            con+=1
    return(len(x),con)

#4
def rerata (b):
    v = 0
    hai =[]
    for i in b:
        v=v+i
    return (v/len (b))

#5
from math import sqrt as sq
def apakahPrima(n):
    n = int(n)
    assert n>=0
    primaKecil = [2,3,5,7,11]
    bukanPrKecil = [0,1,4,6,8,9,10]
    if n in primaKecil:
        return True
    elif n in bukanPrKecil:
        return False
    else:
        for i in range(2,int(sq(n))+1):
            if(n%i==0):
                return False
        return True
print(apakahPrima(17))
print(apakahPrima(97))
print(apakahPrima(123))

#6
def BilanganPrima():
    prima=[]
    for i in range(2,1000):
        a = True
        for n in prima:
            if(i%n==0):
                a=False
                break
        if(a):
            print(i)
            prima.append(i)
    bilanganprima()

#7
def FaktorPrima(x):
    prima=[]
    for i in range(2,x):
        a = True
        for n in prima:
            if(i%n==0):
                a=False
                break
        if a and x%i==0:
            prima.append(i)
    return prima
    print(faktorprima(10))

#8
def Terkandung (a,b):
    return a in b

#9
def cetak():
    for i in range(1,100):
        if(i%3==0 and i%5==0):
            print('Python UMS')
        elif(i%5==0):
            print('UMS')
        elif(i%3==0):
            print('Python')
        else:
            print(i)
            
            
#10
def selesaikanABC(a,b,c):
    d=(b**2)-(4*a*c)
    if d<0:
        return "Determinan negatif. Persamaan tidak memiliki akar real."
    return  "Determinan positif"
print(selesaikanABC(1,2,3))

#11
def apakahKabisat(n):
    if(n%400==0):
        return True
    if(n%100==0):
        return False
    if(n%4==0):
        return True
    return False
print(apakahKabisat(2000))

#12
import random

print ("Permainan tebak angka\nSaya menyimpan sebuah angka bulat antara 1 sampai 100. Coba tebak.")

x = 0
coba = 1
jawaban = random.randint(0,100)
i=0
while x <= 1:
    i=i+1
    inp = int(input("Masukkan tebakan ke-{0} :".format(i)))
    if inp < jawaban:
        print ("Itu terlalu kecil. Coba lagi")
        coba += 1
        
    elif inp == jawaban:
        print ("Ya. Anda benar")
        
        x += 1
        coba += 1
    else:
        print ("Itu terlalu besar. Coba lagi")
coba += 1


#13
def katakan(angka):
    satuan = ["satu", "dua", "tiga", "empat", "lima",
              "enam", "tujuh", "delapan", "sembilan", "sepuluh",
              "sebelas", "dua belas", "tiga belas", "empat belas", "lima belas",
              "enam belas", "tujuh belas", "delapan belas", "sembilan belas"
              ]
    angka = '{:0,.0f}'.format(int(angka))
    angka = angka.split(",")
    katakan = []
    idx = 1
    for x in angka[::-1]:
        seribu = False
        if idx == 2 and x[-1]!="0":
            if int(x)< 2 :
                katakan.append("seribu")
                seribu = True
            else:
                katakan.append("ribu")
        if idx == 3 and x[-1]!="0":
            katakan.append("juta")
        if seribu == False:
            if int(x[-2:])<20 and int(x[-2:])>0:
                katakan.append(satuan[int(x[-2:])-1])
            elif int(x[-2:])>0:
                if int(x[-1])!=0:
                    katakan.append(satuan[int(x[-1])-1])
                if int(x[-2]) != 0:
                    katakan.append(satuan[int(x[-2])-1]+" puluh")
        if int(x[0]) > 2 and len(x)==3 :
            katakan.append(satuan[int(x[0])-1]+" ratus")
        elif len(x)==3 and int(x[0])!=0 :
            katakan.append("seratus")
        idx+=1

return " ". join(katakan[::-1])

#14
def formatRupiah(n):
    x = '{:,}'.format(n).replace(',', '.')
    return "Rp " + x
formatRupiah(1500)