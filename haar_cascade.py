# -*- coding: utf-8 -*-
"""
Created on Sat Jan  2 16:14:09 2021

@author: Niall
"""

import numpy as np
import cv2
import user_input


#xml files including the trainer parts
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

def grayscale():
    """
    Ask a user for input and grayscale an image

    Returns
    -------
    gray : image file
        A grayscaled image.
    img : image file
        A user inputted image.

    """
    try:
        img = cv2.imread(user_input.user_input())
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        return gray,img
    except(cv2.error):
        print("Image file was incorrectly entered please enter again")
        grayscale()

def draw_faces(img,gray):
    """
    Use the haar cascade model to find and draw faces on a specified image.

    Parameters
    ----------
    gray : image file
        A grayscaled image.
    img : image file
        A user inputted image.


    Returns
    -------
    None.

    """
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
            
if __name__ == "__main__":
    gray,img = grayscale()  
    draw_faces(img,gray)
    
    cv2.imshow('img',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()