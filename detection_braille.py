import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

# Lecture de l'image
img = cv.imread('braille15.png', cv.IMREAD_GRAYSCALE)
assert img is not None, "file could not be read, check with os.path. exists()"

# erosion
filterSize =(3, 3)
kernel = cv.getStructuringElement(cv.MORPH_RECT, filterSize)
img_erosion = cv.erode(img, kernel, iterations=1)

cimg = cv.cvtColor(img, cv.COLOR_GRAY2BGR)

#Detection des cercles
circles = cv.HoughCircles(img_erosion, cv.HOUGH_GRADIENT, 1, 6, param1=16, param2=8, minRadius=0, maxRadius=10)

# Trace des cercles detectes
if circles is not None:
    circles = np.uint16(np.around(circles))
    for i in circles[0,:]:
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

# Ajout des différentes hauteurs dans repre_hauteur
repere_hauteur.sort()
count = []
for i in range(len(repere_hauteur)-1):
    if repere_hauteur[i+1]-repere_hauteur[i] <= 2:
        repere_hauteur.append(int((repere_hauteur[i]+repere_hauteur[i+1])/2))
        for j,val in enumerate (circles[:,1]):
            if val == repere_hauteur[i+1] or val == repere_hauteur[i]:
                circles[j,1] = repere_hauteur[-1]
        count.append(repere_hauteur[i])
        count.append(repere_hauteur[i+1])

#Suppression des valeurs proches
for i in count:
    repere_hauteur.remove(i)
repere_hauteur.sort()


# Hauteurs classés par ligne
repere_hauteur_final = []
for i in range(int(len(repere_hauteur)/3)):
    repere_hauteur_final.append(repere_hauteur[i*3:(i+1)*3])

# Classement des longueurs des cercles
repere_longueur = []
for i in circles[:,0]:
    if i not in repere_longueur:
        repere_longueur.append(i)
        
repere_longueur.sort()
count2 = []
for i in range(len(repere_longueur)-1):
    if repere_longueur[i+1]-repere_longueur[i] <= 2:
        repere_longueur.append(repere_longueur[i+1])
        for j,val in enumerate (circles[:,0]):
            if val == repere_longueur[i+1] or val == repere_longueur[i]:
                circles[j,0] = repere_longueur[-1]
        count2.append(repere_longueur[i])
        count2.append(repere_longueur[i+1])

for i in count2:
    repere_longueur.remove(i)
repere_longueur.sort()

# Longueurs classées par ligne
repere_longueur_final = [[] for x in range(len(repere_hauteur_final))]
for i in range(len(circles)):
    for j in range(len(repere_hauteur_final)):
        for k in range(len(repere_longueur)):
            if circles[i,0] == repere_longueur[k] and circles[i,1] in repere_hauteur_final[j]:
                repere_longueur_final[j].append(repere_longueur[k])

for i in range(len(repere_longueur_final)):
    repere_longueur_final[i].sort()
print(repere_longueur_final)


# Calcul des distances entre deux cercles
espace1 = repere_longueur[-1]
espace2 = repere_longueur[-2]
distance = 0
for i in range(len(repere_longueur)-2):
    distance = repere_longueur[i+1]-repere_longueur[i]
    if espace1 > distance:
        espace1 = distance
    if abs(espace1 - distance) >= 2:
        if espace2 > distance:
            espace2 = distance


cv.namedWindow('detected circles', cv.WINDOW_NORMAL)
cv.resizeWindow('detected circles', 800, 600)
cv.imshow('detected circles',cimg)
cv.waitKey(0)
cv.destroyAllWindows()

