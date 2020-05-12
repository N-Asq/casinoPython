#!/usr/bin/python3
#coding: utf-8

from random import randrange
from math import *

colors = ["rouge","noir"]
play_again = True
gains = 0

while play_again:
    flag = False
    while not flag:
        try:
            mise = float(input("Combien de $ voulez-vous miser ? "))
            if mise <= 0:
                raise ValueError
        except ValueError:
            print("Veuillez tapez un nombre supérieur à 0 svp.")
        else:
            mise = round(mise*100)/100
            gains = gains-mise 
            flag = True

    flag = False
    while not flag:
        try:
            pari = int(input("Choisissez un nombre entier entre 0 et 49 sur lequel placer votre mise : "))
            assert pari <= 49 and pari >= 0
        except ValueError:
            print("Ce n'est pas un entier.")
        except AssertionError:
            print("Ce n'est pas un entier entre 0 et 49.")
        else:
            pari_color = pari%2
            print("Vous avez misé ${mise:.2f}, sur le nombre {pari}, qui est un nombre {pari_color}.".format(mise=mise,pari=pari,pari_color=colors[pari_color]))
            flag = True

    tirage = randrange(50)
    tirage_color = tirage%2

    print("Résultat du tirage : {tirage} qui est un nombre {tirage_color}.".format(tirage=tirage,tirage_color=colors[tirage_color]))
    if pari == tirage:
        print("C'est gagné ! Vous remportez ${0:.2f}.".format(ceil(mise*4)))
        gains = gains + ceil(mise*4)
    elif pari_color == tirage_color:
        print("La couleur est juste, vous remportez ${0:.2f}.".format(ceil(mise*1.5)))
        gains = gains + ceil(mise*1.5)
    else:
        print("Perdu !")

    print("Vos gains : ${0:.2f}".format(gains))

    try:
        again_choix = input("Voulez-vous continuez à jouer ? [O/N] : ").upper()
        if again_choix not in ["Y","O","N"]:
            raise ValueError
    except ValueError:
        print("Réponse incomprise, fermeture du programme.")
        play_again = False
    else:
        if again_choix == "N":
            play_again = False