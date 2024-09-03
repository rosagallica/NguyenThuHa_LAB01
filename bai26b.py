# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 11:44:23 2024

@author: ADMIN
"""

N = int(input("Nhập một số nguyên:"))
chuoi_so=str(N)
list_so=list(chuoi_so)
list_so.sort()
chuoi_ket_qua = "".join(list_so)
print (int(chuoi_ket_qua))