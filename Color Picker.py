#This is one of the assitive programs for the task of onboard object detection.
#It commits to read HSV of any point you click in an image
#You click on any point, the [H, S, V] will be printed out
#2 windows will pop out:
#1st one is initial image, for you to find the object
#2nd one is the "Hue" image, for you to find the value may differ
import cv2
import cv2 as cv
import numpy as np
image = cv.imread("123.jpg")
#transfer color space into HSV
HSV = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

#get postion through mouse event and print [H,S,V] value
def getpos(event,x,y,flags,param):
    if event==cv2.EVENT_LBUTTONDOWN:
        print(HSV[y,x])

#Show the 1st window, on which you click
cv.namedWindow("image", cv.WINDOW_NORMAL)
cv2.resizeWindow("image", 1200, 900)
cv2.imshow('image',image)

#Show the image in HSV space
cv.namedWindow("imageHSV", cv.WINDOW_NORMAL)
cv2.resizeWindow("imageHSV", 1200, 900)
cv2.imshow("imageHSV",HSV)

cv2.setMouseCallback("image",getpos)
cv2.waitKey(0)#keep showing