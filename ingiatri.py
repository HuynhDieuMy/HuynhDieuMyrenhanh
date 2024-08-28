# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 19:23:44 2024

@author: Huynh Dieu My 
"""
giatri = {0: "Không",
1: "Một",
2: "Hai",
3: "Ba",
4: "Bốn",
5: "Năm",
6: "Sáu",
7: "Bảy",
8: "Tám",
9: "Chín"}
a = int(input("Nhập số: "))
if a >= 0 and a <= 9:
    print("Giá trị: ", giatri[a])
else:
    print("Không đọc được")