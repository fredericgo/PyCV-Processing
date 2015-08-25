#! /usr/bin/env python

import numpy as np
import Tkinter
from PIL import Image, ImageTk
import cv2
from Tkinter import Tk, RIGHT, BOTH, RAISED
from ttk import Frame, Button, Style


        # opencv2 stuffs
capture = cv2.VideoCapture(0)
        # do the matching
orb = cv2.ORB()
kp, des = None, None
bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

ret, frame = capture.read()

        # A root window for displaying objects
root = Tkinter.Tk()
ret, frame = capture.read()
    # Convert the Image object into a TkPhoto object
im = Image.fromarray(frame)
imgtk = ImageTk.PhotoImage(image=im)
panel = Tkinter.Label(root, image = imgtk)
panel.pack(side = "bottom", fill = "both", expand = "yes")

def captureImg():
    ret, frame = capture.read()
    # Convert the Image object into a TkPhoto object
    b,g,r = cv2.split(frame)
    frame = cv2.merge((r,g,b))

    im = Image.fromarray(frame)
    imgtk = ImageTk.PhotoImage(image=im)


    # Put it in the display window
    panel.configure(image = imgtk)
    panel.image = imgtk
    root.after(100, captureImg)


root.after(100, captureImg)

root.mainloop() # Start the GUI

