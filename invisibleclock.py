import cv2
import numpy as np
import time

rawvideo=  cv2.VideoCapture(0)
time.sleep(2)
count= 0
background= 0
for i in range(68):
    ret, background= rawvideo.read()
    if not ret:
        continue
background= np.flip(background, axis=1)

while rawvideo.isOpened():
    ret, frame= rawvideo.read()
    if not ret:
        break
    count+= 1
    frame= np.flip(frame, axis=1)
    hsv= cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lowerred= np.array([100,40,40])
    upperred=np.array([155,255,255])
    mask1= cv2.inRange(hsv, lowerred, upperred)

    lowerred= np.array([150,40,40])
    upperred=np.array([180,255,255])
    mask2= cv2.inRange(hsv, lowerred, upperred)
    mask=mask1+mask2