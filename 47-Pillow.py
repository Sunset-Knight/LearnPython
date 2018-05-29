#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from PIL import Image, ImageFilter

# 打开一个jpg图像文件，注意是当前路径
im = Image.open('hacknet.jpg')
# 获得图像尺寸
w, h = im.size
print('Original image size: %s X %s' % (w, h))

# 绽放到50%
im.thumbnail((w//2, h//2))
print('Resize image to: %s X %s' % (w//2, h//2))

# im.save('thumbnail.jpg', 'jpeg')

im = Image.open('hacknet.jpg')
# 应用模糊滤镜
im2 = im.filter(ImageFilter.BLUR)
im2.save('blur.jpg', 'jpeg')

