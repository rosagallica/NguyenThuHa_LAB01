# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 09:15:25 2024

@author: ADMIN
"""

print("===========MENU===========\n"
      "1. Hu tieu\n"
      "2. Chao long\n"
      "3. Banh canh\n"
      "4. Bun rieu\n"
      "5. Pho bo\n"
      "==========================\n")
c=float(input("Mời nhập lựa chọn: "))
if c==1:
    print("Món bạn chọn là: Hủ tiếu")
elif c==2:
    print("Món bạn chọn là: Cháo lòng")
elif c==3:
    print("Món bạn chọn là: Bánh canh")
elif c==4:
    print("Món bạn chọn là: Bún riêu")
elif c==5:
    print("Món bạn chọn là: Phở bò")
else:
    print("Không có món nào")