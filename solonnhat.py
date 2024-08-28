# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 19:19:01 2024

@author: Huynh Dieu My 
"""

a = float(input("Nhập vào số a: "))
b = float(input("Nhập vào số b: "))
c = float(input("Nhập vào số c: "))
d = float(input("Nhập vào số d: "))
if a > b and a > c and a > d:
    print("Số có giá trị lớn nhất là: ",a)
elif b > a and b > c and b > d:
    print("Số có giá trị lớn nhất là: ",b)
elif c > b and c > a and c > d:
    print("Số có giá trị lớn nhất là: ",c)
else:
    print("Số có giá trị lớn nhất là: ",d)