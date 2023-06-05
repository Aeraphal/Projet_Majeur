import numpy as np
import cv2 as cv

img = cv.imread('braille1.png', cv.IMREAD_GRAYSCALE)
assert img is not None, "file could not be read, check with os.path. exists()"
img = cv.medianBlur(img, 5)
cimg = cv.cvtColor(img, cv.COLOR_GRAY2BGR)

circles = cv.HoughCircles(img, cv.HOUGH_GRADIENT, 1, 20, param1=20, param2=10, minRadius=0, maxRadius=15)

if circles is not None:
    circles = np.uint16(np.around(circles))
    for i in circles[0, :]:
        # draw the outer Circle
        cv.circle(cimg,(i[0],i[1]),i[2],(0,255,0),2)
        # draw the center of the circle
        cv.circle(cimg,(i[0],i[1]),2,(0,0,255),3)
else:
    print('Aucun cercle trouvé') 


cv.namedWindow('detected circles', cv.WINDOW_NORMAL)
cv.resizeWindow('detected circles', 800, 600)
cv.imshow('detected circles',cimg)
cv.waitKey(0)
cv.destroyAllWindows()
