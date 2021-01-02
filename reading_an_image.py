# -*- coding: utf-8 -*-
"""
Created on Thu Dec 31 02:47:43 2020

@author: Niall
"""

import cv2 as cv2

a_very_very_good_game = cv2.imread("Witcher_3_cover_art.jpg")

cv2.imshow('image',a_very_very_good_game)
cv2.waitKey()

gray_image = cv2.cvtColor(a_very_very_good_game, cv2.COLOR_BGR2GRAY)

cv2.imshow('Grayscale', gray_image) 
cv2.waitKey(0)

cv2.destroyAllWindows() 