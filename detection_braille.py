import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

# Lecture de l'image
img = cv.imread('braille14.png', cv.IMREAD_GRAYSCALE)
assert img is not None, "file could not be read, check with os.path. exists()"

# Top-hat
filterSize =(3, 3)
kernel = cv.getStructuringElement(cv.MORPH_RECT, filterSize)
tophat_img = cv.morphologyEx(img, cv.MORPH_TOPHAT, kernel)

# Seuillage simple
img = cv.split(img)[0]
(retVal, newImg) = cv.threshold(img, 10, 255, cv.THRESH_BINARY)

# Ouverture de l'image
img_dilation = cv.dilate(img, kernel, iterations=1)
img_erosion = cv.erode(img, kernel, iterations=1)

cimg = cv.cvtColor(img, cv.COLOR_GRAY2BGR)

#Detection des cercles
circles = cv.HoughCircles(img_erosion, cv.HOUGH_GRADIENT, 1, 6, param1=16, param2=8, minRadius=0, maxRadius=10)

min_y = 100
# Trace des cercles detectes
if circles is not None:
    circles = np.uint16(np.around(circles))
    for i in circles[0, :]:
        # Trace du contour du cercle
        cv.circle(cimg,(i[0],i[1]),i[2],(0,255,0),2)
        # Trace du centre du cercle
        cv.circle(cimg,(i[0],i[1]),2,(0,0,255),3)
        
        # Pour quadrillage
        if i[1] < min_y:
            min_y = i[1]
else:
    print('Aucun cercle trouvé') 

print(circles)
print(min_y)

cv.namedWindow('detected circles', cv.WINDOW_NORMAL)
cv.resizeWindow('detected circles', 800, 600)
cv.line(cimg, (0, min_y), (500, min_y), (0, 0, 255))
cv.imshow('detected circles',cimg)

# Trace du quadrillage


cv.waitKey(0)
cv.destroyAllWindows()
