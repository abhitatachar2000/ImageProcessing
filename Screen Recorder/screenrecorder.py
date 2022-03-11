import cv2
import numpy as np
import pyautogui as pg
from datetime import datetime
current = str(datetime.now())
#Capture Screensize
path = './screenrecord.avi'
resolution = pg.size()
fourcc = cv2.VideoWriter_fourcc(*"XVID")
fps =25.0
output = cv2.VideoWriter(path, fourcc, fps, resolution)
cv2.namedWindow('Screen_Recording', cv2.WINDOW_NORMAL)
cv2.resizeWindow('Screen_Recording', (600, 400))

while True:
    frame = pg.screenshot()
    frame = np.array(frame)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(frame, current, (50, 50), font, 0.5, (0,0,255), 2)
    cv2.imshow('frame', frame)
    output.write(frame)
    if cv2.waitKey(1) == ord('q'):
        break

output.release()
cv2.destroyAllWindows()
