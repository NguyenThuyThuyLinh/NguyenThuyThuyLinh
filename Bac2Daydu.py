# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 18:08:38 2024

@author: Nguyen Thuy Thuy Linh

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
