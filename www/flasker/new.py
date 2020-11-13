#!/usr/bin/env python
# encoding: utf-8
"""
@author: mark
@file: new.py
@time: 2019/10/31 13:54
@desc:
"""
def search(array,t):
    if t in array:
            low = 0
            hight = len(array) - 1

            while low <= hight:
                mid =(low + hight) // 2
                if array[mid] < t:
                    low =mid + 1
                elif array[mid] > t:
                    hight =mid - 1
                else:
                    break
            print("你要查找的数字%d 出现在序列第%d位" %(t,mid + 1))
            return array[mid]
    else:
        print("你想要查找的%d不在序列内"%t)


if __name__ == "__main__":
    search([1,2,3,4],1)