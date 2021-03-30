#가우시안 블러 on Laplacian 알고리즘

import cv2 # opencv 사용
import numpy as np

img = cv2.imread('solidWhiteCurve.jpg', cv2.IMREAD_GRAYSCALE)
height, width = img.shape[:2]


blur_img = cv2.GaussianBlur(img, (0,0), 1)
Laplacian_img = cv2.Laplacian(blur_img,cv2.CV_8U, ksize=5)

cv2.imshow('img', img)
cv2.imshow('Laplacian_img', Laplacian_img)
cv2.waitKey()

cv2.destroyAllWindows()