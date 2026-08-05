import cv2 as cv 

img = cv.imread('grp1.jpg')

cv.imshow('people',img)

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

face = cv.CascadeClassifier('haarcascade_frontalface_default.xml')

faces_rect = face.detectMultiScale(gray,1.1,4)

print("number of faces found:",len(faces_rect))

for (x,y,w,h) in faces_rect:
    cv.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)


cv.imshow('faces detect',img)














cv.waitKey(0)