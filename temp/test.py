import numpy as np
import cv2

cap = cv2.VideoCapture('./sourse/test.mp4')

fourcc = cv2.VideoWriter_fourcc(*'MJPG')
out = cv2.VideoWriter('./outputVideo/output.avi',fourcc, 20.0, (416,416))

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret==True:
        opencv_image = cv2.resize(frame, (416, 416))
        out.write(opencv_image)

        cv2.imshow('frame',opencv_image)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
      
cap.release()
out.release()
cv2.destroyAllWindows()