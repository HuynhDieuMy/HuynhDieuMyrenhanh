# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 22:18:29 2024

@author: Huynh Dieu My 
"""
import math
a = float(input("Nhập số a: "))
b = float(input("Nhập số b: "))
c = float(input("Nhập số c: "))
if a==0:
    print("Phương trình có 1 nghiệm: ", -c/b)
elif a!=0:
    delta = b**2 - 4*a*c
    if delta > 0:
        x1 = (-b + math.sqrt(delta))/(2*a) 
        x2 = (-b - math.sqrt(delta))/(2*a) 
        print("Phương trình có hai nghiệm phân biệt: x1 = ", x1)
        print("x2 = ", x2)
    elif delta == 0:
        x = -b / (2*a)
        print("Phương trình có hai nghiệm kép: x1 = x2 = ", x )
    elif delta < 0:
        print("Phương trình vô nghiệm")
    else:
        print("Không giải được")