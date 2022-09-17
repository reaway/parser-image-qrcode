#!/usr/bin/python3
# -*- coding: UTF-8 -*-

# pip install zxing

import zxing

reader = zxing.BarCodeReader()
barcode = reader.decode('./image/000595101152.jpg')
print(barcode.type)
print(barcode.parsed)
