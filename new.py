#!/usr/bin/env python
# encoding: utf-8
"""
@author: mark
@file: new.py.py
@time: 2019/11/4 10:33
@desc:
"""

import hashlib
m2 = hashlib.md5()
m2.update("requestId=6&timestamp=1571716703&secretKey=secret".encode("utf-8"))
print(m2.hexdigest().upper())
