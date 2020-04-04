# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 18:55:31 2020

@author: Gaurav
"""


import sys
import webbrowser

sys.argv
#Just because loaction always greater then 1 charecter
if (len(sys.argv)>1):
    location=" ".join(sys.argv[1:])
else:
    location=input("Enter the loction")

webbrowser.open("https://www.google.co.in/maps/place/"+location)