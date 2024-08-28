# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 23:11:35 2024

@author: Huynh Dieu My
"""

hinh = input("Nhập hình bạn cần tính (v: hình vuông, t: hình tròn, n: hình chữ nhật: ")
if hinh == 'v':
    canh = float(input("Nhập độ dài cạnh: ")) 
    print("Chu vi: P =  ", canh*4)
    print("Diện tích: S = ", canh * canh )
elif hinh == 't':
    r = float(input("Nhập độ dài bán kính: "))
    print("Chu vi: P = ", 2*3.14*r)
    print("Diện tích: S = ", (r**2)*3.14)
elif hinh == 'n':
    d = float(input("Nhập độ dài chiều dài: "))
    rng = float(input("Nhập độ dài chiều rộng: "))
    print("Chu vi: P = ", (d + rng)*2)
    print("Diện tích: S = ", d*rng)
else:
    print("Hình bạn nhập không hợp lệ")