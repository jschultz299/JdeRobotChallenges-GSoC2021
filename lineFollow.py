# References: 
#   - "OpenCV and Python Color Detection" by Adrian Rosebrock, access here: https://www.pyimagesearch.com/2014/08/04/opencv-python-color-detection/

from GUI import GUI
from HAL import HAL
import numpy as np
import argparse
import cv2

# create NumPy arrays from the RGB color upper and lower boundaries for "red"
lower = np.array([30, 30, 180], dtype = "uint8")
upper = np.array([55, 55, 240], dtype = "uint8")

# Initialize some values
error_last = 0
error_sum = 0

# Set controller gains
#Kp = .00075
#Kd = .00001
#Ki = .00001

Kp = .001
Kd = .001
Ki = .000001

while True:
    # load the current image
    image = HAL.getImage()

    # Find the red line in the image
    mask = cv2.inRange(image, lower, upper)
    output = cv2.bitwise_and(image, image, mask = mask)

    # Locate the centroid of the red line
    M = cv2.moments(mask, binaryImage=True)

    # Display a white circle at the centroid of the line
    if M['m00'] != 0:
        cx = int(M['m10'] / M['m00'])
        cy = int(M['m01'] / M['m00'])
        cv2.circle(image, (cx, cy), 10, (255, 255, 255), -1)
    else:
        cx = 0
        cy = 0


    # Display the image
    GUI.showImage(image)

    # Obtain image shape and compute set-point error terms
    height, width, dim = image.shape
    error = width/2 - cx
    console.print(error)
    diff_error = error - error_last
    sum_error = error + error_last

    # Send control values to the robot
    HAL.motors.sendV(0.5)
    HAL.motors.sendW(error*Kp + diff_error*Kd + sum_error*Ki)