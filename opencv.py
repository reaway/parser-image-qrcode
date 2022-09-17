#!/usr/bin/python
# -*- coding: UTF-8 -*-

# pip install opencv-contrib-python

import cv2

print('cv2.__version__:', cv2.__version__)
detector = cv2.wechat_qrcode_WeChatQRCode()
img = cv2.imread('./image/test.png')
res, points = detector.detectAndDecode(img)
print('res: ', res)
print('points: ', points)
