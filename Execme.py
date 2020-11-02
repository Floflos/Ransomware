import sys
import os
import getopt
import pyperclip
import json
import hashlib
import time
import random
from string import printable
from getpass import getpass
from Crypto.Cipher import AES







#debut du programme
def main(argv,argc): 
    try:
        opts, args = getopt.getopt(argv[1:],'p',[]) #Si pas d'options, on chiffre
        print("Chiffrement des données en cours")
    except getopt.GetoptError:
        print("option invalide")
        sys.exit()
    for opt,arg in opts: 
        if opt in ('-p'): # Si l'option est p, on considere que la victime a payé le ransomware et on dechiffre les fichier
            print("paiement du ransomware")
            sys.exit()


#Appel de la fonction main et prise en compte des arguments
if __name__ == "__main__" :
    main(sys.argv, len(sys.argv))