#가우시안 블러 on canny 알고리즘

import cv2 # opencv 사용


src = cv2.imread('solidWhiteCurve.jpg')

blur_img = cv2.GaussianBlur(src, (0,0), 2)

canny_img = cv2.Canny(blur_img, 30, 90)


cv2.imshow('solidWhiteCurve.jpg', src)
cv2.imshow('canny_img', canny_img)
cv2.waitKey() 

cv2.destroyAllWindows()