#!/usr/bin/python3
# -*- coding: UTF-8 -*-

# pip install zxing

import zxing

reader = zxing.BarCodeReader()
barcode = reader.decode('./image/test.png')
print(barcode.type)
print(barcode.parsed)
