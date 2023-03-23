#Üç kenarı verilen üçgenin alan hesabı

a = float(input("Birinci kenarı giriniz: "))
b = float(input("İkinci kenarı giriniz: "))
c = float(input("Üçüncü kenarı giriniz: "))
u = (a+b+c)/2
alan = ((u)*(u-a)*(u-b)*(u-c))**0.5
print("Üçgenin alanı: ", alan)