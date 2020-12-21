import cv2
import numpy as np
np.set_printoptions(threshold=np.inf)
img=cv2.imread('./pic/pic1.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret, binary = cv2.threshold(gray,220,255,cv2.THRESH_BINARY)
# 找到边界findContours函数
(_, contours, _) = cv2.findContours(binary,
                                cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
# contours, hierarchy = cv2.findContours(binary,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
# contours[2]输出第二个物体的顶点坐标
# print(str(contours[2].reshape(-1)).replace('\n',',').replace(' ',',').replace(',,',',').replace(',,',',').replace('[,','['))
# 将轮廓画到原图，-1表示全部绘制
windowname ="img"
cv2.namedWindow(windowname, cv2.WINDOW_NORMAL)
cv2.drawContours(img, contours, 0, (0, 0, 255), 3)
cv2.imshow("img", img)
cv2.waitKey(0)
