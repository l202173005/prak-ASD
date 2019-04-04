def swap(A,p,q):
    tmp = A[p]
    A[p] = A[q]
    A[q] = tmp

def cariPosisiYangTerkecil(A, dariSini, sampaiSini):
    posisiYangTerkecil = dariSini
    for i in range(dariSini+1, sampaiSini):
        if A[i]<A[posisiYangTerkecil]:
            posisiYangTerkecil = i
    return posisiYangTerkecil

def bubbleSort(A):
    n=len(A)
    for i in range(n-1):
        for j in range(n-i-1):
            if A[j]>A[j+1]:
                swap(A,j,j+1)


def selectionSort(A):
    n= len(A)
    for i in range(n-1):
        indexKecil=cariPosisiYangTerkecil(A,i,n)
        if indexKecil != i:
            swap(A,i,indexKecil)


def insertionSort(A):
    n=len(A)
    for i in range(1,n):
        nilai = A[i]
        pos=i
        while pos>0 and nilai<A[pos-1]:
            A[pos]=A[pos-1]
            pos=pos-1
        A[pos]=nilai


class MhsTIF(object):
    def __init__(self,nama,NIM,kota,us):
        """Metode inisiasi ini menutupi metode inisiasi di class Manusia"""
        self.nama = nama
        self.NIM = NIM
        self.kotaTinggal = kota
        self.uangSaku = us
    
    def __str__(self):
        x=str(self.NIM)+" "+self.nama+" "+self.kotaTinggal+" "+str(self.uangSaku)
        return x
    
    def ambilNama(self):
        return self.nama
    def ambilNim(self):
        return self.NIM
    def ambilKota(self):
        return self.kotaTinggal
    def ambilUangSaku(self):
        return self.uangSaku

c0 = MhsTIF('hujan', 10, 'Salatiga', 250000)
c1 = MhsTIF('angin', 11, 'Solo', 260000)
c2 = MhsTIF('fatin', 12, 'Surabaya', 300000)
c3 = MhsTIF('air', 25, 'Tangerang', 250000)
c4 = MhsTIF('langit', 30, 'Bogor', 350000)
c5 = MhsTIF('guntur', 40, 'Sidoarjo', 450000)
c6 = MhsTIF('awan', 16, 'Bandung', 650000)
c7 = MhsTIF('pelangi', 26, 'Surabaya', 2750000)
c8 = MhsTIF('rain', 41, 'Cilacap', 250000)
c9 = MhsTIF('could', 3, 'Semarang', 565000)
c10 = MhsTIF('wind', 8, 'Banjarmasin', 450000)

Daftar = [c0, c1, c2, c3, c4, c5, c6, c7, c8, c9, c10]

def MhsSort(A):
    n= len(A)
    for i in range(1,n):
        nilai = A[i]
        pos = i
        while pos>0 and nilai.NIM<A[pos-1].NIM:
            A[pos]=A[pos-1]
            pos=pos-1
        A[pos] = nilai

mhsSort(Daftar)
print('\n'.join(map(str, Daftar)))

A=[1,3,5,7,9]
B=[2,4,8,10,12]

def Kombinasi(a,b):
    c=a+b
    n=len(c)
    for i in range(1,n):
        nilai = c[i]
        pos = i
        while pos>0 and nilai<c[pos-1]:
            c[pos]=c[pos-1]
            pos=pos-1
        c[pos] = nilai
    print(c)   

from time import time as detak
from random import shuffle as kocok

def swap(A,p,q):
    tmp = A[p]
    A[p] = A[q]
    A[q] = tmp

def cariPosisiYangTerkecil(A, dariSini, sampaiSini):
    posisiYangTerkecil = dariSini
    for i in range(dariSini+1, sampaiSini):
        if A[i]<A[posisiYangTerkecil]:
            posisiYangTerkecil = i
    return posisiYangTerkecil

def bubbleSort(A):
    n=len(A)
    for i in range(n-1):
        for j in range(n-i-1):
            if A[j]>A[j+1]:
                swap(A,j,j+1)


def selectionSort(A):
    n= len(A)
    for i in range(n-1):
        indexKecil=cariPosisiYangTerkecil(A,i,n)
        if indexKecil != i:
            swap(A,i,indexKecil)


def insertionSort(A):
    n=len(A)
    for i in range(1,n):
        nilai = A[i]
        pos=i
        while pos>0 and nilai<A[pos-1]:
            A[pos]=A[pos-1]
            pos=pos-1
        A[pos]=nilai

k=[i for i in range(1,10001)]
kocok(k)
u_bub = k[:]
u_sel = k[:]
u_ins = k[:]

aw=detak();bubbleSort(u_bub);ak=detak();print('bubble: %g detik' %(ak-aw));
aw=detak();selectionSort(u_sel);ak=detak();print('selection: %g detik' %(ak-aw));
aw=detak();insertionSort(u_ins);ak=detak();print('insertion: %g detik' %(ak-aw));


