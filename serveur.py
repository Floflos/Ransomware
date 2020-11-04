
#coding:utf-8
import os
import sys
import http.server
import secrets
 
def main(argv,argc):
	cle = secrets.token_hex(32) #clé générée aléatoirement 
	fichier = open("cle.txt", "w") #création et ouverture du fichier cle.txt
	fichier.write("key :"+cle) #on écrit la clé 
	fichier.close()

	PORT = 6666 #utilisation du port 6666
	address = ("", PORT)

	server = http.server.HTTPServer

	handler = http.server.CGIHTTPRequestHandler

	handler.cgi_directories = ["./"]

	httpd = server(address, handler) #lancement du serveur
	print("Serveur actif sur le port :", PORT)
	print("Pour les conditions du tp, laissez le serveur ouvert pendant toute l'operation (chiffrement et dechiffrement)\n Ne surtout pas fermer le serveur lorsque les fichiers sont chiffrés")
	print("En effet, une clé aleatoire est generée à chaque fois\n\n pour fermer le serveur, vous pouvez utiliser CTRL + C ")

	httpd.serve_forever()


#Appel de la fonction main et prise en compte des arguments
if __name__ == "__main__" :
	try:
		main(sys.argv, len(sys.argv))
	except KeyboardInterrupt:
		#supression du fichier de cle
		os.system("shred -vzu cle.txt >/dev/null 2>&1")
		sys.exit()

