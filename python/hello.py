#-*- coding:utf-8 -*-
print('hello world!')
s ='haoba125t\
'
b = r'\s'
str_ = "中文"
'''
str = input("true or false:")
str = int(str)
if str:
    print(s)
elif 0:
    print(b)
d = {"name":"ahui","lang":[1,2,3]}
print(d['name'])
print(d.get('lang','nidaye'))

t = (1,2,3,3)
s = set((1,2,3,3))
#s1 = set((1,[2,3]))
print(s)
print(t)
'''
#print(s)

# 安装第三方模块，测试使用图像处理库
from PIL import Image
im = Image.open('test.jpg')
print(im.format, im.size, im.mode)
im.thumbnail((200,100))
im.save('test_thumb.jpg', 'JPEG')
