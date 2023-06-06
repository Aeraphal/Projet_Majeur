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

# Trace des cercles detectes
if circles is not None:
    circles = np.uint16(np.around(circles))
    for i in circles[0, :]:
        # Trace du contour du cercle
        cv.circle(cimg,(i[0],i[1]),i[2],(0,255,0),2)
        # Trace du centre du cercle
        cv.circle(cimg,(i[0],i[1]),2,(0,0,255),3)
else:
    print('Aucun cercle trouvé') 

# Classement des hauteurs des cercles
repere_hauteur = []
circles = circles[0]
for i in circles[:,1]:
    if i not in repere_hauteur:
        repere_hauteur.append(i)

repere_hauteur.sort()
for i in range(len(repere_hauteur)-2):
    if repere_hauteur[i+1]-repere_hauteur[i] <= 2:
        repere_hauteur.append(int((repere_hauteur[i]+repere_hauteur[i+1])/2))
        repere_hauteur.pop(i)
        repere_hauteur.pop(i)
        repere_hauteur.sort()

# Classement des longueurs des cercles
repere_longueur = []
for i in circles[:,0]:
    if i not in repere_longueur:
        repere_longueur.append(i)
        
repere_longueur.sort()
for i in range(len(repere_longueur)-3):
    if repere_longueur[i+1]-repere_longueur[i] <= 2:
        repere_longueur.append(repere_longueur[i+1])
        repere_longueur.pop(i)
        repere_longueur.pop(i)
        repere_longueur.sort()

# Calcul des distances entre deux cercles
espace1 = repere_longueur[-1]
espace2 = repere_longueur[-2]
distance_petite = 500
distance = 0
repere_longueur_final = []
repere_hauteur_final = []
for i in range(len(repere_longueur)-2):
    distance = repere_longueur[i+1]-repere_longueur[i]
    if espace1 > distance:
        espace1 = distance
    if abs(espace1 - distance) >= 2:
        if espace2 > distance:
            espace2 = distance
#     if distance_petite > distance:
#         distance_petite = distance   
            
# print(distance_petite)

cv.namedWindow('detected circles', cv.WINDOW_NORMAL)
cv.resizeWindow('detected circles', 800, 600)
cv.imshow('detected circles',cimg)
cv.waitKey(0)
cv.destroyAllWindows()

