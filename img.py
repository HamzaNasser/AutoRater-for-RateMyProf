import cv2 as cv

img = cv.imread("like.png")

cv.imshow("like", img)

cv.waitKey(0)