"""
Antoine ROCHAS & Alexandre FERRY
13/11/23
Fichier qui contient la classe pour les missiles du jeu, qu'ils soient tirés par les aliens ou le vaisseau.
"""

from .entity import Entity

class Missile(Entity):
    """
    Classe pour les missiles du jeu, qu'ils soient tirés par les aliens ou le vaisseau.
    """

    def __init__(self, x, y, id, origin):
        # L'id correspond à l'indice dans le dictionnaire des entités du controller et de la vue.
        self.__id = id
        height = 80
        width = 18
        self.__origin = origin
        super().__init__(x, y, height, width, "missile")

    def move(self, dx, dy):
        """
        Déplace le missile de dx et dy.
        Si le missile sort de l'écran, où s'il touche un enemie on le supprime. Cela est géré par le controller.
        """
        super().move(dx, dy)
        return True
    
    def getId(self):
        """
        Retourne l'id du missile.
        """
        return self.__id
    
    def getOrigin(self):
        """
        Retourne l'origine du missile. ("ship" ou "alien")
        """
        return self.__origin
    
    def decrementId(self):
        """
        Décrémente l'id du missile. Utile lors de la suppression d'un missile.
        """
        self.__id -= 1