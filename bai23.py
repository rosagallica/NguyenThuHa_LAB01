# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 11:19:03 2024

@author: ADMIN
"""
import math
a = float(input("Nhập hệ số a:"))
b = float(input("Nhập hệ số b:"))
c = float(input("Nhập hệ số c:"))
delta=b**2 - 4*a*c
if delta > 0:
    x1 = (-b + math.sqrt(delta))/(2*a)
    x2 = (-b - math.sqrt(delta))/(2*a)
    print("PT có 2 nghiệm phân biệt: x1=",x1)
    print("x2=",x2)
elif delta == 0:
    x = -b/(2*a)
    print("PT có nghiệm kép: x=",x)
else:
    print("PT vô nghiệm.")