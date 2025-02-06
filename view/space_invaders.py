"""
Antoine ROCHAS & Alexandre FERRY
13/11/23
Fichier principal du dossier view qui comporte les éléments graphiques du jeu

Fichier optimisé
"""

import tkinter as tk
from PIL import Image, ImageTk

import assets.colors as colors
from .game_frame import GameFrame
from controller.ui_controller import UIController

class SpaceInvaders(tk.Tk):
    """
    Classe principale du jeu qui affiche la fenêtre principale du jeu.
    """
    def __init__(self):
        super().__init__()
        self.title("Space Invaders")
        self.minsize(950, 700)
        self.config(bg=colors.window_bg)
        self.initUI()
        self.placeUI()
        self.__score = 0

    def initUI(self):
        """
        Initialise l'interface graphique du jeu. Crée les éléments graphiques.
        """
        self.btnFrame = tk.Frame(self, bg=colors.window_bg)
        self.recordLabel = tk.Label(self.btnFrame, text="Record : 0", bg=colors.window_bg, fg=colors.text_color, font=colors.widget_font)

        self.gameFrame = GameFrame(self)
        self.uiController = UIController(self.gameFrame, 700, 700)

        self.quitButton = tk.Button(self.btnFrame, text="Quitter", bg=colors.btn_bg, fg=colors.text_color, font=colors.widget_font, relief=tk.FLAT, activebackground=colors.hover_btn_bg, activeforeground=colors.text_color, width=15, command=self.destroy)
        
        self.newGameButton = tk.Button(self.btnFrame, text="Nouvelle partie", bg=colors.btn_bg, fg=colors.text_color, font=colors.widget_font, relief=tk.FLAT, activebackground=colors.hover_btn_bg, activeforeground=colors.text_color, width=15, command=self.start)

        self.pauseBtn = tk.Button(self.btnFrame, text="Pause", bg=colors.btn_bg, fg=colors.text_color, font=colors.widget_font, relief=tk.FLAT, activebackground=colors.hover_btn_bg, activeforeground=colors.text_color, width=15, command=self.updatePauseBtn)

        self.scoreLabel = tk.Label(self.btnFrame, text=f"Score : 0", bg=colors.window_bg, fg=colors.text_color, font=colors.widget_font)

        self.lifeCanvas = tk.Canvas(self.btnFrame, bg = colors.window_bg, width = 150, height = 50, highlightthickness = 0 )
        self.updateLife(3)

        self.difficulty = tk.Scale(self.btnFrame, from_=1, to=4, orient=tk.HORIZONTAL, bg=colors.window_bg, fg=colors.text_color, font=colors.widget_font, label="Difficulté :", length=200, sliderlength=20, troughcolor=colors.window_bg, highlightthickness=0, activebackground=colors.window_bg, command=self.uiController.setDifficulty)

    def placeUI(self):
        """
        Place les éléments de l'interface graphique.
        """
        self.gameFrame.pack(side=tk.LEFT, padx=10, pady=10)
        self.btnFrame.pack(side=tk.RIGHT, padx=10, pady=10)
        self.lifeCanvas.pack(padx=10, pady=10)
        self.quitButton.pack(padx=10, pady=10)
        self.newGameButton.pack(padx=10, pady=10)
        self.pauseBtn.pack(padx=10, pady=10)
        self.scoreLabel.pack(padx=10, pady=10)
        self.difficulty.pack(padx=10, pady=10)
        self.recordLabel.pack(padx=10, pady=10)

    def updateScore(self, score):
        """
        Met à jour le score affiché.
        """
        self.__score += score
        self.scoreLabel.config(text="Score : " + str(self.__score))

    def updatePauseBtn(self):
        """
        Met à jour les éléments graphiques lors de la mise en pause du jeu ou lors de la reprise du jeu.
        """
        self.uiController.pauseGame()
        if not self.uiController.is_playing():
            self.pauseBtn.config(text="Reprendre")
            self.newGameButton.config(state=tk.NORMAL)
            self.textPause = self.gameFrame.create_text(350, 350, text="Pause", font=("Calibri", 50), fill=colors.text_color)
        else:
            self.pauseBtn.config(text="Pause")
            self.newGameButton.config(state=tk.DISABLED)
            self.gameFrame.delete(self.textPause)

    def updateLife(self, life):
        """
        Met à jour le nombre de vie en changeant l'image des coeurs.
        """
        if life == 3 :
            self.__image_bg= ImageTk.PhotoImage(Image.open("assets/images/3_vies.png").resize((150,50)))
            self.lifeCanvas.create_image(0, 0, image=self.__image_bg, anchor=tk.NW)
        elif life == 2 : 
            self.__image_bg= ImageTk.PhotoImage(Image.open("assets/images/2_vies.png").resize((100,50)))
            self.lifeCanvas.create_image(0, 0, image=self.__image_bg, anchor=tk.NW)
        elif life == 1 : 
            self.__image_bg= ImageTk.PhotoImage(Image.open("assets/images/1_vie.png").resize((50,50)))
            self.lifeCanvas.create_image(0, 0, image=self.__image_bg, anchor=tk.NW)
        elif life == 0:
            self.__image_bg= ImageTk.PhotoImage(Image.open("assets/images/0_vie.png").resize((50,50)))
            self.lifeCanvas.create_image(0, 0, image=self.__image_bg, anchor=tk.NW)

    def start(self):
        """
        Lance une nouvelle partie.
        """
        self.newGameButton.config(state=tk.DISABLED)
        self.uiController.placeEntities()
        self.uiController.startGame()
        self.newGameButton.config(command=self.uiController.restart)

    def getScore(self):
        """
        Retourne le score.
        """
        return self.__score
    
    def updatePersonalBest(self, score):
        """
        Met à jour le meilleur score personnel.
        """
        self.recordLabel.config(text="Record : " + str(score))
