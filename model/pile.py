"""
Antoine ROCHAS & Alexandre FERRY
27/11/23
Fichier contenant la classe Stack
"""

class Stack:
    """
    Classe stack qui permet de gérer une pile
    """

    def __init__(self, length):
        """
        Constructeur de la classe pile
        """
        self.__stack = []
        self.__length = length

    def is_empty(self):
        """
        Permet de savoir si la pile est vide
        """
        return len(self.__stack) == 0
    
    def is_full(self):
        """
        Permet de savoir si la pile est pleine
        """
        return len(self.__stack) == self.__length
    
    def stack(self, element):
        """
        Permet d'ajouter un élément dans la pile
        """
        if self.is_full():
            raise Exception("Stack is full")
        else:
            self.__stack.append(element)
        
    def unstack(self):
        """
        Permet de retirer un élément de la pile
        """
        if self.is_empty():
            raise Exception("Stack is empty")
        else:
            return self.__stack.pop()
        
    def get_last(self):
        """
        Permet de récupérer le dernier élément de la pile
        """
        if self.is_empty():
            raise Exception("Stack is empty")
        else:
            return self.__stack[-1]
        
    def __str__(self):
        """
        Permet d'afficher la pile
        """
        return str(self.__stack)
    
    def __len__(self):
        """
        Permet de récupérer la taille de la pile
        """
        return len(self.__stack)