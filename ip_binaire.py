#!/usr/bin/python3
#
# Author: Cyril GENISSON
# Created: 16/10/2023
# Updated: 16/10/2023
#
# Nom du script: ip_binaire.py
# Description: converti les adresses IP du Job14 en format binaire
#

ip_list = ["145.32.59.24", "200.42.129.16", "14.82.19.54"]

for i in range(len(ip_list)):
    chaine, ip_binary = "", ""
    for j in range(len(ip_list[i])):
        if ip_list[i][j] != "." :
            chaine += str(ip_list[i][j])
        else:
            ip_binary +=str(bin(int(chaine))[2:].zfill(8))
            chaine = ""
    ip_binary +=str(bin(int(chaine))[2:].zfill(8))
    print(ip_list[i], ": ",ip_binary)
