import cv2
import numpy as np
import sqlite3
import dlib
import os

cap = cv2.VideoCapture(0)
detector = dlib.get_frontal_face_detector()

# this function is for database
def insertOrUpdate(Id, Name, roll) :
# connecting to the database
    connect = sqlite3.connect("Face-DataBase")
    # selecting the row of an id into consideration
    cmd = "SELECT * FROM Students WHERE ID = " + Id
    cursor = connect.execute(cmd)
    isRecordExist = 0
    # checking wheather the id exist or not
    for row in cursor:
        isRecordExist = 1
    # updating name and roll no
    if isRecordExist == 1:
        connect.execute("UPDATE Students SET Name = ? WHERE ID = ?",(Name, Id))
        connect.execute("UPDATE Students SET Roll = ? WHERE ID = ?",(roll, Id))
    else:
        # insering a new student data
    	params = (Id, Name, roll)
    	connect.execute("INSERT INTO Students(ID, Name, Roll) VALUES(?, ?, ?)", params)
    # commiting into the database
    connect.commit()
    # closing the connection
    connect.close()

name = raw_input("Enter student's name : ").capitalize()
roll = raw_input("Enter student's Roll Number : ")
Id = roll[-3:]
# calling the sqlite3 database
insertOrUpdate(Id, name, roll)

# creating the person or user folder
folderName = "user" + Id
folderPath = os.path.join(os.path.dirname(os.path.realpath(__file__)), "dataset/"+folderName)
if not os.path.exists(folderPath):
    os.makedirs(folderPath)

sampleNum = 0
while(True):
    # reading the camera input
    ret, img = cap.read()
    # Converting to GrayScale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    dets = detector(img, 1)
    # loop will run for each face detected
    for i, d in enumerate(dets):
        sampleNum += 1
        # Saving the faces
        cv2.imwrite(folderPath + "/User." + Id + "." + str(sampleNum) + ".jpg",img[d.top():d.bottom(), d.left():d.right()])
        # Forming the rectangle
        cv2.rectangle(img, (d.left(), d.top())  ,(d.right(), d.bottom()),(0,255,0) ,2)
        # waiting time of 200 milisecond
        cv2.waitKey(200)
    # showing the video input from camera on window
    cv2.imshow('frame', img)
    cv2.waitKey(1)
    # will take 5 faces
    if(sampleNum >= 5):
        break

cap.release()
cv2.destroyAllWindows()
