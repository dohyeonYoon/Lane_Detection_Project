#가우시안 블러 off canny 알고리즘

import cv2 # opencv 사용


src = cv2.imread('solidWhiteCurve.jpg')



canny_img = cv2.Canny(src, 30, 90)


cv2.imshow('solidWhiteCurve.jpg', src)
cv2.imshow('canny_img', canny_img)
cv2.waitKey() 

cv2.destroyAllWindows()