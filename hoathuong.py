# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 23:00:38 2024

@author: Huynh Dieu My 
"""

chu = input("Nhập chữ cái: ")
if chu.islower():
    print("Kết quả: ", chu.upper())
elif chu.isupper():
    print("Kết quả: ", chu.lower())
else:
    print("Không phải chữ cái!")