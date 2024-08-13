# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 19:14:45 2024

@author: Nguyen Thuy Thuy Linh
"""
a = float(input("Nhập cạnh a: "))
b = float(input("Nhập cạnh b: ")) 
c = float(input("Nhập cạnh c: "))
 
if a + b > c and a + c > b and b + c > a: 
     print("a, b, c có thể là ba cạnh của một tam giác.") 
else: print("a, b, c không phải là ba cạnh của một tam giác.")
