"""
https://github.com/isha-git
https://github.com/shripriyamaheshwari
"""

import numpy as np
import cv2

#this is the cascade we just made. Call what you want

amb_cascade = cv2.CascadeClassifier('cascade.xml')
print(amb_cascade.empty())
cap = cv2.VideoCapture('ambulance.mp4')
#cap = cv2.VideoCapture(0)			# For detection using web camera
while 1:
    ret, img = cap.read()
    #print(cv2.COLOR_BGR2GRAY)	
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    #print(gray)
    # add this
    # image, reject levels level weights.
    amb = amb_cascade.detectMultiScale(gray, 1.11, 2)
    
    #print("--", amb)
    # add this
    for (x,y,w,h) in amb:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,0),2)
	print("detected")


    cv2.imshow('img',img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
