"""
Antoine ROCHAS & Alexandre FERRY
13/11/23
Fichier qui contient la classe de base pour les entités du jeu.
"""


class Entity:
    """
    Classe de base pour les entités du jeu.
    Cette classe est vouée à être héritée.
    """

    screen_width = 0
    screen_height = 0

    def __init__(self, x, y, height, width, type):
        self.__x = x
        self.__y = y
        self.__type = type
        self.__height = height
        self.__width = width
    
    def getHitBox(self):
        """
        Retourne un tuple contenant les coordonnées de la hitbox de l'entité.
        """
        return (self.__x-self.__width/2, self.__y-self.__height/2, self.__x + self.__width/2, self.__y + self.__height/2)
    
    def isColliding(self, entity):  
        """
        Retourne True si l'entité est en collision avec l'entité passée en paramètre.
        """
        return self.getHitBox()[0] < entity.getHitBox()[2] and self.getHitBox()[2] > entity.getHitBox()[0] and self.getHitBox()[1] < entity.getHitBox()[3] and self.getHitBox()[3] > entity.getHitBox()[1]
            
    def getType(self):
        """
        Retourne le type de l'entité.
        """
        return self.__type
    
    def getCoords(self):
        """
        Retourne un tuple contenant les coordonnées de l'entité.
        """
        return (self.__x, self.__y)
    
    def move(self, dx, dy):
        """
        Déplace l'entité de dx et dy.
        """
        self.__x += dx
        self.__y += dy

    def isOutOfScreen(self):
        """
        Retourne True si l'entité est en dehors de l'écran.
        """
        return self.__x - self.__width/2 < 0 or self.__x + self.__width/2 > Entity.screen_width or self.__y - self.__height/2 < 0 or self.__y + self.__height/2 > Entity.screen_height
    
    @staticmethod
    def setScreenHeight(height):
        """
        Définit la hauteur de l'écran. (Méthode statique)
        """
        Entity.screen_height = height
    
    @staticmethod
    def setScreenWidth(width):
        """
        Définit la largeur de l'écran. (Méthode statique)
        """
        Entity.screen_width = width

        