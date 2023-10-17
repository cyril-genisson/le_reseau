#!/usr/bin/python3
#
# Author: Cyril GENISSON
# Created: 16/10/2023
# Updated: 17/10/2023
#
# Nom du script: CalculMasque.py
# Description: Permet d'établir un plan d'adressage réseau en fonction
# de la classe d'adresses IP utilisée, du nombre de sous-réseaux et du
# nombre de postes dans le sous-réseau.
#
#  \* WARNING */    Le travail est encore imcomplet pour avoir un plan d'adressage optimisé     \* WARNING */

############################################################
#
# Les éléments à adapter pour le pour l'adressage
#
############################################################
# Classe d'IP attribuées
Ip = "10.0.0.0"
# Liste de sous-réseaux (Nombre_reseau, Nombre_IP) pour le plan d'adressage
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
    if int(l[0]) >= IpClass["A"][0][0] and int(l[0]) <= IpClass["A"][1][0]:
        return "A"
    elif int(l[0]) >= IpClass["B"][0][0] and int(l[0]) <= IpClass["B"][1][0]:
        return "B"
    elif int(l[0]) >= IpClass["C"][0][0] and int(l[0]) <= IpClass["C"][1][0]:
        return "C"
    elif int(l[0]) >= IpClass["D"][0][0] and int(l[0]) <= IpClass["D"][1][0]:
        return "D"
    elif int[l(0)] >= IpClass["E"][0][0] and int(l[0]) <= IpCLass["E"][1][0]:
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

def findcidr(nbhosts):
    # Détermine le masque réseau au format cidr pour le nombre d'hôtes souhaité sur le sous-réseau (Fonction ok)
    k = 0
    while nbhosts > NbHosts[k][1]:
        k += 1
    return NbHosts[k][0]


def NbLan(IpClass, cidr):
    # Permet de déterminer le nombre de sous-réseaux disponibles
    # en fonction du mask et de la classe de réseau
     bitClass={"A": 8, "B": 16, "C": 24, "D": 32}
     return 2**(cidr -bitClass[IpClass])


def cidr2mask(cidr):
    # Converti le format CIDR du masque en masque xxx.xxx.xxx.xxx
    chaine = ""
    for k in range(1, cidr + 1):
        if k % 8 == 0:
            chaine += "1" + "."
        else:
            chaine += "1"
    for k in range(cidr + 1, 32):
        if k % 8 == 0:
            chaine += "0" + "."
        else:
            chaine += "0"
    chaine += "0"
    return bin2ip(chaine)

# Calcul la somme de 2 nombres binaires
binary_sum = lambda x,y : bin(int(a, 2) + int(b, 2))


# Bon là je en me foule pas trop... Je finirai plus tard pour optimiser l'adressage
# Très très bof mais fonctionnel.
def PrintNetwork(network):
    sumL, sumH, ip = 0, 0, Ip.split(".")
    for k in range(len(network)):
        sumL += network[k][0]
        sumH += network[k][1]

    print("/******************************************************\\")
    print("\t\t\tPlan d'adressage")
    print("\******************************************************/")

    print(f"Attribution d'une adresse de classe {ClassDefine(ip)}: {Ip}")
    print(f"Création de {sumL} sous-réseau(x) pour {sumH} hôtes:")
    for i in range(len(network)):
        cidr = findcidr(network[i][1])
        mask = cidr2mask(cidr)
        ipLan = list(ip)
        print()
        print("****************************************************")
        print(f"\tCIDR: {cidr}\tNETMASK= {mask}")
        print(f"         Nombre d'hôtes utilisables {NbHosts[32-cidr][1]}")
        print("****************************************************")
        for j in range(network[i][0]):
            print(f"Réseau 10.0.{j}.0/{cidr}")
            print(f"\t Adresse de broadcast 10.0.{j}.{2**(32-cidr)-1}")
            print(f"\t Première adresse utilisable 10.0.{j}.1")
            print(f"\t Dernière adresse utilisable 10.0.{j}.{2**(32-cidr)-2}")

PrintNetwork(Networks)
