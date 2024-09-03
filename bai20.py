# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 11:07:48 2024

@author: ADMIN
"""

a = int(input("Nhập số thứ 1:"))
b = int(input("Nhập số thứ 2:"))
c = int(input("Nhập số thứ 3:"))
max_value = a
if b > max_value:
    max_value=b
if c > max_value:
    max_value=c
print("Số lớn nhất là:",max_value)