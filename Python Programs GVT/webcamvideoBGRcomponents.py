#Capture video from the webcam and indiviually display BGR components. 
import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    #Original
    cv2.imshow("Original", frame)
    #Blue component
    cv2.imshow("blue component", frame[:,:,0])
    #Green component
    cv2.imshow("green component", frame[:,:,1])
    #Red component
    cv2.imshow("red component", frame[:,:,2])
    if cv2.waitKey(1) & 0XFF == ord("q"):
        break
cap.release()
cv2.destroyAllWindows()
