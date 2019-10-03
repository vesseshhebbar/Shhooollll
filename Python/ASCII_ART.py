# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 13:50:49 2019

@author: student
"""
'''
# #-#-#-#-#-#-#-#-#-# GCD of 2 numbers -#-#-#-#-#-#-#-#-#

def GCD(a, b):
    for i in range(max(a, b), 0, -1):
        if(a%i==0 and b%i==0):
            return i        
x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))

print("\nGCD is", GCD(x, y))
print("\n-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-")

# +-+-+-+-+-+-+-+-+- ASCII of two numbers +-+-+-+-+-+-+-+

def Ascii(c):
    return(ord(c))
c = input("Enter any character: ")
print("\nASCII value of", c, "is", Ascii(c))
print()
print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
print()
'''
# *^*^*^*^*^*^*^*^*^*^*^*^* FUN *^*^*^*^*^*^*^*^*^*^*

def line1():
    for i in range(0,7):
        print("F", end = '')
    for i in range(0,5):
        print(' ', end = '')
    print("U", end = '')
    for i in range(0,5):
        print(' ', end = '')
    print("U", end = '')
    for i in range(0,5):
        print(' ', end = '')
    print("NN", end = '')
    for i in range(0,4):
        print(' ', end = '')
    print("NN")
def line2():
    for i in range(0,2):
        print("F", end = '')
    for i in range(0,10):
        print(' ', end = '')
    print("U", end = '')
    for i in range(0,5):
        print(' ', end = '')
    print("U", end = '')
    for i in range(0,5):
        print(' ', end = '')
    print("NN", end = '')
    for i in range(0,4):
        if(i==0):
            print("N", end = '')
        else:
            print(' ', end = '')
    print("NN")
def line3():
    for i in range(0,7):
        print("F", end = '')
    for i in range(0,5):
        print(' ', end = '')
    print("U", end = '')
    for i in range(0,5):
        print(' ', end = '')
    print("U", end = '')
    for i in range(0,5):
        print(' ', end = '')
    print("NN", end = '')
    for i in range(0,4):
        if(i==1):
            print("N", end = '')
        else:
            print(' ', end = '')
    print("NN")
def line4():
    for i in range(0,2):
        print("F", end = '')
    for i in range(0,11):
        print(' ', end = '')
    print("U", end = '')
    for i in range(0,3):
        print(' ', end = '')
    print("U", end = '')
    for i in range(0,6):
        print(' ', end = '')
    print("NN", end = '')
    for i in range(0,4):
        if(i==2):
            print("N", end = '')
        else:
            print(' ', end = '')
    print("NN")
def line5():
    for i in range(0,2):
        print("F", end = '')
    for i in range(0,12):
        print(' ', end = '')
    print("UUU", end = '')
    for i in range(0,7):
        print(' ', end = '')
    print("NN", end = '')
    for i in range(0,3):
        print(' ', end = '')
    print("NNN")

line1()
line2()
line3()
line4()
line5()

def A(ln):
    if(ln==1):
        return "   A   " 
    if(ln==2):
        return "  A A  "
    if(ln==3):
        return " A   A "
    if(ln==4):
        return "AAAAAAA"
    if(ln==5):
        return "A     A"
    
def B(ln):
    if(ln==1):
        return "BBBB   " 
    if(ln==2):
        return "B   BB "
    if(ln==3):
        return "BBBB   "
    if(ln==4):
        return "B    BB"
    if(ln==5):
        return "BBBBB  " 

def C(ln):
    if(ln==1):
        return "   CCCC" 
    if(ln==2):
        return " CC    "
    if(ln==3):
        return "CC     "
    if(ln==4):
        return " CC    "
    if(ln==5):
        return "   CCCC"

def D(ln):
    if(ln==1):
        return "DDDD   " 
    if(ln==2):
        return "DD  DD "
    if(ln==3):
        return "DD   DD"
    if(ln==4):
        return "DD  DD "
    if(ln==5):
        return "DDDD   "

def E(ln):
    if(ln==1):
        return "EEEEEEE" 
    if(ln==2):
        return "EE     "
    if(ln==3):
        return "EEEEE  "
    if(ln==4):
        return "EE     "
    if(ln==5):
        return "EEEEEEE"

def F(ln):
    if(ln==1):
        return "FFFFFFF" 
    if(ln==2):
        return "FF     "
    if(ln==3):
        return "FFFFF  "
    if(ln==4):
        return "FF     "
    if(ln==5):
        return "FF     "

def G(ln):
    if(ln==1):
        return "  GGGGG" 
    if(ln==2):
        return " GG    "
    if(ln==3):
        return "GG  GGG"
    if(ln==4):
        return " GG   G"
    if(ln==5):
        return "  GGGGG"

def H(ln):
    if(ln==1):
        return "HH   HH" 
    if(ln==2):
        return "HH   HH"
    if(ln==3):
        return "HHHHHHH"
    if(ln==4):
        return "HH   HH"
    if(ln==5):
        return "HH   HH"

def I(ln):
    if(ln==1):
        return " IIIII " 
    if(ln==2):
        return "  III  "
    if(ln==3):
        return "  III  "
    if(ln==4):
        return "  III  "
    if(ln==5):
        return " IIIII "

def J(ln):
    if(ln==1):
        return "JJJJJJJ" 
    if(ln==2):
        return "   JJ  "
    if(ln==3):
        return "   JJ  "
    if(ln==4):
        return "J  JJ  "
    if(ln==5):
        return " JJJ   "

def K(ln):
    if(ln==1):
        return "KK   KK" 
    if(ln==2):
        return "KK KK  "
    if(ln==3):
        return "KKK    "
    if(ln==4):
        return "KK KK  "
    if(ln==5):
        return "KK   KK"

def L(ln):
    if(ln==1):
        return "LL     " 
    if(ln==2):
        return "LL     "
    if(ln==3):
        return "LL     "
    if(ln==4):
        return "LL     "
    if(ln==5):
        return "LLLLLLL"

def M(ln):
    if(ln==1):
        return "MM   MM" 
    if(ln==2):
        return "M M M M"
    if(ln==3):
        return "M  M  M"
    if(ln==4):
        return "M     M"
    if(ln==5):
        return "M     M"

def N(ln):
    if(ln==1):
        return "NN    N" 
    if(ln==2):
        return "N N   N"
    if(ln==3):
        return "N  N  N"
    if(ln==4):
        return "N   N N"
    if(ln==5):
        return "N    NN"

def O(ln):
    if(ln==1):
        return "  OOO  " 
    if(ln==2):
        return " O   O "
    if(ln==3):
        return "O     O"
    if(ln==4):
        return " O   O "
    if(ln==5):
        return "  OOO  "

def P(ln):
    if(ln==1):
        return "PPPPP  " 
    if(ln==2):
        return "P    PP"
    if(ln==3):
        return "PPPP   "
    if(ln==4):
        return "P      "
    if(ln==5):
        return "P      "

def Q(ln):
    if(ln==1):
        return "   Q   " 
    if(ln==2):
        return " Q   Q "
    if(ln==3):
        return "Q     Q"
    if(ln==4):
        return " Q Q Q "
    if(ln==5):
        return "   Q  Q"

def R(ln):
    if(ln==1):
        return "RRRRR  " 
    if(ln==2):
        return "R    R "
    if(ln==3):
        return "RRRR   "
    if(ln==4):
        return "R   R  "
    if(ln==5):
        return "R     R"


def S(ln):
    if(ln==1):
        return "  SSSSS" 
    if(ln==2):
        return "SS     "
    if(ln==3):
        return "  SSS  "
    if(ln==4):
        return "     SS"
    if(ln==5):
        return "SSSSS  "


def T(ln):
    if(ln==1):
        return "TTTTTTT" 
    if(ln==2):
        return "   T   "
    if(ln==3):
        return "   T   "
    if(ln==4):
        return "   T   "
    if(ln==5):
        return "   T   "


def U(ln):
    if(ln==1):
        return "U     U" 
    if(ln==2):
        return "U     U"
    if(ln==3):
        return "U     U"
    if(ln==4):
        return " U   U "
    if(ln==5):
        return "  UUU  "


def V(ln):
    if(ln==1):
        return "V     V" 
    if(ln==2):
        return "V     V"
    if(ln==3):
        return " V   V "
    if(ln==4):
        return "  V V  "
    if(ln==5):
        return "   V   "


def W(ln):
    if(ln==1):
        return "W     W" 
    if(ln==2):
        return "W     W"
    if(ln==3):
        return "W  W  W"
    if(ln==4):
        return "WW   WW"
    if(ln==5):
        return "W     W"


def X(ln):
    if(ln==1):
        return "X     X" 
    if(ln==2):
        return " X   X "
    if(ln==3):
        return "   X   "
    if(ln==4):
        return " X   X "
    if(ln==5):
        return "X     X"


def Y(ln):
    if(ln==1):
        return "Y     Y" 
    if(ln==2):
        return " Y   Y "
    if(ln==3):
        return "   Y   "
    if(ln==4):
        return "   Y   "
    if(ln==5):
        return "   Y   "


def Z(ln):
    if(ln==1):
        return "ZZZZZZZ" 
    if(ln==2):
        return "     Z "
    if(ln==3):
        return "   Z   "
    if(ln==4):
        return " Z     "
    if(ln==5):
        return "ZZZZZZZ"




str = input("Enter your string: \n")

for j in range (1, 6):
    for i in str:
        if(i.upper()     == 'A'):
            print(A(j), end = '    ')
        if(i.upper() == 'B'):
            print(B(j), end = '    ')
        if(i.upper() == 'C'):
            print(C(j), end = '    ')
        if(i.upper() == 'D'):
            print(D(j), end = '    ')
        if(i.upper() == 'E'):
            print(E(j), end = '    ')
        if(i.upper() == 'F'):
            print(F(j), end = '    ')
        if(i.upper() == 'G'):
            print(G(j), end = '    ')
        if(i.upper() == 'H'):
            print(H(j), end = '    ')
        if(i.upper() == 'I'):
            print(I(j), end = '    ')
        if(i.upper() == 'J'):
            print(J(j), end = '    ')
        if(i.upper() == 'K'):
            print(K(j), end = '    ')
        if(i.upper() == 'L'):
            print(L(j), end = '    ')
        if(i.upper() == 'M'):
            print(M(j), end = '    ')
        if(i.upper() == 'N'):
            print(N(j), end = '    ')
        if(i.upper() == 'O'):
            print(O(j), end = '    ')
        if(i.upper() == 'P'):
            print(P(j), end = '    ')
        if(i.upper() == 'Q'):
            print(Q(j), end = '    ')
        if(i.upper() == 'R'):
            print(R(j), end = '    ')
        if(i.upper() == 'S'):
            print(S(j), end = '    ')
        if(i.upper() == 'T'):
            print(T(j), end = '    ')
        if(i.upper() == 'U'):
            print(U(j), end = '    ')
        if(i.upper() == 'V'):
            print(V(j), end = '    ')
        if(i.upper() == 'W'):
            print(W(j), end = '    ')
        if(i.upper() == 'X'):
            print(X(j), end = '    ')
        if(i.upper() == 'Y'):
            print(Y(j), end = '    ')
        if(i.upper() == 'Z'):
            print(Z(j), end = '    ')
        if(i == ' '):
            print("       ", end = '    ')
            
    print()
    
