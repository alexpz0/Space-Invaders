"""
Antoine ROCHAS & Alexandre FERRY
27/11/23
Fichier contenant la classe Liste
"""

class Liste:
    """
    Classe Liste qui permet de gérer une liste
    """

    def __init__(self, length):
        """
        Constructeur de la classe liste
        """
        self.__liste = []
        self.__length = length

    def is_empty(self):
        """
        Permet de savoir si la liste est vide
        """
        return len(self.__liste) == 0
    
    def is_full(self):
        """
        Permet de savoir si la liste est pleine
        """
        return len(self.__liste) == self.__length
    
    def add(self, element, index):
        """
        Permet d'ajouter un élément dans la liste
        """
        if self.is_full():
            raise Exception("List is full")
        else:
            self.__liste.insert(index, element)
        
    def remove(self, index):
        """
        Permet de retirer un élément de la liste
        """
        if self.is_empty():
            raise Exception("List is empty")
        else:
            return self.__liste.pop(index)
        
    def get(self, index):
        """
        Permet de récupérer un élément de la liste
        """
        if self.is_empty():
            raise Exception("List is empty")
        else:
            return self.__liste[index]
        
    def __len__(self):
        """
        Permet de récupérer la taille de la liste
        """
        return len(self.__liste)
        
    def __str__(self):
        """
        Permet d'afficher la liste
        """
        return str(self.__liste)