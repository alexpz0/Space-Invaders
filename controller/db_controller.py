"""
Antoine ROCHAS & Alexandre FERRY
27/11/2023
Fichier contenant les fonctions de la base de données gérant les scores.
La base de donnée est un fichier .txt
"""

from datetime import datetime
import os

class DBController:
    """
    Classe permettant de gérer les scores.
    """

    def __init__(self):
        """
        Constructeur de la classe DBController.
        """
        self.__path = os.path.join(os.path.dirname(__file__), "../assets/scores.txt")
    
    def get_scores(self):
        """
        Fonction permettant de récupérer les scores.
        """
        scores = []
        with open(self.__path, "r") as file:
            for line in file:
                scores.append(line.split(":"))
        return scores
    
    def add_score(self, score):
        """
        Fonction permettant d'ajouter un score.
        """
        with open(self.__path, "a") as file:
            file.write(f"{score}:{datetime.now()}\n")

    def clear(self):
        """
        Fonction permettant de supprimer les scores.
        """
        with open(self.__path, "w") as file:
            file.write("")

    def get_personal_best(self):
        """
        Fonction permettant de récupérer le meilleur score personnel.
        """
        scores = self.get_scores()
        best = 0
        for score in scores:
            if int(score[0]) > best:
                best = int(score[0])
        return best