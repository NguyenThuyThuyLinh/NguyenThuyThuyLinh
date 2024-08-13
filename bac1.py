# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 18:15:34 2024

@author: Student
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