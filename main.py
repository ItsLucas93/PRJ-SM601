"""
Projet: PRJ-SM601 - Théorie des Graphes - 2023/2024 - Thème sur l'Ordonnancement
Auteurs: BAUDET Antoine, SABBEH Chokri, HOUEE Adrien, KOCOGLU Lucas
Description: Ce fichier est le fichier principal du projet, il permet de lancer les exécutions de fonction depuis les autres fichiers python.
Version de Python : 3.12
"""

from termcolor import colored

print(colored("\n\\\\\\ Bienvenue dans le Projet "
                "\n\t\t░█████╗░██████╗░██████╗░░█████╗░███╗░░██╗███╗░░██╗░█████╗░███╗░░██╗░█████╗░███████╗███╗░░░███╗███████╗███╗░░██╗████████╗"
                "\n\t\t██╔══██╗██╔══██╗██╔══██╗██╔══██╗████╗░██║████╗░██║██╔══██╗████╗░██║██╔══██╗██╔════╝████╗░████║██╔════╝████╗░██║╚══██╔══╝"
                "\n\t\t██║░░██║██████╔╝██║░░██║██║░░██║██╔██╗██║██╔██╗██║███████║██╔██╗██║██║░░╚═╝█████╗░░██╔████╔██║█████╗░░██╔██╗██║░░░██║░░░"
                "\n\t\t██║░░██║██╔══██╗██║░░██║██║░░██║██║╚████║██║╚████║██╔══██║██║╚████║██║░░██╗██╔══╝░░██║╚██╔╝██║██╔══╝░░██║╚████║░░░██║░░░"
                "\n\t\t╚█████╔╝██║░░██║██████╔╝╚█████╔╝██║░╚███║██║░╚███║██║░░██║██║░╚███║╚█████╔╝███████╗██║░╚═╝░██║███████╗██║░╚███║░░░██║░░░"
                "\n\t\t░╚════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚══╝╚═╝░░╚══╝╚═╝░░╚═╝╚═╝░░╚══╝░╚════╝░╚══════╝╚═╝░░░░░╚═╝╚══════╝╚═╝░░╚══╝░░░╚═╝░░░"
                "\n\t\t(Groupe D-3 | BAUDET Antoine, SABBEH Chokri, HOUEE Adrien, KOCOGLU Lucas)", "green"))

while True:
    try:
        pass
    except Exception as e:
        print(colored(f"\nUne erreur est survenue : {e}", "red"))


