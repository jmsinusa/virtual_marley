"""
Capture images from webcam and other sources
"""

# from cv2 import VideoCapture
import cv2
from datetime import datetime
import time
import os


def capture_images(base_dir, delay=3, night_fac=20):
    assert os.path.isdir(base_dir), '%s not a directory' % base_dir
    cap = cv2.VideoCapture(0)  #set the port of the camera as before
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)
    while True:
        hour_dir = datetime.now().strftime('%Y-%m-%d_%H')
        hour_dir_path = os.path.join(base_dir, hour_dir)
        if not os.path.isdir(hour_dir_path):
            os.makedirs(hour_dir_path)
        retval, image = cap.read()
        newimage = cv2.flip(image, 0)
        newimage = cv2.flip(newimage, 1)

        img_filename = '%s.png' % datetime.now().strftime('%Y-%m-%d_%H:%M:%S.%f')
        img_path = os.path.join(hour_dir_path, img_filename)
        
        cv2.imwrite(img_path, newimage)
        if datetime.now().hour >= 20 or datetime.now().hour <= 5:
            sleeptime = delay * night_fac
        else:
            sleeptime = delay
        time.sleep(sleeptime - 0.107)
