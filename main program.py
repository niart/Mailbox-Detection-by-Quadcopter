from collections import deque
import numpy as np
import cv2
import cv2 as cv
import time
from object_detection import detection

### Define color segment threshold ###

#red
Lower_red = np.array([163, 50, 0]) # Define the lower of subset1 of red
Upper_red = np.array([18, 255, 255]) # Define the upper of subset1 of red

#yellow
Lower_yellow = np.array([20, 50, 0])
Upper_yellow = np.array([40, 255, 255])

#blue
Lower_blue = np.array([109, 40, 0])
Upper_blue = np.array([130, 255, 255])

#orange
Lower_orange = np.array([10, 50, 0])
Upper_orange = np.array([25, 255, 255])

###Define square approximation parameters###
width_height_ratio = 0.6
area_occupancy_ratio = 0.6

###Define size threshold
#Red
red_upper_size = 300
red_lower_size = 50
#blue
blue_upper_size = 300
blue_lower_size = 50
#yellow
yellow_upper_size = 300
yellow_lower_size = 50
#orange
orange_upper_size = 300
orange_lower_size = 50

mybuffer = 64
pts = deque(maxlen=mybuffer) 
jevois = cv2.VideoCapture(0) #Import picture from jevois video module
#time.sleep(2) #If I wanna pause 2 seconds to let Jevois camera switches on

while True:
    (video_mode, frame) = jevois.read()  #The program is to fuction only if jevois video mode is on;
    if not video_mode:
      print('Jevois fails')
      break
    #Above is to be used when we capture frames from Jevois
    #frame = cv2.imread("test.png")         # This command is to be used when I load from existent photos;
    red = detection.detect(frame, Upper_red, Lower_red, red_upper_size, red_lower_size, width_height_ratio,area_occupancy_ratio)
    blue = detection.detect(frame, Upper_blue, Lower_blue, blue_upper_size, blue_lower_size, width_height_ratio,area_occupancy_ratio)
    yellow = detection.detect(frame, Upper_yellow, Lower_yellow, yellow_upper_size, yellow_lower_size, width_height_ratio, area_occupancy_ratio)
    orange = detection.detect(frame, Upper_orange, Lower_orange, orange_upper_size, orange_lower_size,width_height_ratio, area_occupancy_ratio)

# Merge all those 4 masks
    #res = cv2.bitwise_and(frame, frame, mask=mask)# get color mask

    cv2.namedWindow("Ni Object Detection", 0); #Name the window
    cv2.resizeWindow("Ni Object Detection", 800,600); # Change the window size to adapt to 4:3 of Jevois
    cv2.imshow('Ni Object Detection', frame) #Load the frame which contains rectangle

    cv2.namedWindow("Mask Effect", 0); #name a window to show merged mask
    cv2.resizeWindow("Mask Effect", 800,600); #change the size of mask window
   # cv2.imshow('Mask Effect',res)#Show the mask window for my own analysis

    k = cv2.waitKey(5)&0xFF # Detect ESC to exist the program
    if k == 27:
        break

jevois.release() # Relesase jevois camera
cv2.destroyAllWindows() # Destory all windows
