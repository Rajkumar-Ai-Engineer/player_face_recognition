import cv2 as cv 

img = cv.imread('2.jpg')
cv.imshow('dragon',img)

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('grsy',gray)

blur = cv.GaussianBlur(gray,(3,3),cv.BORDER_DEFAULT)
cv.imshow('blur',blur)

_,thresh = cv.threshold(img,150,255,cv.THRESH_BINARY)
cv.imshow('thresh',thresh) 

dilate = cv.dilate(blur,(3,3),iterations=1)
cv.imshow('dilate',dilate)

erode = cv.erode(blur,(3,3),iterations=1)
cv.imshow('erode',erode)

canny = cv.Canny(gray,125,255)
cv.imshow('canny',canny)

resize = cv.resize(img,(100,100))
cv.imshow('resize',resize)

crop = img[50:200,200:300]
cv.imshow('crop',crop)






cv.waitKey(0)
