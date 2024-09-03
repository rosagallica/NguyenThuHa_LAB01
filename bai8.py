# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 09:07:56 2024

@author: ADMIN
"""

kg=float(input("Nhập cân nặng của bạn(kg):"))
m=float(input("Nhập chiều cao của bạn(m):"))
BMI=kg/(m**2)
print("Chỉ số BMI của bạn là:",BMI)
if BMI<18.5:
    print("Bạn đang bị thiếu cân.")
elif 18.5<=BMI<30:
    print("Bạn có cân nặng khỏe mạnh.")
elif 25<=BMI<30:
    print("Bạn đang bị thừa cân.")
else:
    print("Bạn đang bị béo phì.")