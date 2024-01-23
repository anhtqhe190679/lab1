a=int(input("Nhập số a: "))
b=int(input("Nhập số b: "))
c=int(input("Nhập số c: "))
minimum = min(a,b,c)
maximum = max(a,b,c)
print("Giá trị lớn nhất là: ",maximum)
print("Giá trị nhỏ nhất là: ",minimum)
if a > b:
    a, b = b, a
if b > c:
    b, c = c, b
if a > b:
    a, b = b, a
print("thứ tự của 3 số là: ",a,b,c)