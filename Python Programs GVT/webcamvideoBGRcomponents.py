#Capture video from the webcam
import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    #original
    cv2.imshow("live", frame)
    #blue component
    cv2.imshow("blue component", frame[:,:,0])
    #green component
    cv2.imshow("green component", frame[:,:,1])
    #red component 
    cv2.imshow("red component", frame[:,:,2])
    if cv2.waitKey(1) & 0XFF == ord("q"):
        break
cap.release()
cv2.destroyAllWindows()