"""
Projet: PRJ-SM601 - Théorie des Graphes - 2023/2024 - Thème sur l'Ordonnancement
Auteurs: BAUDET Antoine, SABBEH Chokri, HOUEE Adrien, KOCOGLU Lucas
Description: Ce fichier est le fichier principal du projet, il permet de lancer les exécutions de fonction depuis les autres fichiers python.
Version de Python : 3.12
"""

"""
Rappel de la structure du Pseudo-code :
Début
    Tant que l’utilisateur décide de tester un tableau de contraintes faire
    Choisir le tableau de contraintes à traiter

    Lire le tableau de contraintes sur fichier et le stocker en mémoire

    Créer la matrice correspondant au graphe représentant ce tableau de contraintes et l’afficher

    Vérifier que les propriétés nécessaires pour que ce graphe soit un graphe d’ordonnancement sont vérifiées

         SI oui alors
               Calculer les rangs des sommets et les afficher
               Calculer les calendriers au plus tôt et au plus tard et les afficher
               Calculer les marges et les afficher
               Calculer le(s) chemin(s) critique(s) et
               les afficher
         Sinon
               Proposer à l’utilisateur de changer de tableau de contraintes
    fin Tant que
FIn
"""

from termcolor import colored


# Fonctions
def welcome():
    """
    Fonction permettant d'afficher un message de bienvenue coloré.
    """
    print(colored("\n\\\\\\ Bienvenue dans le Projet "
                  "\n\t\t░█████╗░██████╗░██████╗░░█████╗░███╗░░██╗███╗░░██╗░█████╗░███╗░░██╗░█████╗░███████╗███╗░░░███╗███████╗███╗░░██╗████████╗"
                  "\n\t\t██╔══██╗██╔══██╗██╔══██╗██╔══██╗████╗░██║████╗░██║██╔══██╗████╗░██║██╔══██╗██╔════╝████╗░████║██╔════╝████╗░██║╚══██╔══╝"
                  "\n\t\t██║░░██║██████╔╝██║░░██║██║░░██║██╔██╗██║██╔██╗██║███████║██╔██╗██║██║░░╚═╝█████╗░░██╔████╔██║█████╗░░██╔██╗██║░░░██║░░░"
                  "\n\t\t██║░░██║██╔══██╗██║░░██║██║░░██║██║╚████║██║╚████║██╔══██║██║╚████║██║░░██╗██╔══╝░░██║╚██╔╝██║██╔══╝░░██║╚████║░░░██║░░░"
                  "\n\t\t╚█████╔╝██║░░██║██████╔╝╚█████╔╝██║░╚███║██║░╚███║██║░░██║██║░╚███║╚█████╔╝███████╗██║░╚═╝░██║███████╗██║░╚███║░░░██║░░░"
                  "\n\t\t░╚════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚══╝╚═╝░░╚══╝╚═╝░░╚═╝╚═╝░░╚══╝░╚════╝░╚══════╝╚═╝░░░░░╚═╝╚══════╝╚═╝░░╚══╝░░░╚═╝░░░"
                  "\n\t\t(Groupe D-3 | BAUDET Antoine, SABBEH Chokri, HOUEE Adrien, KOCOGLU Lucas)", "green"))


def menu_principal(choix=0):
    """
    Fonction permettant d'afficher le menu principal.
    Tant que l’utilisateur décide de tester un tableau de contraintes faire
    Choisir le tableau de contraintes à traiter
    """

    while True:
        print("---------------------- Menu Principal ----------------------"
              "\n1.\tLire un tableau de contraintes sur fichier"
              "\n2.\tQuitter le programme"
              "\n----------------------------------------------------------")

        try:
            choix = int(input("Entrez votre choix : "))
            match choix:
                case 1:
                    pass
                case 2:
                    return True
                case _:
                    print(colored("Le choix n'a pas été reconnue.", "red"))
        except ValueError:
            print(colored("Veuillez entrer un nombre entier valide.", "red"))


# Programme principal
if __name__ == '__main__':
    try:
        welcome()
        if menu_principal():
            exit(0)
        exit(1)

    except KeyboardInterrupt:
        print(colored("\nLe programme a été interrompu par l'utilisateur.", "red"))
        exit(0)
    except Exception as e:
        print(colored(f"\nUne erreur s'est produite : {e}", "red"))
        exit(1)