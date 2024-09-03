# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 11:38:13 2024

@author: ADMIN
"""

kytu=input("Nhập một ký tự:")
if kytu.islower():
    print(kytu.upper())
elif kytu.isupper():
    print(kytu.lower())
else:
    print("Không phải chữ cái.")