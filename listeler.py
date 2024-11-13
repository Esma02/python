ogrenci=["Esma","Bilir",70,80,90]
ort=(ogrenci[2]+ogrenci[3]+ogrenci[4]) / 3
print(ogrenci[0]+" "+ogrenci[1]+" "+str(ort))

ogrenciler=[["Esma","Bilir",70,80,90],["Mahmut","Bilir",70,80,90]]
print(ogrenciler[0])
print(ogrenciler[1])
print(ogrenciler[0][2])



#Liste Tnımlama
progDilleri=["Python","C#","Java"]
sonuc=type(progDilleri)
sonuc=progDilleri[0:2]
sonuc=progDilleri[:]
#Güncelleme
progDilleri[-1]="Php"
sonuc=progDilleri
sonuc=len(progDilleri)
sonuc=progDilleri+["Go","Delphi","React"]
sonuc="Python" in progDilleri
for i in progDilleri:
    print(i)
del progDilleri[0]

print(sonuc)




#Uygulama
araba=["Toyota","Bmw","Renault",'Mercedes']
a = len(araba)
a=araba[0]+" "+araba[-1]
araba[2]="Togg"
a=araba
a=araba[:2]
a=araba+["Ford","Citroen"]
del araba[-1]

print(a)


#Liste Metotları
sayilar=[4,5,7,12,1,0,32,5,654,4]
isimler=["Esma","Ayşenur","Berfin"]
sonuc=min(sayilar)
sonuc=min(isimler)
sonuc=max(sayilar)
sonuc=max(isimler)
#ekleme
sayilar.append(1000)
isimler.append("Şeyma")
sonuc= isimler
sayilar.insert(0,14)
sonuc=sayilar
#silme
sayilar.pop(2)
isimler.remove("Berfin")
#sıralama
sayilar.sort()
isimler.sort()

sonuc=isimler.count("Esma")
sonuc=sayilar.count(100)
sonuc=sayilar.index(4)
print(sonuc)

#Uygulama
customers=['esma','ayse','seyma']
order=[120,150,200]



#Listeden farkı değiştirilemez olması,index ve count metotları tek var
liste=[1,2,3]
tuple=(1,2,3)

print(type(liste))
print(type(tuple))



#Dictionary {key:value}  güncellenebilir,tekrarlanamaz
plaka={"Kocaeli":41,
       "Adıyaman":2,
       "İstanbul":34}
print(plaka['Adıyaman'])
plaka['İzmir']=36 #yeni değer ekleme


print(plaka)


#Uygulama
ogrenci={
        101:{
            'Ad':'Yiğit Bilgi',
            'yil':2010,
            'not':(40,80,90)
        },
        102:{
            'Ad':'Ada Bilgi',
            'yil':2012,
            'not':(80,80,80)
        },
        103:{
            'Ad':'Çınar Turan',
            'yil':2017,
            'not':(70,70,70)
        }
}

a=int(input('Öğrenci no:'))
print(ogrenci[a])
#metotlar
sonuc=ogrenci[101]
sonuc=ogrenci.get(101)
sonuc=ogrenci.keys()
sonuc=ogrenci.items()

ogrenci[102]=105 #güncelleme
ogrenci.pop(101) #silme  clear:tamamını silme
sonuc=ogrenci

print(sonuc)




#Sets  indekslenemez,güncellenemez,tekrarlanmaz,eleman siler ekleriz
meyve={"elma","armut","kiraz","elma"}
meyve2={"elma","armut","kiraz","kavun"}


for i in meyve:
    print(i)

sonuc="elma"in meyve
meyve.add("şeftali")
meyve.update(meyve2)    #birleştirme
meyve.remove("elma")    #silme
meyve.discard("armut")  #silme   yoksa hata vermez 
meyve.pop()             #silme olayı random
meyve.clear()

sonuc=meyve
print(sonuc)



#değer tipler - veriler eşitlenir
x=20
y=10
x=y
y=30
print(x,y)

#referans tipler - verinin adresi eşitlenir yani değer değiştiğinde diğerinde de değişim olur
a=["elma"]
b=["armut"]
a=b            #adres kopyalama
a[0]='üzüm'
print(a,b)

#liste kopyalama - referans tipini değer tipine dönüştürme
listA=[10,20],
listB=list(listA)()
listB[0]=30

print(listA,listB)











