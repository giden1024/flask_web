#!/usr/bin/env python
# encoding: utf-8
"""
@author: mayuyang
@time: 2020/10/27 16:30
@desc:
"""

from PIL import Image,ImageDraw,ImageFilter,ImageFont
import random


def get_captcha(filepath,filename):
    numlist = list(range(48,58)) + list(range(65,91)) + list(range(97,123))

    # 获取随机字母
    def rndchar():
        return chr(random.choice(numlist))


    # 获取随机颜色1
    def rndcolor1():
        return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))

    # 获取随机颜色2
    def rndcolor2():
        return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))


    captcha_code = ""

    width = 60 * 4
    height = 60
    # 新建一张图片
    image = Image.new('RGB',(width,height),(255,255,255))
    # 新建字体
    font = ImageFont.truetype("arial.ttf", 30)
    # 新建draw对象
    draw = ImageDraw.Draw(image)

    for x in range(width):
        for y in range(height):
            draw.point((x,y),fill=rndcolor1())

    for t in range(4):
        draw.text((60 * t + 10,10),rndchar(),fill=rndcolor2(),font=font)
        captcha_code = captcha_code + rndchar()
    image.save(filepath + filename,"jpeg")

    captcha_code = "1234"
    return captcha_code


if __name__ == "__main__":
    code = get_captcha("static/img/","cap.jpeg")
    print(code)
