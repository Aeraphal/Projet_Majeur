import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
#coding = utf-8
from enum import Enum

Carac = [" ", #0
    "a", #1
    "err2", #2
    "c", #3
    ",", #4
    "b", #5
    "i", #6
    "f", #7
    "err8", #8
    "e", #9
    "err10", #10
    "d", #11
    ":", #12
    "h", #13
    "j", #14
    "g", #15
    "'", #16
    "k", #17
    "err18", #18
    "m", #19
    ";", #20
    "l", #21
    "s", #22
    "p", #23
    "*", #24
    "o", #25
    "err26", #26
    "n", #27
    "!", #28
    "r", #29
    "t", #30 
    "q", #31
    "Num", #32
    "1", #33 
    "Maj", #34
    "3", #35 
    "!", #36
    "2", #37
    "9", #38
    "6", #39
    "err40", #40
    "5", #41
    "Ital", #42
    "4", #43
    ".", #44
    "8", #45
    "w", #46
    "7", #47
    "-", #48
    "u", #49
    "err50", #50
    "x", #51
    "(", #52
    "v", #53
    "è", #54
    "ç", #55
    ")", #56
    "z", #57
    "0", #58
    "y", #59
    "\"", #60
    "err61", #61
    "ù", #62 
    "é"] #63


# Lecture de l'image
img = cv.imread('braille14.png', cv.IMREAD_GRAYSCALE)
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
rayon = 2
for i in range(len(repere_hauteur)-1):
    if repere_hauteur[i+1]-repere_hauteur[i] <= rayon:
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
    if repere_longueur[i+1]-repere_longueur[i] <= rayon:
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
repere_hauteur_final_2 = [[] for x in range(len(repere_hauteur_final))]
for i in range(len(circles)):
    for j in range(len(repere_hauteur_final)):
        for k in range(len(repere_longueur)):
            if circles[i,0] == repere_longueur[k] and circles[i,1] in repere_hauteur_final[j]:
                repere_longueur_final[j].append(repere_longueur[k])
                repere_hauteur_final_2[j].append(circles[i,1])


min = 0


def tri_insertion(La,Ha):
    L = La
    H = Ha
    N = len(L)
    for n in range(1,N):
        cle = L[n]
        j = n-1
        while j>=0 and L[j] > cle:
            L[j+1], L[j] = L[j], L[j+1] # decalage
            H[j+1], H[j] = H[j], H[j+1]
            j = j-1
    return(L,H)

truc1 = []
truc2 = []
for i in range(len(repere_longueur_final)):
    tri_insertion(repere_longueur_final[i],repere_hauteur_final_2[i])




# Calcul des distances entre deux cercles
espace1 = repere_longueur[-1]
espace2 = repere_longueur[-2]
distance = 0
for i in range(len(repere_longueur_final[0])-2):
    distance = repere_longueur_final[0][i+1]-repere_longueur_final[0][i]
    if distance > rayon:
        if espace1+rayon > distance :                  # distance < espace1 < distance + 2
            espace1 = distance
        elif espace2 > distance and (espace1 + rayon) < distance :
            espace2 = distance  
espace_final = (espace1 + espace2) / 2

list_caractere = []
caractere = []
for i in range(len(repere_hauteur_final_2)):
    list_caractere.append([])
    caractere = [[repere_longueur_final[i][0], repere_hauteur_final_2[i][0]]]
    for k in range(len(repere_hauteur_final_2[i])-1):
        if repere_longueur_final[i][k+1] - repere_longueur_final[i][k] < espace_final:
            caractere.append([repere_longueur_final[i][k+1],repere_hauteur_final_2[i][k+1]])
        elif repere_longueur_final[i][k+1] - repere_longueur_final[i][k] > espace_final+espace1: 
            list_caractere[i].append(caractere)
            caractere = [[repere_longueur_final[i][k+1],repere_hauteur_final_2[i][k+1]]]
            list_caractere[i].append([])
        else : 
            list_caractere[i].append(caractere)
            caractere = [[repere_longueur_final[i][k+1],repere_hauteur_final_2[i][k+1]]]
    list_caractere[i].append(caractere)

print("la liste de caractère cripté donne : ", list_caractere, "ayant ", len(list_caractere), " composant.")


list_caractere_uint8 = []
#Selection des lignes
for i in range(len(list_caractere)):
    #Selection des caracteres
    for j in range(len(list_caractere[i])):
        #Selection des points dans les caractères
        tot = 0
        if list_caractere[i][j] != []:
            min_long = list_caractere[i][j][0][0]
            max_long = list_caractere[i][j][0][0]
            rep_haut = [repere_hauteur[3*i], repere_hauteur[3*i+1], repere_hauteur[3*i+2]]
            for k in range(len(list_caractere[i][j])):
                if max_long < list_caractere[i][j][k][0]:
                    max_long = list_caractere[i][j][k][0]
            if max_long == min_long:
                if i < len(list_caractere[i])-1:
                    if j < len(list_caractere[i]) -1 :
                        if (list_caractere[i][j+1] != []):
                            if list_caractere[i][j+1][0][0] - list_caractere[i][j][-1][0] > espace_final :
                                min_long = min_long - espace1
                            else:
                                max_long = max_long + espace1
                    else:
                        max_long = max_long + espace1
                else : 
                    max_long = max_long + espace1
            rep_long = [min_long, max_long]

            for u in range(3):
                for v in range(2):
                    # print([rep_long[v],rep_haut[u]])
                    # print(list_caractere[i][j])
                    # print([rep_long[v],rep_haut[u]] in list_caractere[i][j])
                    if ([rep_long[v],rep_haut[u]] in list_caractere[i][j]):
                        tot = tot + 2**(2*u+v)


        list_caractere_uint8.append(tot)

print("la file décripté nous renvoie", list_caractere_uint8)

def lecture(list_braille):
    x = len(list_braille)
    list_retour = 'Texte : '
    sauv_maj = 0
    for i in range(x):
        verif_maj = list_braille[i]
        lettre = Carac[verif_maj]
        if verif_maj == 34:
            sauv_maj = 1
        else:
            if sauv_maj == 1:
                list_retour = list_retour + lettre.upper()
                sauv_maj = 0
            else:
                list_retour = list_retour + lettre

    return list_retour



k = []
for i in range(len(list_caractere_uint8)):
    k = lecture(list_caractere_uint8)


print(k)

print("espace 1 = ", espace1, ", l'espace 2 = ", espace2, " et l'espace final = ", espace_final)
print(repere_longueur_final)

cv.namedWindow('detected circles', cv.WINDOW_NORMAL)
cv.resizeWindow('detected circles', 800, 600)
cv.imshow('detected circles',cimg)
cv.waitKey(0)
cv.destroyAllWindows()
