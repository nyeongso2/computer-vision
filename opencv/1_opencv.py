import cv2 as cv
import sys

img = cv.imread('opencv_test/images/soccer.jpg')

if img is None:
    sys.exit('파일이 존재하지않습니다')

cv.imshow('image Display',img)

cv.waitKey()
cv.destroyALLWindows()

print(type(img))
print(img.shape)
