import os
from termcolor import colored

def files_list(path = "testfilses"):
    """
    Lire et renvoie la liste des fichiers de test disponibles dans le dossier de testfiles.
    """
    index_test_files = {}
    try:
        files = os.listdir(path)
        if len(files) == 0:
            return colored("Aucun fichier n'a été trouvé dans le dossier de " + colored(str(path), attrs=["bold", "underline"]), "red"), None
        for i in files:
            if i.split('.')[-1] != 'txt':
                files.remove(i)
        files.sort(key=lambda str: int(str.split()[1].split('.')[0])) # ['table', 'x', '.txt']
        string = "\nFichiers disponibles dans le dossier : " + colored(str(path), attrs=["underline"]) + "\n"
        for i, file in enumerate(files):
            index_test_files[i + 1] = file
            string += str(i + 1) + ".\t" + file + "\n"
        index_test_files[len(index_test_files) + 1] = "Retour au menu principal"
        return string, index_test_files
    except FileNotFoundError:
        return colored("Le dossier de ", "red") + colored(str(path), "red", attrs=["bold", "underline"]) + colored(" n'a pas été trouvé.", "red"), None
    except Exception as e:
        return colored("Une erreur est survenue : " + str(e), "red"), None