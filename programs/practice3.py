import cv2 as cv 
import numpy as np
img = cv.imread('grp1.jpg')
#cv.imshow('cat',img)

def translate(img,x,y):
     transmat = np.float32([[1,0,x],[0,1,y]])
     dimension = (img.shape[1],img.shape[0])
     return cv.warpAffine(img,transmat,dimension)

translated = translate(img,-100,-100)
cv.imshow('translate',translated)

# rotate
def rotate(img,angle,rotpoint=None):
     (width,height) = img.shape[:2]

     if rotpoint is None:
          rotpoint = (width//2,height//2)

     rotmat = cv.getRotationMatrix2D(rotpoint,angle,1.0)
     dimension = (width,height)

     return cv.warpAffine(img,rotmat,dimension)

rotae = rotate(img,160)
cv.imshow('rotae',rotae)

rotated = rotate(rotae,160)
cv.imshow('rotated',rotated)
    
flip = cv.flip(img,0)
cv.imshow('flip',flip)

flip2 = cv.flip(img,1)
cv.imshow('flip2',flip2)

flip3 = cv.flip(img,-1)
cv.imshow('flip3',flip3)

cv.waitKey(0)