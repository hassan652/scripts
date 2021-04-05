#Program to capture image from a camera and display it on the screen

import cv2

#capture the camera
cap = cv2.VideoCapture(0)

#capture the frame
ret, frame = cap.read()

#Display the resulting frame
cv2.imshow("photo",frame)
print("frame shape",frame.shape)

#write the resulting image to .jpg file
cv2.imwrite("pycolorphoto.jpg", frame)

#Keep the photo open until pressed "q"
while True:
   if cv2.waitKey(1) & 0XFF == ord("q"):
        break

#releasing the capture
cap.release()
cv2.destroyAllWindows()