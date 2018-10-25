#!/usr/bin/python2
import cv2
import os

def name1():
	name=raw_input("enter name: ")
	name=name+".jpg"
	return name

x= name1()
cap=cv2.VideoCapture(0)
while True:
	status,frame=cap.read()
	grayimg=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	# showing current image
	cv2.imshow("current image",frame)
	if cv2.waitKey (1) & 0xFF == ord('q'):
		path = '/home/adhoc/Desktop/attendance/Gallery'
		cv2.imwrite(os.path.join(path , x),frame)	
		break

cv2.destroyAllWindows()
cap.release()
