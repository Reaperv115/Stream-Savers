import cv2
import numpy as np
import pyglet
import glob
import keyboard

types = ('*.gif', '*.webm', '*.mpeg')
gifs = []
for files in types:
    gifs.extend(glob.glob(files))
gifnum = 0
w, h = 600, 600
cap = cv2.VideoCapture(gifs[gifnum])
black = cv2.imread('black.png')

if (cap.isOpened() == False):
    print("failed to open file")
while (cap.isOpened()):
    ret, frame = cap.read()

    if (keyboard.is_pressed('n')):
        gifnum += 1
        if (gifnum >= len(gifs)):
            gifnum = 0
        cap = cv2.VideoCapture(gifs[gifnum])
        ret, frame = cap.read()
    if (keyboard.is_pressed('l')):
        gifnum -= 1
        if (gifnum < 0):
            gifnum = len(gifs) - 1
        cap = cv2.VideoCapture(gifs[gifnum])
        ret, frame = cap.read()

    if (ret == True):
        cv2.namedWindow('video', cv2.WND_PROP_FULLSCREEN)
        cv2.imshow('video', frame)
        if (cv2.waitKey(50) & 0xFF == ord('q')):
            break
    else:
        cap.release()
        cv2.imshow('video', black)
        if (cv2.waitKey(5000) & 0xFF == ord('q')):
            break
        gifnum += 1
        if gifnum >= len(gifs):
            gifnum = 0
        cap = cv2.VideoCapture(gifs[gifnum])
        

cap.release()
cv2.destroyAllWindows()