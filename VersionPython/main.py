#coding = utf-8
from enum import Enum
from list import list

class Carac(Enum):
    esp = " " #0
    a = "a" #1
    err2 = "err2" #2
    c = "c" #3
    virg = "," #4
    b = "b" #5
    i = "i" #6
    f = "f" #7
    err8 = "err8" #8
    e = "e" #9
    err10 = "err10" #10
    d = "d" #11
    deux_pts = ":" #12
    h = "h" #13
    j = "j" #14
    g = "g" #15
    apost = "'" #16
    k = "k" #17
    err18 = "err18" #18
    m = "m" #19
    pts_virg = ";" #20
    l = "l" #21
    s = "s" #22
    p = "p" #23
    ast = "*" #24
    o = "o" #25
    err26 = "err26" #26
    n = "n" #27
    pts_exc = "!" #28
    r = "r" #29
    t = "t" #30 
    q = "q" #31
    Num = "00" #32
    un = "1" #33 
    Maj = "Maj" #34
    trois = "3" #35 
    pts_int = "!" #36
    deux = "2" #37
    neuf = "9" #38
    six = "6" #39
    err40 = "err40" #40
    cinq = "5" #41
    Ital = "Ital" #42
    quatre = "4" #43
    pts = "." #44
    huit = "8" #45
    w = "w" #46
    sept = "7" #47
    tir = "-" #48
    u = "u" #49
    err50 = "err50" #50
    x = "x" #51
    par_gau = "(" #52
    v = "v" #53
    e_gr = "è" #54
    c_ced = "ç" #55
    par_dr = ")" #56
    z = "z" #57
    zero = "0" #58
    y = "y" #59
    trem = "\"" #60
    err61 = "err61" #61
    u_gr = "ù" #62 
    e_ai = "é" #63
    

list_1 = [1,43,63,23,12]

def lecture(list_braille):
    x = len(list_braille)
    list_retour = []
    list_act = []
    for i in range(x):
        if list_braille[i] == 0 :
            list_retour.append(list_act)
            list_act = []
        else :
            list_act.append(Carac.list_braille[i])
    return list_retour

y = lecture(list_1)
print(y)

