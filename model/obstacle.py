"""
Antoine ROCHAS & Alexandre FERRY
20/11/23
Fichier qui contient la classe pour les obstacles du jeu.
"""

from .entity import Entity

class Obstacle(Entity):
    """
    Classe pour les obstacles du jeu.
    """

    def __init__(self, x, y, id):
        self.__id = id
        width = 90
        height = 90
        self.__life = 3
        super().__init__(x, y, height, width, "obstacle")

    def move(self, dx, dy):
        """
        On ne bouge pas les obstacles. Donc on ne fait rien.
        """
        pass

    def hit(self):
        """
        Décrémente la vie de l'obstacle. Retourne True si l'obstacle est détruit.
        """
        self.__life -= 1
        return self.__life == 0
    
    def getId(self):
        """
        Retourne l'id de l'obstacle.
        """
        return self.__id
    
    def decrementId(self):
        """
        Décrémente l'id de l'obstacle. Utile lors de la suppression d'un obstacle.
        """
        self.__id -= 1
    
    
    





