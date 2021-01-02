# -*- coding: utf-8 -*-
"""
Created on Sat Jan  2 16:40:02 2021

@author: Niall
"""

#Get used input for the program

def user_input():
    print("Please enter the name of the jpg image you would like facial detection performed on,")
    print("Its important that this image is stored in the same directory as the program")
    user_i = input("Enter the filename including the .jpg extension: ")
    tester = user_i.endswith(".jpg")
    if(tester == False):
        print("")
        print("Incorrect input")
        print("")
        user_input()
    return user_i