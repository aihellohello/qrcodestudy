import cv2
import numpy as np
# 1. 读入原图和模板
img_rgb = cv2.imread('./pic/pic1.jpg')
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
template = cv2.imread('./pic/tmp.jpg', 0)
h, w = template.shape[:2]

# 归一化平方差匹配
res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
threshold = 0.2

# 这段代码后面会有解释
loc = np.where(res >= threshold)  # 匹配程度大于80%的坐标y，x
for pt in zip(*loc[::-1]):  # *号表示可选参数
    right_bottom = (pt[0] + w, pt[1] + h)
    cv2.rectangle(img_rgb, pt, right_bottom, (0, 0, 255), 2)

cv2.imwrite('./pic/res.png', img_rgb)