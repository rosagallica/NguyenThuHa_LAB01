# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 11:10:05 2024

@author: ADMIN
"""

so = int(input("Nhập một số:"))
so_chuoi = ["không", "một", "hai", "ba", "bốn", "năm", "sáu", "bảy", "tám", "chín"]
if 0 <= so <= 9:
    print (so_chuoi[so])
else:
    print("Khong doc duoc")