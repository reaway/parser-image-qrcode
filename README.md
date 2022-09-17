parser-image-qrcode
===============

Python识别图片中的二维码

## 1，使用opencv

```bash
# 安装依赖库
pip install opencv-contrib-python

# 测试
python opencv.py
```

## 2，使用pyzbar

```bash
# 安装依赖库
pip install pyzbar
pip install pillow

# 测试
python zbar.py
```

## 3，使用zxing
> 需要安装Java, 请参阅 [Java开发环境配置](https://www.runoob.com/java/java-environment-setup.html)

```bash
# 安装依赖库
pip pip install zxing

python zx.py
```
或者
```bash
# 安装依赖库
pip pip install pyzxing

# 测试
python zxpy.py
```