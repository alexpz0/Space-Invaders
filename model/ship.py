"""
Antoine ROCHAS & Alexandre FERRY
13/11/23
Fichier qui contient la classe pour le vaisseau du jeu.
"""

from .entity import Entity

class Ship(Entity):
    """
    Classe pour le vaisseau du jeu.
    """

    def __init__(self, x, y):
        height, width = 70, 70
        self.__life = 3
        super().__init__(x, y, height, width,"ship")

    def move(self, dx, dy):
        """
        Déplace le vaisseau de dx et dy.
        Si le vaisseau sort de l'écran, on le replace à la limite de l'écran.
        """
        super().move(dx, dy)
        if self.isOutOfScreen():
            self.move(-dx, -dy)
            return False
        return True
    
    def hit(self):
        """
        Décrémente la vie du vaisseau. Retourne True si le vaisseau est détruit.
        """
        self.__life -= 1
        return self.__life == 0
    
    def getLife(self):
        """
        Retourne la vie du vaisseau.
        """
        return self.__life
    
