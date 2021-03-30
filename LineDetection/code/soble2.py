#가우시안 블러 off sobel 알고리즘

import cv2 # opencv 사용
import numpy as np

img = cv2.imread('solidWhiteCurve.jpg', cv2.IMREAD_GRAYSCALE)
height, width = img.shape[:2]


Sobel_dx = cv2.Sobel(img,cv2.CV_32F, 1, 0) #x방향 미분
Sobel_dy = cv2.Sobel(img,cv2.CV_32F, 0, 1) #y방향 미분


mag = cv2.magnitude(Sobel_dx, Sobel_dy)
mag = np.clip(mag, 0, 255).astype(np.uint8)
cv2.imshow('img', img)
cv2.imshow('mag', mag)
cv2.waitKey()


cv2.destroyAllWindows()