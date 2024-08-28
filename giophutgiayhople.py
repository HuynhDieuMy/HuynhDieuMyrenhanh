# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 22:52:44 2024

@author: Huynh Dieu My 
"""

gio = float(input("Nhập vào giờ: "))
phut = float(input("Nhập vào phút: "))
giay = float(input("Nhập vào giây: "))
if gio < 24 and gio >= 0 and phut < 60 and phut >= 0 and giay < 60 and giay >=0:
    print("Giờ,phút, giây hợp lệ")
else:
    print("Giờ, phút, giây không hợp lệ")
