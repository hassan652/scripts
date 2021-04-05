#Program to take live video from the webcam and show Y, U and V components separately

import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
   retval, frame = cap.read()
   #Displaying original frame
   cv2.imshow('Original', frame)
   #Displaying Y component
   Y = (0.114*frame[:,:,0]+0.587*frame[:,:,1]+0.299*frame[:,:,2])/255
   cv2.imshow('Y component',Y)
   #Displaying U component
   U = (frame[:,:,0]/255.0)-Y
   cv2.imshow("U component", np.abs(U))
   #Displaying V component
   V = (frame[:,:,2]/255.0)-Y
   cv2.imshow("V component", np.abs(V))
   if cv2.waitKey(1) & 0XFF == ord("q"):
   	break
#When everything is done, release the capture
cap.release()
cv2.destroyAllWindows()
