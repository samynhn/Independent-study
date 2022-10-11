import cv2
import time
from PIL import Image

cap = cv2.VideoCapture('test.mp4')
count = 1
# img = Image.open("test1.jpg")

while(cap.isOpened()):
  ret, frame = cap.read()
  count += 1
  if(count%2==0):

    image = cv2.resize(frame, (416, 416))
    cv2.imshow('frame', image)
    # time.sleep(0.1)
  else:      
    # time.sleep(0.1)
    continue

  if cv2.waitKey(60) & 0xFF == ord('q'):
    break

cap.release()
cv2.destroyAllWindows()