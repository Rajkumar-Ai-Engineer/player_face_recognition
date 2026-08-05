import cv2 as cv
import numpy as np 
# blank img
blank =np.zeros((500,500,3),dtype='uint8')
#cv.imshow('blank',blank)

# certain color
blank[:] = 0,255,0
#cv.imshow('blank',blank)

#draw circle
circle = cv.circle(blank,(250,250),40,(0,0,255),2)
#cv.imshow('circle',circle)

#rec

rec = cv.rectangle(blank,(0,0),(250,250),(255,0,0),-1)
cv.imshow('rec',rec)

#line 
line =cv.line(blank,(0,0),(250,250),(255,255,255),2)
cv.imshow('line',line)

text = cv.putText(blank,'hello world',(250,250),cv.FONT_HERSHEY_COMPLEX,1.0,(0,0,0),2)
cv.imshow('text',text)
cv.waitKey(0)