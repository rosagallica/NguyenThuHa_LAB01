# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 11:33:00 2024

@author: ADMIN
"""

gio = int(input("Nhập giờ:"))
phut = int(input("Nhập phút:"))
giay = int(input("Nhập giây:"))
if 0 <= gio <= 23 and 0 <= phut <= 59 and 0 <= giay <= 59:
    print ("Hợp lệ")
else: 
    print("Không hợp lệ")