class MhsTIF(object):
    def __init__(self, nama, umur, kota, us):
        self.nama = nama
        self.umur = umur
        self.kotaTinggal = kota
        self.uangSaku = us

    def __str__(self):
        x = self.nama + ', umur' + str(self.umur) \
            + '. Tinggal di ' + self.kotaTinggal \
            + '. Uang saku ' + str(self.uangSaku) \
            + 'tiap bulannya.'
        return x

    def ambilNama(self):
        return self.nama
    def ambilUmur(self):
        return self.umur
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

#1
def cariKota(target):
    z = []
    for i in Daftar:
        if i.kotaTinggal == target:
            hasil = Daftar.index(i)
            z.append(hasil)
    return z

#2
def cariTerkecil(Daftar):
    n = len(Daftar)
    terkecil = Daftar[0]
    for i in range(1,n):
        if Daftar[i].uangSaku < terkecil.uangSaku:
            terkecil = Daftar[i]

    return terkecil

#3
def cariTerkecil(Daftar):
    n = len(Daftar)
    terkecil = [Daftar[0]]
    for i in range(1,n):
        if Daftar[i].uangSaku < terkecil[0].uangSaku:
            terkecil = [Daftar[i]]
        elif Daftar[i].uangSaku == terkecil[0].uangSaku:
            terkecil.append(Daftar[i])
    return terkecil

#4
def cariDaftarUangSakuKurangdari(kumpulan):
    b = []  
    for i in kumpulan:
        if i.uangSaku < 300000:
            terkecil = i.uangSaku
            b.append(kumpulan.index(i))
    return b

#No5
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def pushAd(self, data_baru):
        node_baru = Node(data_baru)
        node_baru.next = self.head
        self.head = node_baru
    def pushAl(self, data):
        if(self.head == None):
            self.head = Node(data)
        else:
            current = self.head
            while (current.next != None):
                current = current.next
            current.next = Node(data)
        return self.head
    def insert(self, data, pos):
        node = Node(data)
        if not self.head:
            self.head = node
        elif posisi == 0:
            node.next = self.head
            self.head = node
        else:
            prev = None
            current = self.head
            current_pos = 0
            while(current_pos < pos) and current.next:
               prev = current
               current = current.next
               current_pos +=1
            prev.next = node
            node.next = current
        return self.head
    def search(self, v):
        current = self.head
        while current != None:
            if current.data == v:
                return "True"
            current = current.next
        return "False"
    def display(self):
        current = self.head
        while current != None:
            print(current.data)
            current = current.next

#6
def binSe(kumpulan, target):
    low = 0
    high = len(kumpulan) -1
    data = []
    while low <= high:
        mid = (high + low) //2
        if kumpulan[mid] == target:
            data.append(kumpulan.index(target))
            return True
        elif target < kumpulan[mid]:
            high = mid -1
        else :
            low = mid +1
    return False

#7
def binSearch(kumpulan, target):
    low = 0
    high = len(kumpulan) -1
    data = []
    while low != high:
        mid = (high + low) //2
        if kumpulan[mid] == target:
            break
        elif target < kumpulan[mid]:
            high = mid -1
        else :
            low = mid +1
    for i in range (low, high):
        if target == kumpulan[i]:
            data.append(i)
    return data

a = [2,3,5,6,6,6,8,9,9,10,11,12,13,13,14]

#8
def binSearching(kumpulan, target):
    low = 0
    high = len(kumpulan) -1
    while low <= high:
        mid = (high + low) //2
        if kumpulan[mid] == target:
            return mid
        elif kumpulan[mid] < target:
            high = mid +1
        else :
            low = mid -1
            
    return -1

b = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
