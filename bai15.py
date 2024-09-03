# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 09:47:11 2024

@author: ADMIN
"""

import math
a = float(input("Nhập số a:"))
b = float(input("Nhập số b:"))
if a==b:
    print("Lỗi: a và b không thể bằng nhau.")
else:
    tuso=((a+b)/(math.pow(a, 1/3)) + math.pow(b, 1/3)) - math.pow(a*b, 1/3)
    mauso=(math.pow(a, 1/3)-math.pow(b, 1/3))**2
    B=tuso/mauso
    print("Kết quả của biểu thức là:",B)