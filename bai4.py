# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 07:32:31 2024

@author: ADMIN
"""

n=int(input("Nhập n là số nguyên dương có 2 chữ số: "))
if 9>n:
    print("Không hợp lệ")
elif n>99:
    print("Không hợp lệ")
else:
    print("Tổng chữ số là: ",n//10+n%10)