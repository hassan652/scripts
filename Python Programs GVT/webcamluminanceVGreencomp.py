#Capture video from the webcam and compare green component and luminance. 
import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    #Original
    cv2.imshow("Original", frame)
    #luminance (normalizing by 256 because imshow expects a float number between 0 and 1)
    Y = (0.114*frame[:,:,0]+0.587*frame[:,:,1]+0.299*frame[:,:,2])/256
    cv2.imshow("Y component", Y)
    #green component
    cv2.imshow("green component", frame[:,:,1])
    if cv2.waitKey(1) & 0XFF == ord("q"):
        break
cap.release()
cv2.destroyAllWindows()