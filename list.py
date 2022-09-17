#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import os
import sys
import json

import cv2

import pyzbar.pyzbar as pyzbar
from PIL import Image, ImageEnhance

import zxing
from pyzxing import BarCodeReader


def cv2_parser(image_path):
    depro = './opencv_3rdparty-wechat_qrcode/detect.prototxt'
    decaf = './opencv_3rdparty-wechat_qrcode/detect.caffemodel'
    srpro = './opencv_3rdparty-wechat_qrcode/sr.prototxt'
    srcaf = './opencv_3rdparty-wechat_qrcode/sr.caffemodel'
    detector = cv2.wechat_qrcode_WeChatQRCode(depro, decaf, srpro, srcaf)
    img = cv2.imread(image_path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    res, points = detector.detectAndDecode(img)
    if len(res) > 0:
        print('opencv: ' + res[0])
        return True
    return False


def pyzbar_parser(image_path):
    img = Image.open(image_path)
    qrcodes = pyzbar.decode(img)
    for qrcode in qrcodes:
        code = qrcode.data.decode()
        if len(code) > 0:
            print('pyzbar: ' + code)
            return True
        return False


def zxing_parser(image_path):
    reader = zxing.BarCodeReader()
    barcode = reader.decode(image_path)
    if len(barcode.parsed) > 0:
        print('zxing: ' + barcode.parsed)
        return True
    return False


def pyzxing_parser(image_path):
    reader = BarCodeReader()
    results = reader.decode(image_path)
    for result in results:
        if 'format' in result and result['format'].decode() == 'QR_CODE':
            print('pyzxing: ' + result['parsed'].decode('GBK'))
            return True
    return False


path = './image'
imgs = os.listdir(path)
for name in imgs:
    suffix = name.split('.')[-1]
    if suffix.lower() in ('jpg', 'png'):
        file = path + '/' + name
        print(name)
        if not cv2_parser(file):
            if not zxing_parser(file):
                pyzxing_parser(file)
        # sys.exit()
        print('-----------------------------------')
