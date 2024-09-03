# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 11:41:09 2024

@author: ADMIN
"""

a = int(input("Nhập số thứ 1:"))
b = int(input("Nhập số thứ 2:"))
c = int(input("Nhập số thứ 3:"))
if b<a:
    a, b = b, a
if c<a:
    a, c = c, a
if c<b:
    b, c = c, b
print("Các số thep thứ tự tăng dần là:",a, b, c)        