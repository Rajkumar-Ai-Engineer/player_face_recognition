import cv2 as cv 
import numpy as np 
img = cv.imread('2.jpg')
cv.imshow('grp1',img)



blank = np.zeros(img.shape,dtype='uint8')





gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

blur = cv.GaussianBlur(gray,(3,3),cv.BORDER_DEFAULT)

_,thresh = cv.threshold(blur,80,255,cv.THRESH_BINARY)
cv.imshow('THRESH',thresh)

canny = cv.Canny(gray,125,175)
cv.imshow('canny',canny)

contors,heirarchies = cv.findContours(canny,cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE)
#cv.imshow('contor',contors)
print(len(contors))

draw = cv.drawContours(blank,contors,-1,(0,0,255),1)
cv.imshow('drawn',draw)






cv.waitKey(0)