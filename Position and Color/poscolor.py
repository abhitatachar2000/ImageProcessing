import cv2
import numpy

def mouse_event(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        text = '( '+str(x)+', '+str(y)+' )'
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img, text, (x,y), font, 1, (0,255,0), 2)
    
    if event == cv2.EVENT_RBUTTONDOWN:
        b = img[y, x, 0]
        g = img[y, x, 1]
        r = img[y, x, 2]
        text = '( '+str(b)+', '+str(g)+ ', '+ str(r)+' )'
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img, text, (x,y), font, 1, (0,255,0), 2)

cv2.namedWindow(winname='Frame')
img = cv2.imread('./imagepath') #Replace Path here
cv2.setMouseCallback('Frame', mouse_event)

while True:
    cv2.imshow('Frame', img)
    if cv2.waitKey(1) == ord('q'):
        break

cv2.destroyAllWindows()
