"""
Projet: PRJ-SM601 - Théorie des Graphes - 2023/2024 - Thème sur l'Ordonnancement
Auteur: KOCOGLU Lucas
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

from filemanager.D_3_filemanager import files_list
from filemanager.D_3_filemanager import read_file
from fonctions.D_3_graph_display import display_graph_matrix
from fonctions.D_3_graph_display import display_graph_relations
from fonctions.D_3_validators import ordonnancement_validator
from fonctions.D_3_ordonnancement import ordonnencement_graph


# Fonctions
def welcome():
    """
     * Fonction: welcome
     * -----------------
     * Fonction permettant d'afficher un message de bienvenue coloré.
    ²²²"""
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
     * Fonction: menu_principal
     * -----------------
     * Fonction permettant d'afficher le menu principal.
     * Tant que l’utilisateur décide de tester un tableau de contraintes faire
     * Choix possibles :
     * 1. Lire un tableau de contraintes sur fichier
     * 2. Quitter le programme
    """
    # Boucle principale
    while True:
        print("---------------------- Menu Principal ----------------------"
              "\n1.\tLire un tableau de contraintes sur fichier"
              "\n2.\tQuitter le programme"
              "\n----------------------------------------------------------")
        try:
            # Demande de choix
            choix = int(input(colored("Entrez votre choix : ", "magenta")))
            match choix:
                case 1:
                    menu_graphe()
                case 2:
                    return True
                case _:
                    print(colored("Le choix n'a pas été reconnue.", "red"))
        except ValueError:
            print(colored("Veuillez entrer un nombre entier valide.", "red"))
        except Exception as e:
            print(colored("Une erreur est survenue : " + str(e), "red"))


def menu_graphe(choix=0):
    """
     * Fonction: menu_graphe
     * -----------------
     * Fonction permettant d'afficher le menu de traitement des graphes.
     * Un menu s'affiche permettant de choisir parmi une liste de fichiers de test dans le dossier testfiles.
     * L'utilisateur peut choisir un fichier de test pour le traiter, ou sortir du menu avec le choix 0.
     * Après le choix d'un fichier, le programme appelle les fonctions pour lire le graphes sous différents affichages.
     * Et vérifie si le graphe est un graphe d'ordonnancement.
     * Si c'est le cas, le programme propose de continuer le traitement du graphe d'ordonnancement.
     * Sinon, le programme propose de retourner au menu de choix de tableau.
    """
    # Récupération dans la première variable le text d'affichage, dans la seconde variable un dictionnaire avec comme
    # clé l'index et comme valeur le chemin du fichier
    string_test_files, index_test_files = files_list()

    if index_test_files is not None:
        print("---------------------- Menu Graphe ----------------------"
              + string_test_files +
              "----------------------------------------------------------")
        while True:
            try:
                # Demande de choix
                choix = int(input(colored("Entrez le numéro du fichier à traiter : ", "magenta")))

                # Sortie du menu
                if index_test_files[choix] == "Retour au menu principal":
                    break
                # Traitement du fichier
                elif choix in index_test_files.keys():
                    # Lecture du fichier, avec en première variable un dictionnaire contenant le graph, et en seconde
                    # variable une matrice de valeurs
                    graph_dict, graph_matrix = read_file(index_test_files[choix])

                    # Affichage des relations du graphe
                    print("----------------------------------------------------------")
                    display_graph_relations(graph_dict)
                    input(colored("Appuyez sur une touche pour continuer...", "magenta"))

                    # Affichage de la matrice de valeurs
                    print("----------------------------------------------------------")
                    print("* " + colored("Matrice de valeurs :", attrs=["bold", "underline"]))
                    display_graph_matrix(graph_matrix)
                    input(colored("Appuyez sur une touche pour continuer...", "magenta"))

                    # Vérification des propriétés du graphe d'ordonnancement
                    validator, adjacency_matrix = ordonnancement_validator(graph_matrix, graph_dict)
                    print("----------------------------------------------------------")
                    # Si validation OK, c'est un graphe d'ordonnancement
                    if validator:
                        # Demande de confirmation pour continuer le graph d'ordonnancement
                        confirm = None
                        while confirm not in ['y', 'n']:
                            confirm = input(colored("Souhaitez-vous continuer ? (y/n)... ", "magenta"))
                            match confirm:
                                case 'y':
                                    ordonnencement_graph(adjacency_matrix, graph_matrix)
                                    print("---------------------- Menu Graphe ----------------------"
                                          + string_test_files +
                                          "----------------------------------------------------------")
                                    break
                                case 'n':
                                    print(
                                        colored("Retour au choix de tableau...", "magenta"))
                                    print("---------------------- Menu Graphe ----------------------"
                                          + string_test_files +
                                          "----------------------------------------------------------")
                                    break
                                case _:
                                    print(colored("Le choix n'a pas été reconnue.", "red"))

                    # Si validation pas OK, retour au menu de choix de tableau
                    else:
                        input(colored("Appuyez sur une touche pour continuer (retour au choix de tableau)...", "magenta"))
                        print("---------------------- Menu Graphe ----------------------"
                              + string_test_files +
                              "----------------------------------------------------------")
                # Choix non reconnu
                else:
                    print(colored("Le choix n'a pas été reconnue.", "red"))
            except ValueError:
                print(colored("Veuillez entrer un nombre entier valide.", "red"))
            except Exception as e:
                print(colored("Une erreur est survenue : " + str(e), "red"))
    else:
        print(string_test_files)


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
        print(colored("Une erreur est survenue : " + str(e), "red"))
        exit(1)
