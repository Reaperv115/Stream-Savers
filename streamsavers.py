import cv2
import numpy as np
import pyglet
import glob
import keyboard

#loading all video-type files 
types = ('*.gif', '*.webm', '*.mpeg')
gifs = []
for files in types:
    gifs.extend(glob.glob(files))

#video index
gifnum = 0

#video stream
cap = cv2.VideoCapture(gifs[gifnum])

#pause image
black = cv2.imread('black.png')

#making sure the video stream was successfully opened
if (cap.isOpened() == False):
    print("failed to open file")

while (cap.isOpened()):

    #ret is true if you returned with a valid frame, otherwise false
    #frame is the actual frame data to display
    ret, frame = cap.read()

    #checking for keyboard input to change video
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

    #if ret is true display the video frame
    if (ret == True):
        cv2.namedWindow('video', cv2.WND_PROP_FULLSCREEN)
        cv2.imshow('video', frame)
        if (cv2.waitKey(50) & 0xFF == ord('q')):
            break
    #else pause on the black screen and start next video
    else:
        cap.release()
        cv2.imshow('video', black)
        if (cv2.waitKey(5000) & 0xFF == ord('q')):
            break
        gifnum += 1
        if gifnum >= len(gifs):
            gifnum = 0
        cap = cv2.VideoCapture(gifs[gifnum])
        
# close video stream and destroy all windows
cap.release()
cv2.destroyAllWindows()