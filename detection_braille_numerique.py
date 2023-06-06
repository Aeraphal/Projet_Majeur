import numpy as np
import cv2 as cv

img = cv.imread('braille5.jpg', cv.IMREAD_GRAYSCALE)
assert img is not None, "file could not be read, check with os.path. exists()"

# Appliquer un seuil pour la binarisation
# seuil = 200  # Valeur du seuil (0-255)
# _, img = cv.threshold(img, seuil, 255, cv.THRESH_BINARY)

img = cv.medianBlur(img, 5)

# ouverture
kernel = np.ones((11,11),np.uint8)
img = cv.morphologyEx(img, cv.MORPH_ERODE,kernel)

cimg = cv.cvtColor(img, cv.COLOR_GRAY2BGR)

circles = cv.HoughCircles(img, cv.HOUGH_GRADIENT, 1, 100, param1=60, param2=30, minRadius=0, maxRadius=150)

if circles is not None:
    circles = np.uint16(np.around(circles))
    for i in circles[0, :]:
        # draw the outer Circle
        # cv.circle(cimg,(i[0],i[1]),i[2],(0,255,0),2)
        # draw the center of the circle
        cv.circle(cimg,(i[0],i[1]),2,(0,0,255),3)
else:
    print('Aucun cercle trouvé') 


cv.namedWindow('detected circles', cv.WINDOW_NORMAL)
cv.resizeWindow('detected circles', 800, 600)
cv.imshow('detected circles',cimg)
cv.waitKey(0)
cv.destroyAllWindows()
