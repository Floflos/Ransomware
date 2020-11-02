
#coding:utf-8
import os
import sys
import http.server
import secrets
 
def main(argv,argc):
	cle = secrets.token_hex(32)
	print (cle)
	fichier = open("cle.txt", "w")
	fichier.write("key :"+cle)
	fichier.close()

	PORT = 8080
	address = ("", PORT)

	server = http.server.HTTPServer

	handler = http.server.CGIHTTPRequestHandler

	handler.cgi_directories = ["./"]

	httpd = server(address, handler)
	print("Serveur actif sur le port :", PORT)
	print("Pour les conditions du tp, laissez le serveur ouvert pendant toute l'operation (chiffrement et dechiffrement)")
	print("En effet, une clé aleatoire est generée à chaque fois")

	httpd.serve_forever()


#Appel de la fonction main et prise en compte des arguments
if __name__ == "__main__" :
	try:
		main(sys.argv, len(sys.argv))
	except KeyboardInterrupt:
		os.system("shred -vzu cle.txt >/dev/null 2>&1")
		sys.exit()

