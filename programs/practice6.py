import cv2 as cv 
import numpy as np 

img = cv.imread('park.jpg')
cv.imshow('park',img)

blank = np.zeros(img.shape[:2],dtype='uint8')

b,g,r = cv.split(img)
# cv.imshow('blue',b)
# cv.imshow('green',g)
#cv.imshow('red',r)
b = cv.merge([b,blank,blank])
cv.imshow('blue',b)

g = cv.merge([blank,g,blank])
cv.imshow('green',g)
r = cv.merge([blank,blank,r])
cv.imshow('red',r)
print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)


# CANNY

canny = cv.Canny(b,125,255)
cv.imshow("canny_b",canny)





cv.waitKey(0)