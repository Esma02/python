#Döngüler  for-> listeler / while->koşullar
#for döngüsü ->list


sayi=[1,2,3,4,5,6,7]
for i in sayi:
    print(i)
isim=['Esma','Mahmut','Ali','canan']
for isim in isim:
    print(isim)
ad='Canan'
for x in ad:
    print(x)
tuplem=[(1,2),(3,4),(5,6)]
for a,b in tuplem:
    print(a,b)
sozluk={"41":"kocaeli","34":"İstanbul"}
for s in sozluk.values():
    print(s)
for k in sozluk.keys():
    print(k) 
for a,b in sozluk.items():
    print(a,b)

#Uygulama
sayilar=[3,5,7,2,15,12,45]
for i in sayilar:
    print(i)

for kat in sayilar:
    if (kat % 3 ==0):
        print(kat)

topl=0
for top in sayilar:
    topl=top+topl
print(topl)

urun=["samsung s24","samsung s22","iphone 15","iphone 14"]
for u in urun:
    index = u.find("iphone")  #index kullanamayız hata veriyo
    if index>-1:
        print(u)





#while döngüsü ->koşullu işlemlerde
sayilar=[1,2,3,4,5,6,7,8,9]

i=0
while i<10:
    print(i)
    i+=1
i=1
while (i<len(sayilar)):
    print(sayilar[i])
    i+=1

#uygulama
# başlangıç ve bitiş değerlerini kullanıcıdan alacağız ve arasındaki tüm çift değerleri 
sayi1=int(input("başlangıç:"))
sayi2=int(input("bitiş:"))

i=sayi1
while (i<sayi2):
    if i%2==0:
        print(i)
        i+=1

#1-100 arasındaki sayıları azalan 
i=100
while(i>0):
    print(i)
    i-=1

#Uygulama

ogrenciler=[]
kosul="e"

while (kosul != "h"):
    no=input("Numarası")
    ograd=input("Adı:")
    ogrsoyad=input("Soyadı:")

    ogrenciler.append({
        "no":no,
        "ograd":ograd,
        "ogrsoyad":ogrsoyad
    })

    kosul=input("Devam mı (e/h)")

for ogr in ogrenciler:
    print(f"{no} numaralı {ograd} {ogrsoyad} isimli öğrenci")




#enumerate-> listedeki değişkenlerime index atama işlemi 
#zip -> iki listeyi birleştirmede kullanılır
