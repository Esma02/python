 #if / if-else / if/elif/else blokları
#Arac yakıt tipine göre ne kadar yakıt masrafı bulma
#benzin:39.35 , dizel:41.71 , lpg:20.28
arac=input("Aracınızın Tipi ne(B/D/L):")
km=int(input("KM bilgisi:"))

if arac=='B':
    sonuc=km * 39.35
    print(sonuc)
elif arac=='D':
    sonuc=km * 41.71
    print(sonuc)
elif arac=='L':
    sonuc=km * 20.28
    print(sonuc)
else:
    print("Belirtilen formatta girin")


#öğrenci notu hesaplama
yazili1=int(input("1. Yazılı"))
yazili2=int(input("2. Yazılı"))
sozlu=int(input("Sözlü Notu:"))
ort=(yazili1+yazili2+sozlu)/3
if ort<24 and ort>0:
    print("0")
elif ort<44 and ort>25:
    print("1")
elif ort<54 and ort>45:
    print("2")
elif ort<69 and ort>55:
    print("3")
elif ort<70 and ort>84:
    print("4")
elif ort<85 and ort>100:
    print("5")
else:
    print("Notlarınızı kontrol edin")
