import cv2 as cv2
import numpy as np
from datetime import datetime

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
output = cv2.VideoWriter('./savedfile.avi', fourcc, 20.0, (640, 480), 0)
while True:
    ret, frame = cap.read()
    if ret:
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        current = datetime.now()
        current = str(current)
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(frame, current, (50,50), font, 0.5, (0,0,255), 2)
        cv2.imshow('frame', frame)
        output.write(frame)
        if cv2.waitKey(1) == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
