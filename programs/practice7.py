import cv2 as cv 

img = cv.imread('2.jpg')
cv.imshow('papa',img)

#1.gaussian

gauss = cv.GaussianBlur(img,(3,3),cv.THRESH_BINARY)
cv.imshow('gauss',gauss)

#averaging blur
aver = cv.blur(img,(7,7))
cv.imshow('aver',aver)

#blob
#blob = cv.dnn.blobFromImage(gauss,1.0,(500,500))
#cv.imshow('blob',blob)

#medianblur

med = cv.medianBlur(img,3)
cv.imshow('med',med)

#bilateral

bi = cv.bilateralFilter(img,3,15,15)
cv.imshow('bi',bi)










cv.waitKey(0)