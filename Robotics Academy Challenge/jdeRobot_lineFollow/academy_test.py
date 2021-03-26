#!/usr/bin/env python
# References: 
#   - "OpenCV and Python Color Detection" by Adrian Rosebrock, access here: https://www.pyimagesearch.com/2014/08/04/opencv-python-color-detection/

#from GUI import GUI
#from HAL import HAL
import numpy as np
import argparse
import cv2
# Enter sequential code!
#console.print("Program Start")

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", help = "path to the image")
args = vars(ap.parse_args())
# load the image
image = cv2.imread(args["image"])

# create NumPy arrays from the RGB color upper and lower boundaries for "red"
lower = np.array([30, 30, 180], dtype = "uint8")
upper = np.array([55, 55, 240], dtype = "uint8")

# Find the red line in the image
mask = cv2.inRange(image, lower, upper)
output = cv2.bitwise_and(image, image, mask = mask)

M = cv2.moments(mask)
if M['m00'] != 0:
    cx = int(M['m10'] / M['m00'])
    cy = int(M['m01'] / M['m00'])
    cv2.circle(image, (cx, cy), 10, (255, 255, 255), -1)

cv2.imshow("images", np.hstack([image, output]))
cv2.waitKey(0)

height, width, dim = image.shape
error = cx - width/2
print(error)


# create a NumPy array from the RGB color boundary
# for (lower, upper) in red_boundary:
#     lower = np.array(lower, dtype = "uint8")
#     upper = np.array(upper, dtype = "uint8")
#     print(lower)
#     # find the colors within the specified boundaries and apply
#     # the mask
#     mask = cv2.inRange(image, lower, upper)
#     output = cv2.bitwise_and(image, image, mask = mask)
#     # show the images
#     cv2.imshow("images", np.hstack([image, output]))
#     cv2.waitKey(0)

#while True:
    # Enter iterative code!
    #HAL.motors.sendV(1.0)
    #img = HAL.getImage()
    #GUI.showImage(img)