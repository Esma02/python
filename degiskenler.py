isim='Esma'
mesaj=input("Mesajınız Nedir:")
print(mesaj,isim)


#Değişken Tanımlama 
kdv=0.18
urun1=2000
urun2=5000
urun1=urun1+(urun1*kdv)
print(urun1)
urun2=urun2+(urun2*kdv)
print(urun2)
print(urun1+urun2)

#Veri Tipleri
ad="Esma"
yas=23
ogrenci=True
print(type(ad))
print(type(yas))
print(type(ogrenci))
print("Ad:"+ad+" "+"Yas:"+str(yas)+" "+"Öğrenci mi:"+str(ogrenci))



#Veri tipi dönüşümleri
sayi1=int(input('Sayı1:'))
sayi2=int(input('Sayı2:'))
toplam=sayi1+sayi2
print(toplam)

x=int("10")
x=float("10.5")
x=str(True)
x=str(10)

print(x)



#UYGULAMALAR
#1-> Yarıçapı verilen dairenin alan ve çevresini hesaplayın
yaricap=float(input("Yarıçap:"))
pi=3.14
alan=pi*(yaricap*yaricap)
cevre=2*pi*yaricap
print("Alan:",alan)
print("Cevre:",cevre)




#2-> Kalvyeden girilen km bilgisinin mil cinsinden hesaplama
km=float(input("KM bilgisini Girin:"))
mil=km/1,609344
print((mil))