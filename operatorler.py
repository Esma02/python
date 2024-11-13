#operatör:Belirli koşul dahilinde 2 değişkeni karşılaştırma işlemi
#Aritmetik operatörler
a=10
b=20
sonuc=a+b
sonuc=a-b
sonuc=a*b
sonuc=a/b
sonuc=a%b    #mod
sonuc=a**b   #üs
sonuc=a//b   #kalan

print(sonuc)

#Atama Operatörleri
c,d,e=10,20,30
c+=5
c-=5
c*=5
c/=5
c%=5
c**=5
c //=5

print(c)

#Uygulama
f,g,h=4,8,(12,2)
i=int(input('1. sayı:'))
j=int(input('2. sayı:'))
carp=i*j
top=f+g+(h[0]+h[1])
k=carp-top
print(k)

n=(h[0]+h[1])//g
print(n)

m= f + g + (h[0] + h[1]) % 7
print(m)



#Karşılaştırma Operatörleri
a,b,c,d=2,2,10,5
mail='info@firat.com'
sifre='123'
sonuc= a==b
sonuc= a==c
sonuc= a!=b
sonuc=(mail==input('mail:'))
sonuc=(sifre==input('sifre:'))
sonuc=a>b
sonuc=a<=b

print(sonuc)


#Uygulama
#Girilen 2 sayıdan hangisi büyük
sayi1=int(input('1. Sayı:'))
sayi2=int(input('2. Sayı:'))
if sayi1>sayi2:
    print('sayi1 büyük')
print("Sayi2 büyük")
#sayının tek-çift kontrolü
if (sayi1%2==0):
    print("Çift")
else:
    print("Tek")



#Mantıksal Operatörler - and/or/not
x=2
sonuc=(x>10) and (x<1)
sonuc=(x>10) or (x<1)
#and
#T,T->T
#T,F->T
#F,F->F

#or
#T,T->T
#T,F->T
#F,F->F

#NOT
#F->T
#T->F
print(sonuc)

#uygulama
yas=int(input('yaşınız:'))
izin=True

# if yas<18 and izin ==True:
#     print("Çalışır")
# elif yas<18 and izin==False:
#     print("Çalışamaz")


#identitiy is ,is not ve membership in
x=[2,4,6]
y=[2,4,6]
z=y
print(x==y)
print(x is y)
print(x is not y)
print(z is y)
print(z is not y)

print(2 in x)
print(20 not in x)

