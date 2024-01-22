from pokemon import Pokemon
import pygame
from PIL import Image
from Stats import Statistiques
from fenetre import *
from Capacité import Capacite
from Capacite_stats import CapaciteStatistique

class Salamèche(Pokemon):
    def __init__(self, nom, image, capacites):
        super().__init__(nom, "Feu", pygame.image.load("resized_autocollant-salameche-pokemon-004.png"), capacites)

    def afficher_image(self, x, y):
        # Votre logique pour afficher l'image de Salamèche
        fenetre.blit(self.image, (x, y))


class Carapuce(Pokemon):
    def __init__(self, nom, image, capacites):
        super().__init__(nom, "Eau", pygame.image.load("resized_250px-Carapuce-RFVF.png"), capacites)

    def afficher_image(self, x, y):
        # Votre logique pour afficher l'image de Salamèche
        fenetre.blit(self.image, (x, y))


class Bulbizarre(Pokemon):
    def __init__(self, nom, image, capacites):
        super().__init__(nom, "Plante", pygame.image.load("resized_autocollant-bulbizarre-pokemon-001.png"), capacites)

    def afficher_image(self, x, y):
        # Votre logique pour afficher l'image de Salamèche
        fenetre.blit(self.image, (x, y))

class pokemon :
    def __init__(self,nom_pokemon, type_pokemon, image, Statistiques, capacites):
        self.nom = nom_pokemon
        self.type_pokemon = type_pokemon
        self.image = image 
        self.Statistiques = Statistiques
        self.capacites = capacites  

    def afficher_pokemon (self):
        Salamèche (Salamèche, "feu", pygame.image.load("resized_autocollant-salameche-pokemon-004.png"), Statistiques(), Capacite)
        Bulbizarre ( Bulbizarre, "plante", pygame.image.load("resized_autocollant-salameche-pokemon-004.png"), Statistiques(), Capacite)
        Carapuce (Carapuce, "eau", pygame.image.load("resized_autocollant-salameche-pokemon-004.png"), Statistiques(), Capacite)
    
    def afficher_image(self, x, y):
        # Votre logique pour afficher l'image de Salamèche
        fenetre.blit(self.image, (x, y))

