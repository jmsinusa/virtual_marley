"""
Capture images from webcam and other sources
"""

# from cv2 import VideoCapture
import cv2
from datetime import datetime
import time
import os
from matplotlib import pyplot as plt

cap = cv2.VideoCapture(0)  #set the port of the camera as before
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)
# cap.set(cv2.CV_CAP_PROP_CONVERT_RGB, True)

while True:
    retval, image = cap.read()
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    newimage = cv2.flip(image, 0)
    newimage = cv2.flip(newimage, 1)
    plt.imshow(newimage)
    plt.show()
