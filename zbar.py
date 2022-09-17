#!/usr/bin/python3
# -*- coding: UTF-8 -*-

# pip install pyzbar
# pip install pillow

import pyzbar.pyzbar as pyzbar
from PIL import Image, ImageEnhance


def zbar_parser(image_path):
    img = Image.open(image_path)
    # 以下图片处理过程可以不做
    # img = ImageEnhance.Brightness(img).enhance(2.0)#增加亮度
    # img = ImageEnhance.Sharpness(img).enhance(17.0)#锐利化
    # img = ImageEnhance.Contrast(img).enhance(4.0)#增加对比度
    # img = img.convert('L')#灰度化

    qrcodes = pyzbar.decode(img)
    for qrcode in qrcodes:
        data = qrcode.data.decode('utf-8')
        print(qrcode)
        print(data)


zbar_parser('./image/test.png')
