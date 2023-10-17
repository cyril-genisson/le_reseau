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

############################################################
#
# Les éléments à adapter pour le pour l'adressage
#
############################################################
# Classe d'IP attribuées
Ip = "192.168.225.15"
# Liste de sous-réseau (Nombre_reseau, Nombre_IP) pour le plan d'adressage
Networks=[(1, 12), (5, 30), (5, 120), (5, 160)]

############################################################
#
# Définitions des classes IPs
#
############################################################

# Définition des différentes classes de réseau
IpClass={"A": [[0,0,0,1], [126,255,255,254]], \
        "B": [[128,0,0,1], [191,255,255,254]], \
        "C": [[192,0,0,1], [223,255,255,254]], \
        "D": [[224,0,0,0], [239,255,255,255]], \
        "E": [[240,0,0,0], [247,255,255,255]] \
       }

# Liste du nombre d'hôtes disponibles en fonction du mask de sous-réseau
NbHosts=[(32, 1), (31, 2)]
for k in range(2, 32):
    NbHosts.append((32-k, 2**k - 2))

############################################################
#
# Définitions des fonctions utiles pour le traitement
#
############################################################
def bin2int(octet):
    # Convertie un octet en entier (Fonction ok).
    integer = 0
    for k in range(len(octet)):
        if octet[k] == '1':
            integer += 2**(7-k)
    return integer


def int2bin(integer):
    # Convertie un entier en binaire (Fonction ok)
    return bin(integer)[2:].zfill(8)


def ClassDefine(l):
    # Retourne la classe de l'adresse IP (Fonction ok)
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


def ip2bin(ip):
    # Retourne l'adresse IP en une chaine binaire 00000000.00000000.00000000.00000000 (Fonction ok)
    ipL = ip.split(".")
    binary = ""
    for k in range(len(ipL) - 1):
        binary += int2bin(int(ipL[k])) + "."
    binary += int2bin(int(ipL[3]))
    return binary


def bin2ip(binary):
    # Retourne une IP binaire sous la fome d'une adresse IP décimale (Fonction ok)
    ipB = binary.split(".")
    ip = ""
    for i in range(len(ipB) - 1):
        ip += str(bin2int(ipB[i])) + "."
    ip += str(bin2int(ipB[3]))
    return ip


def mask2bin(cidr):
    binary=""
    for k in range(cidr)
        if k % 8:
            binary += "." + "1"
        else:
            binary += "1"
    
    return binary


def bin2mask(binary):
    return mask


def PrintNetwork(network):
    sumL, sumH = 0, 0
    for k in range(len(network)):
        sumL += network[k][0]
        sumH += network[k][1]
    print(f"Attribution d'une adresse de classe {ClassDefine(Ip)} {Ip[0]}.{Ip[1]}.{Ip[2]}.{Ip[3]}")
    print(f"Création de {sumL} sous-réseau(x) pour {sumH} hôtes:")
    for i in range(len(network)):
        for j in range(network[i][0]):
            netmask = MaskNetwork(network[i][1])
           # print(f"Réseau {}/{netmask}")
           # print(f"\t Adresse de broadcast {}"}
           # print(f"\t Première adresse utilisable {}")
           # print(f"\t Dernière adresse utilisable {}")
           # print(f"\t Nombre d'hôtes utilisables {}")
           # print(f"\t Nombre de sous-réseaux {}")
