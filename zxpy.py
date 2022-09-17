#!/usr/bin/python3
# -*- coding: UTF-8 -*-

# pip install pyzxing

from pyzxing import BarCodeReader

reader = BarCodeReader()
results = reader.decode('./image/000595101152.jpg')
print(results)
