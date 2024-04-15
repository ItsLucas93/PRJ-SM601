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

from filemanager.filemanager import files_list
from filemanager.filemanager import read_file
from fonctions.graph_display import display_graph_matrix
from fonctions.graph_display import display_graph_relations
from fonctions.validators import ordonnancement_validator


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
    Fonction permettant d'afficher le menu du graphe.
    """

    string_test_files, index_test_files = files_list()

    if index_test_files is not None:
        print("---------------------- Menu Graphe ----------------------"
              + string_test_files +
              "----------------------------------------------------------")
        while True:
            try:
                choix = int(input(colored("Entrez le numéro du fichier à traiter : ", "magenta")))
                if index_test_files[choix] == "Retour au menu principal":
                    break
                elif choix in index_test_files.keys():
                    # print(read_file(index_test_files[choix])[0])
                    graph_dict, graph_matrix = read_file(index_test_files[choix])
                    print("----------------------------------------------------------")
                    display_graph_relations(graph_dict)
                    input(colored("Appuyez sur une touche pour continuer...", "magenta"))
                    print("----------------------------------------------------------")
                    print("* " + colored("Matrice de valeurs :", attrs=["bold", "underline"]))
                    display_graph_matrix(graph_matrix)
                    input(colored("Appuyez sur une touche pour continuer...", "magenta"))
                    print("----------------------------------------------------------")
                    # Vérification des propriétés du graphe d'ordonnancement
                    validator = ordonnancement_validator(graph_matrix, graph_dict)
                    if validator:
                        confirm = None
                        while confirm not in ['y', 'n']:
                            confirm = input(colored("Souhaitez-vous continuer ? (y/n)... ", "magenta"))
                            match confirm:
                                case 'y':
                                    # TODO: Calculer les rangs des sommets et les afficher
                                    # TODO: Calculer les calendriers au plus tôt et au plus tard et les afficher
                                    # TODO: Calculer les marges et les afficher
                                    # TODO: Calculer le(s) chemin(s) critique(s) et les afficher
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
                    else:
                        input(colored("Appuyez sur une touche pour continuer (retour au choix de tableau)...", "magenta"))
                        print("---------------------- Menu Graphe ----------------------"
                              + string_test_files +
                              "----------------------------------------------------------")
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