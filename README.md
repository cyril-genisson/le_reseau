# Le réseau

## Job 1: Installation de Cisco Packet Tracer
- Inscription sur la page: [skillsforall.com](https://skillsforall.com/)
- Démarrage du cours: [Notions de base sur les réseaux](https://skillsforall.com/course/networking-basics?courseLang=fr-FR)
- Téléchargement de Packet Tracer: [Packet Tracer 8.2.1](https://skillsforall.com/resources/lab-downloads?courseLang=fr-FR)

![Installation de Packet Tracer](./pictures/Job1.jpg "Cisco Packet Tracer")

## Job 2
- Qu'est-ce qu'un réseau?
Un réseau peut être associé à la notion de graphe dans le monde mathématiques

- A quoi sert un réseau informatique?
L'utilité d'un réseau informatique est de pouvoir connecter différents éléments du 

- Quel matériel avons-nous besoin pour construire un réseau?
Si l'on reste très flou sur la technologie employée pour communiquer 

## Job 3
Les ordinateurs de Pierre et Alice sont directement connectés entre eux sans passé par des composants
réseaux actifs comme un switch ou un routeur. Le cable choisit doit donc être croisée pour que la
communication puissse s'effectuée entre les deux machines. La connexion réseau est "Fast Ethernet"
c'est-à-dire qu'elle est asynchrone et bi-directionnelle ce qui permet d'avoir une vitesse de transmission
de 100Mb/s au lieu des 10Mb/s en "Ethernet".

## Job 4
- Qu'est-ce qu'une adresse IP?

- A quoi sert un IP?

- Qu'est-ce qu'une adresse MAC?

- Qu'est-ce qu'une IP publique et privé?

![Screenshoot Job4](./pictures/Job4.jpg "Pair à Pair")

## Job 5

![Screeshoot Job5 Pierre](./pictures/Job5_Pierre.jpg "IP PC Pierre")
![Screeshoot Job5 Alicia](./pictures/Job5_Pierre.jpg "IP PC Alicia")

- Quelle ligne de commande avez-vous utilisée pour vérifier l'id des machines?
```bash
# Commande permettant d'avoir les informations réseaux
ipconfig /all
```

## Job 6

![Ping](./pictures/Job6_Ping.jpg "Ping des PC Pierre et Alicia")

- Quelle est la commande permettant de Ping entre les PC?
```bash
# Commande employée sur l'ordinateur de Pierre
ping 192.168.1.2

# Commande employée sur l'ordinateur d'Alicia
ping 192.168.1.1
```

## Job 7

![Ping sur PC Pierre éteint](./pictures/Job7.jpg "PC Pierre éteint Ping")

- Le PC de Pierre a-t-il reçu les paquets envoyés par Alicia?
- Expliquez pourquoi.

Le PC de Pierre n'a pas pu recevoir les paquets icmp émis par Alicia, puisque son
ordinateur est éteint et que sa carte réseau ne traite plus les paquets envoyés par le cable réseau.

## Job 8

- Quelle est la différence entre un hub et un switch?

- Comment fonctionne un hub et quels sont ses avantages et ses inconvénients?

- Quels sont les avantages et inconvénients d'un switch?

- Comment un switch gère-t'il le réseau?

## Job 9

- Faire un schéma de votre réseau
(Doit représenter la topologie et la configuration du réseau en incluant les composants)


- Identifier au moins trois avantages importants d'avoir un schéma

## Job 10

- Quelle est la différence entre une adresse IP statique et une adresse IP attribuée par DHCP?

## Job 11
Attribution d'une adresse de classe A 10.0.0.0
Création de 21 sous-réseau:
- 1 sous-réseau de 12 hôtes     10.0.0./
- 5 sous-réseaux de 30 hôtes    10.0.0./
- 5 sous-réseaux de 120 hôtes   10.0.0./
- 5 sous-réseaux de 160 hôtes   10.0.0./

Pour générer l'ensemble du plan d'adressage nous avons évalué au plus juste les besoins de chaque
sous-réseaux. Donc il est possible que l'on ne puisse pas ajouter un nouvel hôte sur certain
de ces sous-réseaux. Le calcul est effectué de tel manière que l'on essaye d'économiser au
maximum les adresses IPs en ne prévoyant pas des sous-réseaux avec une grande perte d'adresses IPs
non utilisées.

Ci-dessous le code Python ayant servit à définir notre plan d'adressage automatiquement pour l'ensemble
des sous-réseaux:
```Python

```


### Définissons le plan d'adressage

- Pourquoi a-t-on choisi une adresse 10.0.0.0 de classe A

- Quelle est la différence entre les différents types d'adresses?

## Job 12
Tableau des sept couches du modèle OSI (description des rôles de chaque couche)

|   Couche   |   Nom |   Rôle |
|:--:    |:-:    |---    |
|   7   |   Application   | Service applicatif au plus proche des utilisateurs  |
|   6   |   Présentation  | Encode, chiffre et compresse les données utiles |
|   5   |   Session   |   Etablit des sessions entre les applications   |
|   4   |   Transport   |   Etablit, maintient et termine des sessions entre des périphériques terminaux |
|   3   |   Réseau  |   Adresse les interfaces globalement et détermine les meilleurs chemins à travers un inter-réseau |
|   2   |   Liaison de données  |   Adresse localement les interfaces, livre les informations localement, méthode MAC   |
|   1   |   Physique    |   Encodage du signal, câblage et connecteurs, spécifications physiques    |

Associez les différentes matériels ou protocoles aux couches
| Matériel / Protocole  |   Couche  |
|:--:    |:--:    |
|   Ethernet    |   1   |
|   TCP |   5   |
|   MAC |   2   |
|   Fibre optique   |   1   |
|   PPTP    |   5   |
|   IPv4    |   3|
|   SSL/TLS |   6   |
|   TCP |   5   |
|   WIFI    |   1   |
|   IPv6    |   3   |
|   UDP |   4   |
|   FTP |   5   |
|   routeur |   3   |
|   HTML    |   6   |
|   Cable RJ45  |   1   |

## JOB 13

- Quell est l'architecture de ce réseau?

- Indiquer quelle est l'adresse IP du réseau?
192.168.10.0/24

- Quelle est l'adresse de diffusion de ce réseau?
192.168.10.255

## JOB 14
Conversion des adresses IP en binaire
Pour ne pas trop s'embéter à tout faire à la main on peut écrire un petit script convertissant
l'adresse IP en binaire:
```python
  1 #!/usr/bin/python3
  2 #
  3 # Author: Cyril GENISSON
  4 # Created: 16/10/2023
  5 # Updated: 16/10/2023
  6 #
  7 # Nom du script: ip_binaire.py
  8 # Description: converti les adresses IP du Job14 en format binaire
  9 # Il y a sûrement plus simple à faire mais bon...
 10
 11 ip_list = ["145.32.59.24", "200.42.129.16", "14.82.19.54"]
 12
 13 for i in range(len(ip_list)):
 14     chaine, ip_binary = "", ""
 15     for j in range(len(ip_list[i])):
 16         if ip_list[i][j] != "." :
 17             chaine += str(ip_list[i][j])
 18         else:
 19             ip_binary +=str(bin(int(chaine))[2:].zfill(8))                                                                        20             chaine = ""
 21     ip_binary +=str(bin(int(chaine))[2:].zfill(8))
 22     print(ip_list[i], ": ",ip_binary)
```

- 192.168.0.1              11000000 10101000 00000000 00000001
- 145.32.59.24             10010001 00100000 00111011 00011000
- 200.42.129.16            11001000 00101010 10000001 00010000
- 14.82.19.54              00001110 01010010 00010011 00110110

**Remarque:** On n'aurait pu se servir d'une partie du code du Job11 mais nous n'avions
rien de mieux à faire que de réinventer la roue...

## JOB 15

- Qu'est-ce que le routage?

- Qu'est-ce qu'un qateway?

- Qu'est-ce qu'un VPN?
Virtual Private Network
- Qu'est-ce qu'un DNS?
Domain Name Service
