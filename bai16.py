# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 10:25:10 2024

@author: ADMIN
"""

h=int(input("Số giờ:"))
p=int(input("Số phút:"))
s=int(input("số giây:"))
if h>24:
    print("Không hợp lệ")
elif p>60:
    print("Không hợp lệ")
elif s>60:
    print("Không hợp lệ")
else:
    tong_giay = h*3600 + p*60 + s
    print("Tổng số giây là:",tong_giay)