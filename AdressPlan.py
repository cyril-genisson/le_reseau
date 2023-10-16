#!/usr/bin/python3
#
# Author: Cyril GENISSON
# Created: 16/10/2023
# Updated: 16/10/2023
#
# Nom du script: CalculMasque.py
# Description: Permet d'établir un plan d'adressage réseau en fonction
# de la classe d'adresses IP utilisée, du nombre de sous-réseaux et du
# nombre de postes dans le sous-réseau.
#

# Définition des différentes classes de réseau
IpClass={"A": [[0,0,0,1], [126,255,255,254]], \
        "B": [[128,0,0,1], [191,255,255,254]], \
        "C": [[192,0,0,1], [223,255,255,254]], \
        "D": [[224,0,0,0], [239,255,255,255]], \
        "E": [[240,0,0,0], [247,255,255,255]] \
       }


def ClassDefine(l):
    if Ip[0] >= IpClass["A"][0][0] and Ip[0] <= IpClass["A"][1][0]:
        return "A"
    elif Ip[0] >= IpClass["B"][0][0] and Ip[0] <= IpClass["B"][1][0]:
        return "B"
    elif Ip[0] >= IpClass["C"][0][0] and Ip[0] <= IpClass["C"][1][0]:
        return "C"
    elif Ip[0] >= IpClass["D"][0][0] and Ip[0] <= IpClass["D"][1][0]:
        return "D"
    elif Ip[0] >= IpClass["E"][0][0] and Ip[0] <= IpCLass["E"][1][0]:
        return "E"
    else:
        print("L'adresse réseau IPv4 n'est pas correcte")
        exit(1)


def IpToBin(ip):
    # Retourne l'adresse IP [x,x,x,x] sous la forme d'une liste de 32 éléments
    l, x = [], ""
    for i in range(len(ip)):
        x += str(bin(ip[i])[2:].zfill(8))
    print(x)    
    for i in range(len(x)):
        l.append(int(x[i]))
    return l


def ReservedAdress(ip):
    l=[]
    for k in range(2):
        l.append(ip)
    print(l)
    l[0][3], l[1][3] = 0, 255
    return l[0],l[1]


def MaskNetwork(network):
    # la fonction MaskNetwork prend le nombre d'hôtes du sous-réseau pour calculer le masque nécessaire
    # au format CIDR (Classless Inter Domain Routing)
    return(32 - len(bin(network)[2:]))


# Classe d'IP attribuées
Ip = [10,0,0,0]
Networks=[(1, 12), (5, 30), (5, 120), (5, 160)]

print(MaskNetwork(120))
