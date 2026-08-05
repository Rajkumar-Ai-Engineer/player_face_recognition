'''import cv2 as cv

dog = cv.VideoCapture('dog.mp4')

while True:
    is_true,frame = dog.read()
    cv.imshow('dog',frame)
    key = cv.waitKey(1) & 0xFF
    if key == ord("q"):
                break
dog.release()'''

#resize and rescale

'''img = cv.imread('park.jpg')
cv.imshow('park',img)
cv.waitKey(0)'''

'''def rescale(frame,scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimension = (width,height)

    return cv.resize(frame,dimension,interpolation= cv.INTER_AREA)

dog = cv.VideoCapture('dog.mp4')


while True:
    is_true,frame = dog.read()
    resize = rescale(frame)
    cv.imshow('dg', frame)
    cv.imshow('dog', resize)
    if cv.waitKey(20) & 0xFF==ord('q'):
        break

dog.release()
cv.destroyAllWindows()'''
# img = cv.imread('image_1.jpg')
# cv.imshow('img',img)
# cv.waitKey(0)