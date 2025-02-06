"""
Antoine ROCHAS & Alexandre FERRY
13/11/23
Fichier qui contient la classe pour les aliens du jeu.
"""

from .entity import Entity

class Alien(Entity):
    """
    Classe pour les aliens du jeu.
    """

    def __init__(self, x, y, id):
        height = 41
        width = 58
        self.__id = id
        super().__init__(x, y, height, width, "alien")

    def move(self, dx, dy):
        """
        Déplace l'alien de dx et dy. 
        La logique de déplacement des aliens est gérée par le controller car ils se déplacent en groupe.
        """
        super().move(dx, dy)
        return True
    
    def getId(self):
        """
        Retourne l'id de l'alien.
        """
        return self.__id
    
    def decrementId(self):
        """
        Décrémente l'id de l'alien. Utile lors de la suppression d'un alien.
        """
        self.__id -= 1