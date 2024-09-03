# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 11:47:12 2024

@author: ADMIN
"""

import math
hinh = input("Nhập hình (v:vuông, n:chữ nhật, t:tròn):")
if hinh == "v":
    canh=float(input("Nhập độ dài cạnh:"))
    C=4*canh
    S=canh*canh
elif hinh == "n":
    chieudai=float(input("Nhập chiều dài:"))
    chieurong=float(input("Nhập chiều rộng:"))
    if chieudai <= chieurong:
        print("Không hợp lệ")
    else:
        C=2*(chieudai + chieurong)
        S=chieudai*chieurong
elif hinh == "t":
    bankinh=float(input("Nhập bán kính:"))
    C=2*math.pi*bankinh
    S=math.pi*bankinh*bankinh
else:
    print("Hình không hợp lệ.")
print("Chu vi:",C)
print("Diện tích:",S)
                