import cv2 as cv2
import numpy as np
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
count = 0
while True:
    ret, frame = cap.read()  
    if ret:  
        cv2.imshow('frame', frame)
        cv2.imwrite('./frames{0}.jpg'.format(count), frame)
        count=count+1
        #output.write(frame)
        if cv2.waitKey(1) == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
