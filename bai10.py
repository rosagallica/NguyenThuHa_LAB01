# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 09:16:39 2024

@author: ADMIN
"""

so_xe=int(input("Nhập số xe (4 chữ số):"))
if so_xe>9999:
    print("Không hợp lệ")
elif so_xe<=999:
    print("Không hợp lệ")
else:
    S=sum(int(chu_so) for chu_so in str(so_xe))
    so_nut=S%10
    print("Xe có số nút là:",so_nut)