import cv2 as cv 
import matplotlib.pyplot as plt

img  = cv.imread('grp1.jpg')

cv.imshow('papa',img)

#1.gray
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray)

# # 2.hsv

hsv = cv.cvtColor(img,cv.COLOR_BGR2HSV)
cv.imshow('hsv',hsv)

# #3.lab

lab = cv.cvtColor(img,cv.COLOR_BGR2LAB)
cv.imshow('lab',lab)

# #4.rgb

rgb =cv.cvtColor(img,cv.COLOR_BGR2RGB)
cv.imshow('rgb',rgb)


# 5.hsl

# hsl = cv.cvtColor(img,cv.COLOR_BGR2HSL)

# #5.PLOT
plt.imshow(img)
plt.show()



cv.waitKey(0)