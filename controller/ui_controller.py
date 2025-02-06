"""
Antoine ROCHAS & Alexandre FERRY
Fichier contenant la classe GameFrame
20/11/23

Ce fichier contient la classe UIController qui permet de gérer les interactions entre la vue et le modèle.
Fichier à optimiser (moveMissiles)
"""

from random import randint

from model.entity import Entity
from model.alien import Alien
from model.ship import Ship
from model.missile import Missile
from model.obstacle import Obstacle

from model.liste import Liste
from model.pile import Stack
from model.file import Queue

class UIController:
    """
    Cette classe permet de gérer les interactions entre la vue et le modèle,
    elle est totalement indépendante de tkinter et peut être utilisée avec n'importe quelle autre bibliothèque
    à condition que l'utilisateur implémente les méthodes nécessaires dans la classe GameFrame
    """

    def __init__(self, game, screen_width, screen_height):
        # On définit la taille de l'écran pour les entités
        Entity.setScreenWidth(screen_width)
        Entity.setScreenHeight(screen_height)

        # Référence vers la vue
        self.__game = game
        self.__screen_width = screen_width
        self.__screen_height = screen_height

        # Dictionnaire contenant les entités du jeu
        self.__entities = {
            "aliens": [],
            "ship": None,
            "ship_missile": None,
            "aliens_missiles": [],
            "obstacles": []
        }

        # Variables de jeu
        self.__is_playing = False
        self.__alien_speed = 3
        self.__shoot_delay = 1500
        self.__missile_speed = 8
        self.__score_multiplier = 1

    def setDifficulty(self, difficulty):
        """
        Méthode permettant de modifier la difficulté du jeu.
        """
        alien_speeds = [3, 4, 6, 6]
        shoot_delays = [1500, 1200, 800, 500]
        missile_speeds = [8, 10, 14, 16]
        score_multipliers = [1, 1.3, 1.6, 2]

        self.__score_multiplier = score_multipliers[int(difficulty)-1]
        self.__alien_speed = alien_speeds[int(difficulty)-1]
        self.__shoot_delay = shoot_delays[int(difficulty)-1]
        self.__missile_speed = missile_speeds[int(difficulty)-1]

    def moveEntity(self, entity, dx, dy):
        """
        Méthode permettant de déplacer une entité.
        """
        if self.__is_playing:
            result = entity.move(dx, dy) # On vérifie si le déplacement est possible
            if result:
                self.__game.moveEntity(entity, dx, dy)

    def placeEntities(self):
        """
        Méthode permettant de placer les entités sur le canvas.
        """
        id = 0
        # On place les aliens sur 3 lignes et 6 colonnes
        for line in range(3):
            for column in range(6):
                alien = Alien(100 + column*100, 50 + line*100, id)
                self.__entities["aliens"].append(alien)
                self.__game.placeEntity(alien)
                id += 1

        # On place les obstacles sur 3 colonnes et 1 ligne
        for column in range(3):
            obstacle = Obstacle(150 + column*200, 500, column)
            self.__entities["obstacles"].append(obstacle)
            self.__game.placeEntity(obstacle)

        # On place le vaisseau au milieu en bas de l'écran
        ship = Ship(self.__screen_width/2, self.__screen_height-50)
        self.__entities["ship"] = ship
        self.__game.placeEntity(ship)
        
    def deleteEntity(self, entity):
        """
        Méthode permettant de supprimer une entité en fonction de son type.
        Pour chaque type, on supprime l'entité du canvas puis on supprime du dictionnaire.
        Si l'entité possède un id, on décrémente les id des entités suivantes.
        """
        self.__game.deleteEntity(entity)

        if entity.getType() == "alien":
            # On supprime l'alien du dictionnaire
            del self.__entities["aliens"][entity.getId()]
            # On décrémente l'id des aliens suivants
            for i in range(entity.getId(), len(self.__entities["aliens"])):
                self.__entities["aliens"][i].decrementId()

        elif entity.getType() == "ship":
            self.__entities["ship"] = None

        elif entity.getType() == "missile":
            if entity.getOrigin() == "ship":
                self.__entities["ship_missile"] = None
            else:
                del self.__entities["aliens_missiles"][entity.getId()]
                # On décrémente l'id des missiles suivants
                for i in range(entity.getId(), len(self.__entities["aliens_missiles"])):
                    self.__entities["aliens_missiles"][i].decrementId()

        elif entity.getType() == "obstacle":
            del self.__entities["obstacles"][entity.getId()]
            # On décrémente l'id des obstacles suivants
            for i in range(entity.getId(), len(self.__entities["obstacles"])):
                self.__entities["obstacles"][i].decrementId()

    def startGame(self):
        """
        Méthode permettant de lancer le jeu.
        """
        self.__is_playing = True
        self.bindKeys()
        self.moveAliens()
        self.moveMissiles()
        self.shootAlien()

    def restart(self):
        """
        Méthode permettant de relancer le jeu.
        """
        self.__entities = {
            "aliens": [],
            "ship": None,
            "ship_missile": None,
            "aliens_missiles": [],
            "obstacles": []
        }
        self.__game.reset()
        self.placeEntities()
        self.__is_playing = True
        self.__game.master.updateLife(3)

    def pauseGame(self):
        """
        Méthode permettant de mettre le jeu en pause.
        Cette méthode met à jour la variable is_playing. Si celle-ci est à False, les fonctions récurssives
        tourneront en boucle sans rien faire.
        """
        self.__is_playing = not self.__is_playing

    def moveAliens(self):
        """
        Méthode récurssive permettant de faire bouger les aliens.
        """
        y_move = 0
        if self.__is_playing:
            for alien in self.__entities["aliens"]:
                # Si un alien est en dehors de l'écran, on inverse le sens de déplacement
                if alien.isOutOfScreen():
                    self.__alien_speed = -self.__alien_speed
                    y_move = 3
                    break
            for alien in self.__entities["aliens"]:
                self.moveEntity(alien, self.__alien_speed, y_move)
                if alien.isColliding(self.__entities["ship"]):
                    self.__is_playing = False
                    self.__game.gameOver()
                    break
        self.__game.master.after(20, self.moveAliens)

    def bindKeys(self):
        """
        Méthode permettant de lier les touches du clavier aux actions du jeu
        """
        self.__game.master.bind("q", lambda event: self.moveEntity(self.__entities["ship"], -10, 0))
        self.__game.master.bind("Q", lambda event: self.moveEntity(self.__entities["ship"], -10, 0))
        self.__game.master.bind("d", lambda event: self.moveEntity(self.__entities["ship"], 10, 0))
        self.__game.master.bind("D", lambda event: self.moveEntity(self.__entities["ship"], 10, 0))

        self.__game.master.bind("<Right>", lambda event: self.moveEntity(self.__entities["ship"], 10, 0))
        self.__game.master.bind("<Left>", lambda event: self.moveEntity(self.__entities["ship"], -10, 0))

        self.__game.master.bind("<space>", lambda event: self.shoot())

        self.__game.master.bind("<Escape>", lambda event: self.__game.master.updatePauseBtn())

    def shoot(self):
        """
        Méthode permettant de faire tirer le vaisseau.
        """
        if self.__is_playing:
            # Le vaisseau ne peut tirer qu'un seul missile à la fois
            if self.__entities["ship_missile"] is not None:
                return
            missile = Missile(self.__entities["ship"].getCoords()[0], self.__entities["ship"].getCoords()[1], -1, "ship")
            self.__entities["ship_missile"] = missile
            self.__game.placeEntity(missile)

    def shootAlien(self):
        """
        Méthode récurssive permettant de faire tirer un alien aléatoirement toutes les x ms.
        """
        if self.__is_playing:
            alien_id = randint(0, len(self.__entities["aliens"])-1)
            alien = self.__entities["aliens"][alien_id]
            missile = Missile(alien.getCoords()[0], alien.getCoords()[1], len(self.__entities["aliens_missiles"]), "alien")
            self.__entities["aliens_missiles"].append(missile)
            self.__game.placeEntity(missile)
        self.__game.master.after(self.__shoot_delay, self.shootAlien)

    def moveMissiles(self):
        """
        Méthode récurssives permettant de faire bouger les missiles.
        """
        if self.__is_playing:

            # Cas du missile du vaisseau
            missile = self.__entities["ship_missile"]
            if missile is not None:
                self.moveEntity(missile, 0, -self.__missile_speed)
                if missile.isOutOfScreen():
                    self.deleteEntity(missile)
                else:
                    for alien in self.__entities["aliens"]:
                        if missile.isColliding(alien):
                            self.deleteEntity(missile)
                            self.deleteEntity(alien)
                            self.__game.master.updateScore(int(10*self.__score_multiplier))
                            break
                    for obstacle in self.__entities["obstacles"]:
                        if missile.isColliding(obstacle):
                            self.deleteEntity(missile)
                            isDead = obstacle.hit()
                            if isDead:
                                self.deleteEntity(obstacle)
                            break
                    for alien_missile in self.__entities["aliens_missiles"]:
                        if missile.isColliding(alien_missile):
                            self.deleteEntity(missile)
                            self.deleteEntity(alien_missile)
                            break
            
            # Cas des missiles des aliens
            for missile in self.__entities["aliens_missiles"]:
                self.moveEntity(missile, 0, self.__missile_speed)
                if missile.isColliding(self.__entities["ship"]):
                    self.deleteEntity(missile)
                    isDead = self.__entities["ship"].hit()
                    self.__game.master.updateScore(-30)
                    self.__game.master.updateLife(self.__entities["ship"].getLife())
                    if isDead:
                        self.__is_playing = False
                        self.__game.gameOver()
                for obstacle in self.__entities["obstacles"]:
                    if missile.isColliding(obstacle):
                        self.deleteEntity(missile)
                        isDead = obstacle.hit()
                        if isDead:
                            self.deleteEntity(obstacle)
                        break

            if self.__entities["aliens"] == []:
                self.__is_playing = False
                self.__game.win()

        self.__game.master.after(20, self.moveMissiles)

    def is_playing(self):
        return self.__is_playing