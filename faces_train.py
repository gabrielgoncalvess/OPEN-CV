# -*- coding: utf-8 -*-
"""
Created on Sat Mar  6 20:03:08 2021

@author: gabre
"""

import os
import cv2 as cv
import numpy as np

people = ["Christian Bale", "Margot Robbie", "Tom Welling"]
    
DIR = r"pasta com subpastas contendo as fotos de treino"

haar_cascade = cv.CascadeClassifier(r"/haar_face.xml")

features = []
labels = []


def create_train():
    for person in people:
        path = os.path.join(DIR, person)
        label = people.index(person)

        for img in os.listdir(path):
            img_path = os.path.join(path,img)

            img_array = cv.imread(img_path)
            if img_array is None:
                continue 
                
            gray = cv.cvtColor(img_array, cv.COLOR_BGR2GRAY)

            faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4) # 4

            for (x,y,w,h) in faces_rect:
                faces_roi = gray[y:y+h, x:x+w]
                features.append(faces_roi)
                labels.append(label)
                

                
                
create_train()
print("Training Done -------------------")

features = np.array(features, dtype="object")
labels = np.array(labels)

face_recognizer = cv.face.LBPHFaceRecognizer_create()


# Train the Recognizer on the features list and the labels list
face_recognizer.train(features,labels)

face_recognizer.save('face_trained.yml')
np.save('features.npy', features)
np.save('labels.npy', labels)




            
    