# -*- coding: utf-8 -*-
"""
Created on Mon Aug 12 19:15:53 2024

@author: NguyenThuyThuyLinh
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