import numpy as np
import cv2

class detection:
     def __init__(self):

     def detect(image, upper_limit, lower_limit, upper_size, lower_size, square_threshold, area_occupancy_threshold):
        #Transform BGR value to HSV;
         hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV) #Transform BGR value to HSV;
         mask = cv2.inRange(hsv, upper_limit, lower_limit)

        #Erode the mask in order to eliminate nearby noises which may has similar color to the object;
         kernel = np.ones((5,5),np.uint8)#create convolution
         mask = cv2.erode(mask, kernel, iterations=2) # Get a new mask for red object

        #Dilate the new mask in order to maintain its size
         mask = cv2.dilate(mask, kernel, iterations=2)

        #find contours
         cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
         square_center = None #Initialize the center of red object;
         if len(cnts) > 0: #If the contour exists (means I obtained gathered pixels which remain on the mask of red)

            #find the biggest contour, because there's at most 1 object for each color, so I don't need small
            c = max(cnts, key=cv2.contourArea) #find the largest largest contour

            #find rotated bounding rectangle#
            #Create a min rectangle to enclose the largest contour
            rec = cv2.minAreaRect(c)

            # Obtain the 4 corners of the box
            box = cv2.boxPoints(rec)

            #transfer the data type
            box = np.int0(box)

            #find the center, width and height of the rectangle
            ((a,b), (width, height), angle_of_rotation) = cv2.minAreaRect(c)

            #define the similarity of width and height
            similarity = min(width, height) / max(width, height)

            # find the area percentage of given color in rectangle (AFTER noise reduction)
            area_percentage = cv2.contourArea(c) / width * height

            if upper_size> max(width, height) and min((width, height))> lower_size:
                if (similarity) > square_threshold and (area_percentage > area_occupancy_threshold): #If width and height close enough and the rectangle is "full" enough of the color
                    cv2.drawContours(image, [box], 0, (255, 0, 0), 4)  # Draw the rectangle of contour on the image
                    cv2.circle(image, (int(a),int(b)), 5, (255, 0, 0), -1)   #Draw the center of square
                    square_center = (a,b)
                    print (square_center)
                else:
                    square_center = None
            else:
                 square_center = None
         else:
            square_center = None #Destroy the value


