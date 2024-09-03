# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 11:15:11 2024

@author: ADMIN
"""

a = float(input("Nhập hệ số a:"))
b = float(input("Nhập hệ số b:"))
if a == 0:
    if b == 0:
        print("PT có vô số nghiệm.")
    else:
        print("PT vô nghiệm.")
else:
            x = -b/a
            print("PT có nghiệm duy nhất:",x)