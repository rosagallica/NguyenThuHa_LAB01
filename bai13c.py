# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 09:44:02 2024

@author: ADMIN
"""

ngay=int(input("Nhập ngày:"))
thang=int(input("Nhập tháng:"))
nam=int(input("Nhập năm:"))
if ngay>31:
    print("Không hợp lệ")
elif thang>12:
    print("Không hợp lệ")
else:
    ngay_thang_nam=f"{nam}/{thang}/{ngay}"
    print("Ngày sinh của bạn là:",ngay_thang_nam)