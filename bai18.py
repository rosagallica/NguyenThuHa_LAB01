# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 10:39:54 2024

@author: ADMIN
"""

h1=int(input("Nhập số giờ của khoảng thời gian thứ 1:"))
p1=int(input("Nhập số phút của khoảng thời gian thứ 1:"))
s1=int(input("Nhập số giây của khoảng thời gian thứ 1:"))
h2=int(input("Nhập số giờ của khoảng thời gian thứ 2:"))
p2=int(input("Nhập số phút của khoảng thời gian thứ 2:"))
s2=int(input("Nhập số giây của khoảng thời gian thứ 2:"))
tong_giay1=h1*3600 + p1*60 + s1
tong_giay2=h2*3600 + p2*60 + s2
ketqua=tong_giay1 + tong_giay2
ketqua=tong_giay1 - tong_giay2
print("Tổng và hiệu của phép toán là:",ketqua)
if ketqua < 0:
    print("Kết quả âm. Vui lòng kiểm tra lại dữ liệu.")
gio = ketqua//3600
phut = (ketqua%3600)//60
giay = ketqua%60
gio_phut_giay=f"{gio}:{phut}:{giay}"
print("giờ:phút:giây:",gio_phut_giay)