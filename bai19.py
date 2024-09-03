# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 11:00:40 2024

@author: ADMIN
"""

a = int(input("Nhập số thứ 1:"))
b = int(input("Nhập số thứ 2:"))
c = int(input("Nhập số thứ 3:"))
d = int(input("Nhập số thứ 4:"))
min_value = a
if b < min_value:
    min_value=b
if c < min_value:
    min_value=c
if d < min_value:
    min_value=d
print("Số nhỏ nhất là:",min_value)