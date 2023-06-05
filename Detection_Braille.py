import cv2 as cv
import sys
import numpy as np

img = cv.imread('test.png',0)
if img is None:
    sys.exit("Impossible de lire l'image")
img = cv.medianBlur(img,5)
cimg = cv.cvtColor(img,cv.COLOR_GRAY2BGR)
circles = cv.HoughCircles(img,cv.HOUGH_GRADIENT,1,2,param1=1,param2=0.8,minRadius=0,maxRadius=0)
if circles is None:
    sys.exit("Pas de cercles detectes")
circles = np.uint16(np.around(circles))

for i in circles[0,:]:
    # draw the outer circle
    cv.circle(cimg,(i[0],i[1]),i[2],(0,255,0),2)
    # draw the center of the circle
    cv.circle(cimg,(i[0],i[1]),2,(0,0,255),3)
    
cv.imshow('Cercles detectes',cimg)
cv.waitKey(0)
cv.destroyAllWindows()