# -*- coding: utf-8 -*-
"""
Created on Sat Sep  3 06:22:30 2022

@author: Master Zhang
"""
import cv2

image = cv2.imread("C:/Users/Master Zhang/Desktop/images/big.png")  # 以灰度方式加载图片
template = cv2.imread("C:/Users/Master Zhang/Desktop/images/small3.png")  # 以灰度方式加载图片

cv2.imshow("image",image)
cv2.imshow("template",template)
cv2.waitKey(0)




imageGray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

ret,image_binary = cv2.threshold(imageGray,120,120, cv2.THRESH_BINARY)     #阈值处理为二值图像
out_binary, contours, hierarchy = cv2.findContours(image_binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
for cnt in range(len(contours)):
    # 提取与绘制轮廓
    cv2.drawContours(image_binary, contours, cnt, (0, 255, 0), 2)





cv2.imshow("image_binary",image_binary)
cv2.waitKey(0)




templateGray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)

cv2.imshow("imageGray",imageGray)
cv2.imshow("templateGray",templateGray)
cv2.waitKey(0)


# 执行模板匹配
result = cv2.matchTemplate(imageGray, templateGray, cv2.TM_CCORR_NORMED)  # 匹配模式        小图在大图中的位置


(minVal, maxVal, minLoc, maxLoc) = cv2.minMaxLoc(result)

#确定起点和终点的（x，y）坐标边界框
(startX, startY) = maxLoc
endX = startX + template.shape[1]
endY = startY + template.shape[0]
#在图像上绘制边框
cv2.rectangle(image, (startX, startY), (endX, endY), (0,255,0), 3)
#显示输出图像
cv2.imshow("Output", image)
cv2.waitKey(0)





value_num = cv2.minMaxLoc(res)  # 匹配小图和大图最左边和最右边的位置


print(value_num)
x = value_num[2][0]  # 横坐标
# 4、缩放比例及校准滑块偏移量。原图680x390，实际页面图283x162
print(x)
x = int(x * 283 / 680)  # 缩放比例
print(x)
bk = 30 - int(20 * 283 / 680)  # 偏移量
print(bk)
x = x - bk
print(x)