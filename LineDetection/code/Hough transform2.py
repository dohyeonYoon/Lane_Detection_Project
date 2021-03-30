#가우시안 블러 off hough 알고리즘 


import cv2
import numpy as np
import sys

#그레이스케일 이미지 불러오기 
src = cv2.imread('solidWhiteCurve.jpg')

if src is None: 
    print('image load failed!!')
    sys.exit()


#Canny Edge Detection 
canny_img = cv2.Canny(src,50,150,)



#허프변환
lines = cv2.HoughLinesP(canny_img, 1,np.pi/180., 50, minLineLength= 30, maxLineGap = 4)
dst = cv2.cvtColor(canny_img, cv2.COLOR_GRAY2BGR)

#직선을 빨간색으로 표시 
if lines is not None:
    for i in range(lines.shape[0]):
        pt1 = (lines[i][0][0], lines[i][0][1])
        pt2 = (lines[i][0][2], lines[i][0][3])
        cv2.line(dst,pt1,pt2, (0,0,255), 2, cv2.LINE_AA)



#출력
cv2.imshow('src', src)
cv2.imshow('dst', dst)

cv2.waitKey()

cv2.destroyAllwindows()