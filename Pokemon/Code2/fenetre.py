import pygame
from CombatManager import *

NOIR = (0, 0, 0)
VERT = (0, 255, 0)
ROUGE = (255, 0, 0)
BLANC = (255, 255, 255)

# Définir la fenêtre (variable globale)
largeur, hauteur = 800, 600
fenetre = pygame.display.set_mode((largeur, hauteur))
pygame.display.set_caption("Choisissez votre Pokémon")

class Fenetre:
    def __init__(self, largeur, hauteur, titre):
        pygame.init()
        self.surface = pygame.display.set_mode((largeur, hauteur))
        pygame.display.set_caption(titre)
        self.largeur, self.hauteur = pygame.display.get_surface().get_size()
        self.font = pygame.font.Font(None, 36)

    def afficher_image(self, x, y):
        fenetre.blit(self.pokemon_joueur.image, (x, y))

    def afficher_statistiques(self, x, y):
        pygame.draw.rect(fenetre, NOIR, (x, y, 200, 30))  # Fond noir
        pygame.draw.rect(fenetre, VERT, (x, y, (self.pokemon_joueur.statistiques.points_de_vie / 20) * 200, 30))  # Jauge verte

        font = pygame.font.Font(None, 36)
        attributs = [
            ("Attaque", self.pokemon_joueur.statistiques.attaque),
            ("Défense", self.pokemon_joueur.statistiques.defense),
            ("Attaque Spéciale", self.pokemon_joueur.statistiques.attaque_speciale),
            ("Défense Spéciale", self.pokemon_joueur.statistiques.defense_speciale),
            ("Vitesse", self.pokemon_joueur.statistiques.vitesse),
        ]

        pygame.draw.rect(fenetre, NOIR, (x, y + 30, 200, 150))
        for i, (attribut, valeur) in enumerate(attributs):
            texte_attribut = font.render(f"{attribut}: {valeur}", True, BLANC)
            fenetre.blit(texte_attribut, (x + 5, y + 30 + i * 30 + 5))

    def dessiner_rectangle(self, couleur, rect):
        pygame.draw.rect(self.surface, couleur, rect)


    def actualiser_affichage(self):
        pygame.display.flip()
        pygame.time.Clock().tick(5)


