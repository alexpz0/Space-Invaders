"""
Antoine ROCHAS & Alexandre FERRY
27/11/23
Fichier contenant la classe File
"""

class Queue:
	"""
	Classe file qui permet de gérer une file
	"""

	def __init__(self, length):
		"""
		Constructeur de la classe file
		"""
		self.__file = []
		self.__length = length

	def is_empty(self):
		"""
		Permet de savoir si la file est vide
		"""
		return len(self.__file) == 0
	
	def is_full(self):
		"""
		Permet de savoir si la file est pleine
		"""
		return len(self.__file) == self.__length
	
	def queue(self, element):
		"""
		Permet d'ajouter un élément à la fin de la file
		"""
		if self.is_full():
			raise Exception("File is full")
		else:
			self.__file.append(element)
		
	def dequeue(self):
		"""
		Permet de retirer le premier élément de la file
		"""
		if self.is_empty():
			raise Exception("Queue is empty")
		else:
			return self.__file.pop(0)
		
	def get_first(self):
		"""
		Permet de récupérer le premier élément de la file
		"""
		if self.is_empty():
			raise Exception("Queue is empty")
		else:
			return self.__file[0]
		
	def __str__(self):
		"""
		Permet d'afficher la file
		"""
		return str(self.__file)
	
	def __len__(self):
		"""
		Permet de récupérer la taille de la file
		"""
		return len(self.__file)