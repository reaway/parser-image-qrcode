#!/usr/bin/python3
# -*- coding: UTF-8 -*-

# pip install opencv-contrib-python

import cv2

depro = './opencv_3rdparty-wechat_qrcode/detect.prototxt'
decaf = './opencv_3rdparty-wechat_qrcode/detect.caffemodel'
srpro = './opencv_3rdparty-wechat_qrcode/sr.prototxt'
srcaf = './opencv_3rdparty-wechat_qrcode/sr.caffemodel'
detector = cv2.wechat_qrcode_WeChatQRCode(depro, decaf, srpro, srcaf)
img = cv2.imread('./image/test.png')
# img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #转为灰度图片，可以不做
qrcodes, points = detector.detectAndDecode(img)
print('qrcodes: ', qrcodes)
print('points: ', points)
