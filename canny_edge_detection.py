# -*- coding: utf-8 -*-
"""
Created on Thu Dec 31 13:20:54 2020

@author: Niall
"""

import cv2 
import numpy as np 

FILE_NAME = 'group_photo.jpg'
try: 
	# Read image from disk. 
    img = cv2.imread(FILE_NAME) 

	# Canny edge detection. 
    edges = cv2.Canny(img, 100, 200) 
    
    cv2.imshow('canny', edges) 
    cv2.waitKey(0)

	# Write image back to disk. 
    cv2.imwrite(f'{FILE_NAME}_result.jpg', edges) 
except IOError: 
	print ('Error while reading files !!!') 
