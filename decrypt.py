import cv2


#	Chaque lettre est individualisée dans sa case de grillage. 
#	On définit les position 1, 2, 3, 4, 5 et 6 qui correspondent à des cases pleines ou vides. (2^6 = 64 possibilités)
#	On effectue un traitement binaire avec ces informations. 
#Chaque résultat du traitement binaire renvoie un caractère bien précis.
#		Les résultats vident renvoie un espace.
#On stocke le résultat du traitement binaire dans une file. 



# A l'initialisation, nous avons un ensemble grillagé dont il faut décrypter chaque éléments
# A l'intérieur de chaque case, un autre damier de deux de côté et trois de hauteurs
# Chaque cases dans le damier est un bouléen. Soit il est vrai, soit il est faux
# Suivant la position de la case dans le damier, s'il est vrai, alors on renvoie une valeur, qui vaut 0 sinon
# On renvoie par le cumul des résultat à l'intérieur de chaque case du damier
# On fait cela pour l'ensemble du grillage

