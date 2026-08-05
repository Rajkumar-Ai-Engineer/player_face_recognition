import cv2 as cv
import numpy as np


img = cv.imread('images/cats.jpg')
#cv.imshow('img',img)

blank = np.zeros(img.shape[:2],dtype='uint8')
#cv.imshow("blank",blank)

rec = cv.rectangle(blank.copy(),(30,30),(370,370),(255,0,0),-1)
#cv.imshow('rec',rec)



circle = cv.circle(blank.copy(),(img.shape[1]//2, img.shape[0]//2),100,255,-1)
#cv.imshow('circle',circle)

weared = cv.bitwise_and(circle,rec)
cv.imshow("weared",weared)


masked = cv.bitwise_and(img,img,mask=weared)
cv.imshow("masked",masked)




cv.waitKey(0)
cv.destroyAllWindows()