import numpy as np
import cv2

def cross(x):
    pass

img = np.zeros((300, 512, 3), np.uint8)
cv2.namedWindow('Color Picker')

cv2.createTrackbar('Switch', 'Color Picker', 0, 1, cross)
cv2.createTrackbar('R', 'Color Picker', 0, 255, cross)
cv2.createTrackbar('G', 'Color Picker', 0, 255, cross)
cv2.createTrackbar('B', 'Color Picker', 0, 255, cross)

while True:
    cv2.imshow("Color Picker", img)
    s = cv2.getTrackbarPos('Switch', 'Color Picker')
    r = cv2.getTrackbarPos('R', 'Color Picker')
    g = cv2.getTrackbarPos('G', 'Color Picker')
    b = cv2.getTrackbarPos('B', 'Color Picker')

    if s == 0:
        img[:]= [0, 0, 0]
    else:
        img[:] = [b, g, r]

    if cv2.waitKey(1) == ord('q'):
        break

cv2.destroyAllWindows()
