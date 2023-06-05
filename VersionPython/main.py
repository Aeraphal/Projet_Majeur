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
    "00", #32
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
    
#J'aime la choucroute!
list_1 = [34,14,16,1,6,19,9,0,21,1,0,3,1]

def lecture(list_braille):
    x = len(list_braille)
    list_retour = 'Texte : '
    sauv_maj = 0
    for i in range(x):
        verif_maj = list_braille[i]
        lettre = Carac[verif_maj]
        print("i = ", i)
        print("La lettre est = ", lettre)
        if verif_maj == 34:
            sauv_maj = 1
        else:
            if sauv_maj == 1:
                list_retour = list_retour + lettre.upper()
                sauv_maj = 0
            else:
                print 
                list_retour = list_retour + lettre
        print("La liste retour est = ", list_retour)

    return list_retour

y = lecture(list_1)
print(y)

