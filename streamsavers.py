import cv2
import numpy as np
import pyglet
import glob
import time
import msvcrt
import os

gifs = glob.glob('*.gif')
gifnum = 0
w, h = 600, 600
cap = cv2.VideoCapture(gifs[gifnum])
black = cv2.imread('black.png')

if (cap.isOpened() == False):
    print("failed to open file")
while (cap.isOpened()):
    ret, frame = cap.read()

    if (ret == True):
        cv2.namedWindow('video', cv2.WND_PROP_FULLSCREEN)
        cv2.imshow('video', frame)
        if (cv2.waitKey(25) & 0xFF == ord('q')):
            break
    else:
        cv2.imshow('video', black)
        if (cv2.waitKey(25) & 0xFF == ord('q')):
            break
        time.sleep(5)
        gifnum += 1
        if gifnum >= len(gifs):
            gifnum = 0
        cap = cv2.VideoCapture(gifs[gifnum])
        

cap.release()
cv2.destroyAllWindows()