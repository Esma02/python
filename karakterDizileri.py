kursAdi='Python ile Programlama'
kursAciklama='Güzel bir kurs'
kursSure='20 saat'
mesaj="kurs adı: "+kursAdi+" kurs açıklaması:"+kursAciklama
print(mesaj)

#Uygulama
#kursAdi içerisindeki karakter sayısı
print(len(kursAdi))
#kursAdi içerisindeki 'Python kelimesini al
print(kursAdi[0:6])
#Değişkendeki ilk 5 ve son 5 karakteri al
print(kursAdi[0:5]+" "+kursAdi[-5:])
#değişkeni tersten yazdır
print(kursAdi[::-1])
#tüm karakterleri küçük harfe çevir
print(kursAdi.lower())

 
print(kursAdi[0])  #İlk karakter
print(kursAdi[-1]) #Son karakter
adet = len(kursAdi)#Karakter Sayısı
print(adet)
print(kursAdi[adet-1])
print(kursAdi[0:6]) #0-5 karakteri al (Python)
print(kursAdi[11:]) #11'den başla sonuna kadar al
print(kursAdi[0:20:3]) #3 er atlayarak git
print(kursAdi[::2])
print(kursAdi[::-1])  #ters çevirir stringi



#string concat -> birleştirme
ad="Esma"
soyad="Bilir"
yas=23
ms="Adım "+ad+" "+soyad+" "+str(yas)+" yaşındayım."
print(ms)

#string format
msj="Adım {} {}. {} yaşındayım.".format(ad,soyad,yas)
print(msj)

#f-string
msj1=f"Adım {ad} {soyad}. {yas} yaşındayım."
print(msj1)

#Uygulama -> klavyeden girilen nota göre mesaj yazdırma
not1=int(input("1. not:"))
not2=int(input("2. not:"))
ad=input("Adınız:")
ort=int(not1+not2)/2
mesaj1="{} isimli öğrencinin 1. notu {} 2. notu {} ve ortalaması {} olarak hesaplanmıştır.".format(ad,not1,not2,ort)
mesaj2=f"{ad} isimli öğrencinin 1. notu {not1} 2. notu {not2} ve ortalaması {ort} olarak hesaplanmıştır."
print(mesaj1)
print(mesaj2)

#String Metotları
mesaj3="Python ile Programlama"
sonuc=mesaj3.upper()        #Harfleri büyütür
sonuc=mesaj3.lower()        #Küçültür
sonuc=mesaj3.title()        #Tüm kelimelerin baş harfini büyütür
sonuc=mesaj3.capitalize()   #Sadece ilk kelimenin baş harfini büyütür
sonuc=mesaj3.isupper()
sonuc=mesaj3.strip()        # Boşluk karakterlerini kaldırır
sonuc=mesaj3.split()        #Her boşluktan karakterleri ayırır.
sonuc=mesaj3.split(',')     #, den karakterleri ayır
sonuc=mesaj3.replace("Python","Java") #python->Java çevir
sonuc=mesaj3.count('a')     #a karakter sayısı

print(sonuc)
