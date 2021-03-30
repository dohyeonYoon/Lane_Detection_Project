from tkinter import *
import cv2 # opencv 사용
import numpy as np
import sys

root = Tk()
root.title("Line Detection Program") #윈도우창제목
root.geometry("480x200") #가로x세로


line_var=IntVar()  #필터 라디오 박스 설정
frame_line=LabelFrame(root,padx=15, pady=10, text="필터") #필터 프레임 설정
frame_line.pack(side=LEFT,fill="both")
btn_line1=Radiobutton(frame_line,padx=15, pady=10, text="Sobel", value=1, variable=line_var)
btn_line1.select()
btn_line2=Radiobutton(frame_line,padx=15, pady=10, text="Laplacian", value=2, variable=line_var)
btn_line3=Radiobutton(frame_line,padx=15, pady=10, text="Canny", value=3, variable=line_var)


btn_line1.pack()
btn_line2.pack()
btn_line3.pack()


frame_gaussian=LabelFrame(root,padx=15, pady=10, text="가우시안 블러") #필터 프레임 설정
frame_gaussian.pack(side=LEFT,fill="both")

gaussian_var=IntVar() #가우시안 필터 라디오 박스 설정
btn_gaussian1=Radiobutton(frame_gaussian,padx=15, pady=10, text="On", value=1, variable=gaussian_var)
btn_gaussian1.select()
btn_gaussian2=Radiobutton(frame_gaussian,padx=15, pady=10, text="Off", value=2, variable=gaussian_var)

btn_gaussian1.pack()
btn_gaussian2.pack()

frame_haugh=LabelFrame(root,padx=15, pady=10, text="허프 변환") #허프 변환 프레임 설정
frame_haugh.pack(side=LEFT,fill="both")

haugh_var=IntVar() #허프변환 필터 라디오 박스 설정
btn_haugh1=Radiobutton(frame_haugh,padx=15, pady=10, text="On", value=1, variable=haugh_var)
btn_haugh1.select()
btn_haugh2=Radiobutton(frame_haugh,padx=15, pady=10, text="Off", value=2, variable=haugh_var)

btn_haugh1.pack()
btn_haugh2.pack()


def btncmd():  #btncmd 함수설정
    if line_var.get()==1 and gaussian_var.get()==1 and haugh_var.get()==1: #Sobel필터, Gaussian on, Haugh on
       #그레이스케일 이미지 불러오기 
       src = cv2.imread('solidWhiteCurve.jpg' ,cv2.IMREAD_GRAYSCALE)

       if src is None: 
          print('image load failed!!')
          sys.exit()


       #가우시안블러 처리 
       blur_img = cv2.GaussianBlur(src, (0,0),1)

       #Sobel Edge Detection 
       Sobel_dx = cv2.Sobel(blur_img,cv2.CV_32F, 1, 0) #x방향 미분
       Sobel_dy = cv2.Sobel(blur_img,cv2.CV_32F, 0, 1) #y방향 미분

       mag = cv2.magnitude(Sobel_dx, Sobel_dy)




       #허프변환
       lines = cv2.HoughLinesP(mag, 1,np.pi/180., 50, minLineLength= 30, maxLineGap = 4)
       dst = cv2.cvtColor(mag, cv2.COLOR_GRAY2BGR)

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
    elif line_var.get()==1 and gaussian_var.get()==1 and haugh_var.get()==2: #Sobel필터, Gaussian on, Haugh off
         img = cv2.imread('solidWhiteCurve.jpg',cv2.IMREAD_GRAYSCALE)
         height, width = img.shape[:2]


         blur_img = cv2.GaussianBlur(img, (0,0), 1)
         Sobel_dx = cv2.Sobel(blur_img,cv2.CV_32F, 1, 0) #x방향 미분
         Sobel_dy = cv2.Sobel(blur_img,cv2.CV_32F, 0, 1) #y방향 미분


         mag = cv2.magnitude(Sobel_dx, Sobel_dy)
         mag = np.clip(mag, 0, 255).astype(np.uint8)
         cv2.imshow('img', img)
         cv2.imshow('mag', mag)
         cv2.waitKey()


         cv2.destroyAllWindows()
    elif line_var.get()==1 and gaussian_var.get()==2 and haugh_var.get()==1: #Sobel필터, Gaussian off, Haugh on
         #그레이스케일 이미지 불러오기 
         src = cv2.imread('solidWhiteCurve.jpg')

         if src is None: 
            print('image load failed!!')
            sys.exit()



         #Sobel Edge Detection 
         Sobel_dx = cv2.Sobel(src,cv2.CV_32F, 1, 0) #x방향 미분
         Sobel_dy = cv2.Sobel(src,cv2.CV_32F, 0, 1) #y방향 미분

         mag = cv2.magnitude(Sobel_dx, Sobel_dy)




         #허프변환
         lines = cv2.HoughLinesP(mag, 1,np.pi/180., 50, minLineLength= 30, maxLineGap = 4)
         dst = cv2.cvtColor(mag, cv2.COLOR_GRAY2BGR)

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
    elif line_var.get()==1 and gaussian_var.get()==2 and haugh_var.get()==2: #Sobel필터, Gaussian off, Haugh off
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
    elif line_var.get()==2 and gaussian_var.get()==1 and haugh_var.get()==1: #Laplacian필터, Gaussian on, Haugh on
         src = cv2.imread('solidWhiteCurve.jpg', cv2.IMREAD_GRAYSCALE)

         if src is None:
            print('Image load failed!')
            sys.exit()


         #가우시안블러 처리 
         blur_img = cv2.GaussianBlur(src, (0,0),1)

         #edge
         edges = cv2.Laplacian(blur_img, cv2.CV_8U, ksize=5)


         lines = cv2.HoughLinesP(edges, 1, np.pi / 180., 160,
                                 minLineLength=50, maxLineGap=1)

         dst = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)

         if lines is not None:
            for i in range(lines.shape[0]):
                pt1 = (lines[i][0][0], lines[i][0][1])  # 시작점 좌표
                pt2 = (lines[i][0][2], lines[i][0][3])  # 끝점 좌표
                cv2.line(dst, pt1, pt2, (0, 0, 255), 2, cv2.LINE_AA)

         cv2.imshow('src', src)
         cv2.imshow('dst', dst)
         cv2.waitKey()
         cv2.destroyAllWindows()
    elif line_var.get()==2 and gaussian_var.get()==1 and haugh_var.get()==2: #Laplacian필터, Gaussian on, Haugh off
         img = cv2.imread('solidWhiteCurve.jpg', cv2.IMREAD_GRAYSCALE)
         height, width = img.shape[:2]


         blur_img = cv2.GaussianBlur(img, (0,0), 1)
         Laplacian_img = cv2.Laplacian(blur_img,cv2.CV_8U, ksize=5)

         cv2.imshow('img', img)
         cv2.imshow('Laplacian_img', Laplacian_img)
         cv2.waitKey()

         cv2.destroyAllWindows()
    elif line_var.get()==2 and gaussian_var.get()==2 and haugh_var.get()==1: #Laplacian필터, Gaussian off, Haugh on
         src = cv2.imread('solidWhiteCurve.jpg', cv2.IMREAD_GRAYSCALE)

         if src is None:
            print('Image load failed!')
            sys.exit()

         edges = cv2.Laplacian(src, cv2.CV_8U, ksize=5)

         lines = cv2.HoughLinesP(edges, 1, np.pi / 180., 160,
                                 minLineLength=50, maxLineGap=1)

         dst = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)

         if lines is not None:
            for i in range(lines.shape[0]):
                pt1 = (lines[i][0][0], lines[i][0][1])  # 시작점 좌표
                pt2 = (lines[i][0][2], lines[i][0][3])  # 끝점 좌표
                cv2.line(dst, pt1, pt2, (0, 0, 255), 2, cv2.LINE_AA)

         cv2.imshow('src', src)
         cv2.imshow('dst', dst)
         cv2.waitKey()
         cv2.destroyAllWindows()
    elif line_var.get()==2 and gaussian_var.get()==2 and haugh_var.get()==2: #Laplacian필터, Gaussian off, Haugh off
         img = cv2.imread('solidWhiteCurve.jpg', cv2.IMREAD_GRAYSCALE)
         height, width = img.shape[:2]


         Laplacian_img = cv2.Laplacian(img,cv2.CV_8U, ksize=5)

         cv2.imshow('img', img)
         cv2.imshow('Laplacian_img', Laplacian_img)
         cv2.waitKey()

         cv2.destroyAllWindows()
    elif line_var.get()==3 and gaussian_var.get()==1 and haugh_var.get()==1: #Canny필터, Gaussian on, Haugh on
        #그레이스케일 이미지 불러오기 
         src = cv2.imread('solidWhiteCurve.jpg')

         if src is None: 
            print('image load failed!!')
            sys.exit()
         
         #가우시안블러 처리 
         blur_img = cv2.GaussianBlur(src, (0,0),1)

         #Canny Edge Detection 
         canny_img = cv2.Canny(blur_img,50,150,)
         
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
    elif line_var.get()==3 and gaussian_var.get()==1 and haugh_var.get()==2: #Canny필터, Gaussian on, Haugh off
         src = cv2.imread('solidWhiteCurve.jpg')

         blur_img = cv2.GaussianBlur(src, (0,0), 2)

         canny_img = cv2.Canny(blur_img, 30, 90)


         cv2.imshow('solidWhiteCurve.jpg', src)
         cv2.imshow('canny_img', canny_img)
         cv2.waitKey() 

         cv2.destroyAllWindows()
    elif line_var.get()==3 and gaussian_var.get()==2 and haugh_var.get()==1: #Canny필터, Gaussian off, Haugh on
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
    elif line_var.get()==3 and gaussian_var.get()==2 and haugh_var.get()==2: #Canny필터, Gaussian off, Haugh off
         src = cv2.imread('solidWhiteCurve.jpg')



         canny_img = cv2.Canny(src, 30, 90)


         cv2.imshow('solidWhiteCurve.jpg', src)
         cv2.imshow('canny_img', canny_img)
         cv2.waitKey() 

         cv2.destroyAllWindows()
    else: #예외
        print("img load failed")


    




btn = Button(root,padx=15, pady=10, text="실행",command=btncmd) #버튼생성
btn.pack(side=RIGHT,padx=30,) #버튼 위치 조정



root.mainloop()