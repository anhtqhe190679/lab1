import math
a=int(input("Nhập số a: "))
b=int(input("Nhập số b: "))
c=int(input("Nhập số c: "))
x=int(input("Nhập số x: "))
S1 = a*x**2 + b*x + c
print(S1) 

if b*b -4*a*c > 0:
    S2 == sqrt(b*b - 4*a*c)
else:
    S2 = 0
print(S2)

a = float(input("Nhập cạnh a: "))
b = float(input("Nhập cạnh b: "))
c = float(input("Nhập cạnh c: "))
if a + b > c and b + c > a and a + c > b:
    print("a, b, và c là độ dài của ba cạnh của một tam giác.")
    p = (a+b+c)/2
    S1 = math.sqrt(p*(p-a)*(p-b)*(p-c))
    print(S1)
else:
    print("a, b, và c không là độ dài của ba cạnh của một tam giác.")
