Projet de simple Ransomware python:

En premier lieu, installer les dependances et librairies avec "pip install -r requirements.txt"

Pour tester le projet, ouvrir 3 terminaux: deux dans le fichier courant du projet et un dans tmp.

Ouvrir le serveur avec "python3 serveur.py" 

ATTENTION, ne pas fermer le serveur si vos fichiers sont chiffrés car la clé est aleatoire et est supprimée lors de la fermeture du serveur.

Dans le second terminal, tester le ransomware avec "python3 Execme.py"
Dans votre terminal dans tmp, vous devriez remarquer que tous les fichiers du repertoire et sous repertoires sont chiffrés avec l'extension .enc

Pour dechiffrer, faire la commande "python3 Execme.py -p"

Dans votre terminal dans tmp, vous devriez constater que tous les fichiers sont revenus à la normale