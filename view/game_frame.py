"""
Antoine ROCHAS & Alexandre FERRY
Fichier contenant la classe GameFrame
13/11/23

Ce fichier contient la classe GameFrame qui permet de créer le widget principal du jeu, un canvas.
Fichier optimisé
"""

import tkinter as tk
from PIL import Image, ImageTk

from controller.db_controller import DBController

class GameFrame(tk.Canvas):
    """
    Classe permettant de créer le widget principal du jeu, le canvas qui contient les entités du jeu.
    """
    def __init__(self, master):
        super().__init__(master, width=700, height=700, highlightthickness=0, bg="white")
        self.__image_bg = ImageTk.PhotoImage(Image.open("assets/images/background.png"))
        self.create_image(0, 0, image=self.__image_bg, anchor=tk.NW)

        self.__entities = {
            "aliens": [],
            "ship": None,
            "ship_missile": None,
            "aliens_missiles": [],
            "obstacles": []
        }

        # Attribut contenant les images des aliens et des missiles pour les stocker en mémoire et éviter qu'elles ne soient supprimées par le garbage collector
        self.__alien_images = [] 
        self.__alien_missile_images = []
        self.__obstacle_images = []

        self.__db_controller = DBController()

        self.master.updatePersonalBest(self.__db_controller.get_personal_best())

    def placeEntity(self, entity):
        """
        Place une entité sur le canvas en fonction de son type.
        Pour chaque type, on crée une image et on la stocke dans un attribut pour éviter qu'elle ne soit supprimée par le garbage collector.
        On place ensuite l'image sur le canvas puis on l'ajoute dans le dictionnaire.
        """
        if entity.getType() == "alien":
            alien = ImageTk.PhotoImage(Image.open("assets/images/alien.png").resize((58, 41)))
            self.__alien_images.append(alien)
            image = self.create_image(entity.getCoords()[0], entity.getCoords()[1], image=self.__alien_images[len(self.__alien_images)-1], anchor=tk.CENTER)
            self.__entities["aliens"].append(image)

        elif entity.getType() == "ship":
            self.ship_image = ImageTk.PhotoImage(Image.open("assets/images/ship.png").resize((80, 80)))
            image = self.create_image(entity.getCoords()[0], entity.getCoords()[1], image=self.ship_image, anchor=tk.CENTER)
            self.__entities["ship"] = image

        elif entity.getType() == "missile":
            if entity.getOrigin() == "ship":
                self.missile_image = ImageTk.PhotoImage(Image.open("assets/images/missile.png").resize((18, 80)))
                image = self.create_image(entity.getCoords()[0], entity.getCoords()[1], image=self.missile_image, anchor=tk.CENTER)
                self.__entities["ship_missile"] = image

            else:
                alien_missile_image = ImageTk.PhotoImage(Image.open("assets/images/alien_missile.png").resize((18, 80)))
                self.__alien_missile_images.append(alien_missile_image)
                image = self.create_image(entity.getCoords()[0], entity.getCoords()[1], image=self.__alien_missile_images[len(self.__alien_missile_images)-1], anchor=tk.CENTER)
                self.__entities["aliens_missiles"].append(image)

        elif entity.getType() == "obstacle":
            obstacle_image = ImageTk.PhotoImage(Image.open("assets/images/obstacle.png").resize((100, 100)))
            self.__obstacle_images.append(obstacle_image)
            image = self.create_image(entity.getCoords()[0], entity.getCoords()[1], image=self.__obstacle_images[len(self.__obstacle_images)-1], anchor=tk.CENTER)
            self.__entities["obstacles"].append(image)

    def deleteEntity(self, entity):
        """
        Supprime une entité du canvas en fonction de son type.
        Pour chaque type, on supprime l'image du canvas puis on supprime du dictionnaire.
        """
        if entity.getType() == "alien":
            # On supprime l'image de l'alien du canvas
            self.delete(self.__entities["aliens"][entity.getId()])
            # On supprime l'image de l'alien du tableau
            del self.__entities["aliens"][entity.getId()]

        elif entity.getType() == "ship":
            self.delete(self.__entities["ship"])
            self.__entities["ship"] = None

        elif entity.getType() == "missile":
            if entity.getOrigin() == "ship":
                self.delete(self.__entities["ship_missile"])
                self.__entities["ship_missile"] = None
            else:
                self.delete(self.__entities["aliens_missiles"][entity.getId()])
                del self.__entities["aliens_missiles"][entity.getId()]

        elif entity.getType() == "obstacle":
            self.delete(self.__entities["obstacles"][entity.getId()])
            del self.__entities["obstacles"][entity.getId()]

    def moveEntity(self, entity, dx, dy):
        """
        Déplace une entité sur le canvas en fonction de son type.
        """
        if entity.getType() == "alien": 
            # entity.getId() correspond à l'indice de l'alien dans le tableau
            self.move(self.__entities["aliens"][entity.getId()], dx, dy)

        elif entity.getType() == "ship":
            self.move(self.__entities["ship"], dx, dy)

        elif entity.getType() == "missile":
            if entity.getOrigin() == "ship":
                self.move(self.__entities["ship_missile"], dx, dy)
            else:
                self.move(self.__entities["aliens_missiles"][entity.getId()], dx, dy) 

    def gameOver(self):
        """
        Affiche le message de fin de partie
        """
        self.create_text(350, 350, text="Game Over", font=("Calibri", 50), fill="red")
        self.master.newGameButton.config(state=tk.NORMAL)

    def win(self):
        """
        Affiche le message de victoire
        """
        self.create_text(350, 350, text="Victoire !", font=("Calibri", 50), fill="green")
        self.master.newGameButton.config(state=tk.NORMAL)
        self.__db_controller.add_score(self.master.getScore())
        self.master.updatePersonalBest(self.__db_controller.get_personal_best())

    def reset(self):
        """
        Réinitialise le canvas
        """
        self.__entities = {
            "aliens": [],
            "ship": None,
            "ship_missile": None,
            "aliens_missiles": [],
            "obstacles": []
        }
        self.delete("all")
        self.create_image(0, 0, image=self.__image_bg, anchor=tk.NW)
        self.master.updateScore(-self.master.getScore())
