# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 07:33:31 2024

@author: ADMIN
"""

gio=int(input("Số giờ= "))
phut=int(input("Số phút= "))
giay=int(input("Số giây="))
if gio>24:
    print("Không hợp lệ")
elif phut>60:
    print("Không hợp lệ")
elif giay>60:
    print("Không hợp lệ")
else:
    gio_phut_giay=f"{gio}:{phut}:{giay}"
    print("hh:mm:ss:",gio_phut_giay)
    print("Tổng số giây là: ",gio*3600+phut*60+giay)