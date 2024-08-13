# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 20:03:37 2024

@author: Nguyen Thuy Thuy Linh
"""
Bai 1: Diem Trung binh 
"""distance = float(input("Nhap diem trung binh:"))
if distance <3.5:
    print("Hoc luc kem") 
 """
istance = float(input("Nhap diem trung binh:"))
if distance >=3.5 and distance <7 :
        print("Hoc luc yeu")
    """   
distance = float(input("Nhap diem trung binh:"))
if distance >=5 and distance <7 :
        print("Hoc luc Trung binh")
        """
Bai 2: Phuong trinh bac 1
Cach 1
"""
a = float(input("Nhap gia tri a:"))
b = float(input("Nhap gia tri b:"))
if a==0 and b==0:
    print("Phuong trinh vo so nghiem")
elif a==0 and b!=0:
    print("Phuong trinh vo nghiem")
else:
    x= -b/a
    print("Phuong trinh co nghiem la x:", x)
    """
Cach 2 
    """
    a = float(input("Nhap gia tri a:"))
b = float(input("Nhap gia tri b:"))
if a==0:
    if  b==0:
        print("Phuong trinh vo so nghiem")
    else:
        print("Phuong trinh vo nghiem")
else:
    x= -b/a
    print("Phuong trinh co nghiem la x:", x)
    """
Bai 3: Phuong trinh bac 2
Day du: 
    """
    import math

a = float(input("Nhap gia tri a: "))
b = float(input("Nhap gia tri b: "))
c = float(input("Nhap gia tri c: "))

if a == 0:
    if b != 0:
        print("Phuong trinh co 1 nghiem duy nhat: x =", -c / b)
    else:
        print("Phuong trinh vo nghiem")
else:
    delta = b * b - 4 * a * c
    if delta < 0:
        print("Phuong trinh vo nghiem")
    elif delta == 0:
        x = -b / (2 * a)
        print("Phuong trinh co 1 nghiem kep: x =", x)
    else:
        x1 = (-b - math.sqrt(delta)) / (2 * a)
        x2 = (-b + math.sqrt(delta)) / (2 * a)
        print("Phuong trinh co hai nghiem la x1:", x1)
        print("Phuong trinh co hai nghiem la x2:", x2)
        """
Rut gon
"""
import math
a = float(input("Nhap gia tri a:"))
b = float(input("Nhap gia tri b:"))
c = float(input("Nhap gia tri c:"))
delta = b * b - 4 * a * c
if a!=0:
    if delta < 0:
        print("Phuong trinh vo nghiem")
    elif delta == 0:
        x = -b / (2 * a)
        print("Phuong trinh co 1 nghiem kep: x =", x)
    else:
        x1 = (-b - math.sqrt(delta)) / (2 * a)
        x2 = (-b + math.sqrt(delta)) / (2 * a)
        print("Phuong trinh co hai nghiem la x1:", x1)
        print("Phuong trinh co hai nghiem la x2:", x2)
        """
Bai 4: Tam giac
Cau 1: 
    """
    a = float(input("Nhập cạnh a: "))
b = float(input("Nhập cạnh b: ")) 
c = float(input("Nhập cạnh c: "))
 
if a + b > c and a + c > b and b + c > a: 
     print("a, b, c có thể là ba cạnh của một tam giác.") 
else: print("a, b, c không phải là ba cạnh của một tam giác.")
"""
Cau 2:
    """
    a = float(input("Nhập cạnh a: "))
b = float(input("Nhập cạnh b: "))
c = float(input("Nhập cạnh c: "))
if (a + b c and a + c > b and b + c > a): 
    if a = b == c:
        print(" tam giác đều ")
    elif a*a + b*b == c*c or a*a + c*c == b*b or b*b + c*c == a*a:
        print(" tam giác vuông")
    elif a bor b == cora == c: 
        print(" tam giác cân")
    else:
        print(" đây là tam giác")
else:
     print(" đây không là tam giác")
     """
Bai 5: Tien taxi
"""
distance = float(input(" nhập số quãng đường taxi đi (km): "))

money = 3*13000+5*12000+ (distance 8)*10000 if distance > 0 and distance <= 1:

print("số tiền phải trả là 20000")

elif distance > 1 and distance < 4:

print("số tiền phải trả = ", distance*13000)

elif distance >= 4 and distance <= 8:

else:

print(" số tiền phải trả = ", 3*13000+ (distance - 3)*12000)

print(" số tiền phải trả = ", money)

if money > 100:

print(" số tiền phải trả sau cùng = ", money (money*0.08))
"""
Bai 6: keo bua bao:
    """
    import random
choices = ["kéo", "búa", "bao"] 
kq_người_chơi = input("Nhập kết quả người chơi: ")
if kq_người chơi not in ["kéo", "búa", "bao"]:
   print("kết quả không hợp lệ, nhập lại")
kq_may = random.choice(choices)
print(f"kết quả của máy {kq_may}")
if kq_người_chơi == kq_may:
   print("Hòa!")
elif (kq_người chơi == "búa" and kq_may == "kéo") or\ 
     (kq_người_chơi == "kéo" and kq_may = "bao") or\
     (kq_người_chơi == "bao" and kq_may == "búa"):
   print(" Bạn thắng")
else:
   print("Bạn thua")      
   """