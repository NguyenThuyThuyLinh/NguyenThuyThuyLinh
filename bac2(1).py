# -*- coding: utf-8 -*-
"""
Created on Mon Aug 12 19:36:50 2024

@author: Nguyen Thuy Thuy Linh

"""
import math
a = float(input("Nhap gia tri a:"))
b = float(input("Nhap gia tri b:"))
c = float(input("Nhap gia tri c:"))
if  a==0 and b!=0 and c!=0:
    print("Phuong trinh co 1 nghiem duy nhat:x=", -c/b )
elif a!=0 and b*b-4*a*c<0:
       print("Phuong trinh vo nghiem")
elif a!=0 and b*b-4*a*c==0:
       print("Phuong trinh co 2 nghiem kep:x=" , -b/2*a)
else:
    x1= (-b-math.sqrt(b*b-4*a*c))/(2*a)
    x2= (-b+math.sqrt(b*b-4*a*c))/(2*a)
    print("Phuong trinh co hai nghiem la x:", x1,x2)