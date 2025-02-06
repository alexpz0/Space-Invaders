# Space Invaders

#### **STRUCTURE DU PROJET**

Nous avons divisé notre projet en 3 parties principales : la vue, le modèle et le controleur. 

**La vue** régit l'affichage visuel de notre jeu, c'est à dire la fenêtre principal, les différents canvas et bouttons... On utilise ici la bibliothèque graphique Tkinter et PIL.

**Le modèle** permet de créer nos entités en leur attribuant une position, une hitbox ect... C'est ici que sont mentionnées les caractéristiques des entités de base de notre projet. Le modèle contient également les piles, files et listes que nous devions implémenter pour ce projet.

Enfin **le controlleur** permet de déterminer les touches qui permettront à l'utilisateur de jouer. De plus, c'est aussi dans le controlleur que l'on gère les évènements de notre jeu comme les tirs, les déplacements et les collisions.

#### **REGLES DU JEU**

Le joueur incarne un vaisseau qui doit éliminer tous les aliens ennemis. Pour cela, il a la capacité de tirer des missiles qui tuent les aliens en un coup. De plus, l'utilisateur dispose de 3 vies. C'est à dire qu'il peut encaisser deux missiles d'alien avant de mourir. 

Il y aussi des obstacles sous forme d'asteroïdes qui permettent de protéger le vaisseau. Chacun d'eux a 3 vies et disparait lorsqu'il n'en a plus.

Nous avons implementé 4 niveaux de difficultés dans notre jeu. A chaque niveau, la vitesse des missiles ainsi que la vitesse de déplacement des aliens augmentent.
 
#### **LES TOUCHES**

Le joueur déplace son vaisseau vers la gauche avec la touche ***q*** ou bien avec la ***flèche gauche*** et vers la droite avec la touche ***d*** ou bien avec ***flèche droite***. Il tire avec la touche ***espace***. il a la possibilité de mettre pause en cliquant sur le bouton ***Pause*** ou en appuyant sur la touche ***ECHAP***.

