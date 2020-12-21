

# -*- coding: UTF-8 -*-
'''
==============================
test:找出图片中二维码,并替换成自己的二维码
==============================
'''
import numpy as np
import argparse
import cv2


#==========获得二维码起始坐标位置和尺寸大小==
def find_code(pic_file):
    # print("请输入解码图片完整名称：")
    # code_name = input('>>:').strip()
    # print("正在识别：")
    image = cv2.imread(pic_file)
    # image = cv2.imread(code_name)
    # 灰度
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # 使用opencv自带的Sobel算子进行过滤
    gradX = cv2.Sobel(gray, ddepth=cv2.cv2.CV_32F, dx=1, dy=0, ksize=-1)
    gradY = cv2.Sobel(gray, ddepth=cv2.cv2.CV_32F, dx=0, dy=1, ksize=-1)

    # 将过滤得到的X方向像素值减去Y方向的像素值
    gradient = cv2.subtract(gradX, gradY)
    # 先缩放元素再取绝对值，最后转换格式为8bit型
    gradient = cv2.convertScaleAbs(gradient)
    # 均值滤波取二值化
    blurred = cv2.blur(gradient, (9, 9))
    (_, thresh) = cv2.threshold(blurred, 225, 255, cv2.THRESH_BINARY)

    # 腐蚀和膨胀的函数
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (21, 7))
    closed = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)
    closed = cv2.erode(closed, None, iterations=4)
    closed = cv2.dilate(closed, None, iterations=4)
    cv2.imwrite('./pic/closed.jpg', closed)
    # 找到边界findContours函数
    (_, cnts, _) = cv2.findContours(closed.copy(),
                                    cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    print(cnts,type(cnts))
    a =cnts
    print(a,type(a),len(a))
    # 计算出包围目标的最小矩形区域
    c = sorted(cnts, key=cv2.contourArea, reverse=False)[0]

    tmp =0
    max =0
    len(a)
    for i in range(len(a)):

        xy =a[i][-1][0][0] + a[i][-1][0][1]
        if  xy >max:
            max =xy
            tmp= i
        # print(a[i][0][0],a[i][0][1])
    # print(tmp)
    # print(a[tmp])
    rect = cv2.minAreaRect(c)
    rect1 = cv2.minAreaRect(a[tmp])
    # print(rect,rect1)
    box = np.int0(cv2.boxPoints(rect1))
    print(box)
    #======显示=======
    # windowname ="ScanQRcodeTest"
    # cv2.namedWindow(windowname, cv2.WINDOW_NORMAL)
    # cv2.drawContours(image, [box], -1, (0, 255, 0), 3)
    # cv2.imshow(windowname, image)
    # cv2.waitKey(0)
    #===============

    #=========保存证据=======
    # 绘制轮廓
    cv2.drawContours(image, [box], -1, (0, 255, 0), 3)

    cv2.imwrite('./pic/findresult.jpg',image)

    # ====获得二维码起始坐标位置和尺寸大小
    x0,y0 = box[1][0],box[1][1]
    x3,y3 =box[3][0],box[3][1]
    height = y3-y0
    width = x3 -x0
    return x0,y0 ,height,width




import qrcode

# my_str ='https://mp.weixin.qq.com/s/lAOxEG1TB6czHBMXcwpkjA' #'我爱你'#
my_str ='https://mp.weixin.qq.com/s/jbEeVf8i9cm7yKaQP9SVoQ'
my_qrcode_filename ='./pic/simpleqrcode.jpg'
img = qrcode.make(my_str)
img.save(my_qrcode_filename)


#========找位置==========
pic_file ='./pic/pic1221.jpg'
x0,y0 ,height,width=find_code(pic_file)

#========对粘贴的二维码进行尺寸调整==========
img = cv2.imread(my_qrcode_filename)
img_copy = img.copy()
img_copy = cv2.resize(img_copy,(width+10,height+10))
cv2.imwrite('./pic/yudaresize.jpg',img_copy)


#=========粘贴新二维码===========
from PIL import Image
import matplotlib.pyplot as plt
img= Image.open(pic_file)
img2=Image.open(r'./pic/yudaresize.jpg')
img.paste(img2,(x0-5,y0-5,x0+width+5,y0+height+5))
# plt.imshow(img)
# plt.show()
img.save("./pic/newpic.jpg")

