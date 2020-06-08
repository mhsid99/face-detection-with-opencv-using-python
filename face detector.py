# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 03:36:36 2020

@author: Hamza
"""

import cv2
face=cv2.CascadeClassifier(r"D:\Projects\Project Resources\haarcascade_frontalface_default.xml")
img=cv2.imread(r"D:\Projects\Project Resources\champs.jpg",1)
#you can add any pic you want with a face.
#champs here is my favorite fotball club,Liverpool :P(I am a huge football fan xD)
faces=face.detectMultiScale(img)
count=0
for(x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
        count+=1
print("\nNo of faces detected:",count)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
#detects all faces in the picture and prints the total number of faces detected. It may also detect a non living face. like a statue.
for lists in faces:
        (x,y,w,h)=lists
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
        lists=img[y:y+h,x:x+w]
        face_resize=cv2.resize(lists,(100,100))
        cv2.imshow('image',face_resize)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
#to show the faces only one by one