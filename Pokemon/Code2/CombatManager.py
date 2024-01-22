import pygame
import sys
import random
import time
from GameManager import GameManager
from fenetre import *
from Capacité import *
from Capacite_stats import *

class CombatManager:
    def __init__(self, pokemon_joueur, pokemon_adversaire):
        self.pokemon_joueur = pokemon_joueur
        self.pokemon_adversaire = pokemon_adversaire
        self.attaque_selectionnee = None
        self.font = pygame.font.Font(None, 36)
        self.etat_combat = "ChoixAttaque"

    def initialiser(self):
        self.fenetre.main_loop(self.boucle_principale)

    def afficher_message_progressif(self, message):
        pygame.draw.rect(fenetre, BLANC, (50, hauteur - 100, largeur - 100, 50))  # Boîte blanche
        font = pygame.font.Font(None, 36)
        
        message_affichage = ""
        
        for char in message:
            message_affichage += char
            texte_message = font.render(message_affichage, True, NOIR)
            fenetre.blit(texte_message, (60, hauteur - 90))
            pygame.display.flip()
            pygame.time.delay(100)


    def tour_joueur(self):
        attaque_selectionnee = None

        while attaque_selectionnee is None:
            attaque_selectionnee = self.choisir_attaque_clavier()
            if attaque_selectionnee is not None:
                break

            attaque_selectionnee = self.choisir_attaque_souris()

        self.attaque_selectionnee = attaque_selectionnee

        if self.attaque_selectionnee is not None:
            capacite_joueur = self.pokemon_joueur.capacites[self.attaque_selectionnee]
            degats_joueur = capacite_joueur.utiliser(self.pokemon_joueur, self.pokemon_adversaire)
            message_joueur = f"{self.pokemon_joueur.nom} utilise {capacite_joueur.nom} et inflige {degats_joueur} dégâts !"
            message_joueur_2 = f"{self.pokemon_adversaire.nom} perd {degats_joueur} PV !"
            self.afficher_message_progressif(message_joueur)
            self.afficher_message_progressif(message_joueur_2)
            time.sleep(2)


    def attaque_adversaire(self):
        capacite_adversaire = random.choice(self.pokemon_adversaire.capacites)
        if capacite_adversaire:
            degats_adversaire = capacite_adversaire.utiliser(self.pokemon_adversaire, self.pokemon_joueur)
            message = f"{self.pokemon_adversaire.nom} utilise {capacite_adversaire.nom} et inflige {degats_adversaire} dégâts !"
            message_joueur_2 = f"{self.pokemon_joueur.nom} perd {degats_adversaire} PV !"
            self.afficher_message_progressif(message)
            self.afficher_message_progressif(message_joueur_2)
            time.sleep(2)

        self.afficher_statut_combat()

    def tour_adversaire(self):
        self.attaque_adversaire()
        self.afficher_menu_attaques()

    def combat(self):
        while self.pokemon_joueur.statistiques.points_de_vie > 0 and self.pokemon_adversaire.statistiques.points_de_vie > 0:
            attaquant, defenseur = self.determiner_ordre_attaque()

            if self.etat_combat == "ChoixAttaque":
                self.afficher_message_progressif("Choisissez une attaque")
                self.attaque_selectionnee = self.choisir_attaque()

            # Attaque de l'adversaire
            self.attaque_adversaire()

            # Affichage des PV et message
            self.afficher_statut_combat()

            if self.pokemon_joueur.statistiques.points_de_vie <= 0:
                self.etat_combat = "FinCombat"
                self.afficher_message_progressif(f"{self.pokemon_adversaire.nom} a gagné !")
                break

            # Attaque du joueur
            if self.attaque_selectionnee is not None:
                capacite_joueur = self.pokemon_joueur.capacites[self.attaque_selectionnee]
                degats_joueur = capacite_joueur.utiliser(self.pokemon_joueur, self.pokemon_adversaire)
                message_joueur = f"{self.pokemon_joueur.nom} utilise {capacite_joueur.nom} et inflige {degats_joueur} dégâts !"
                message_joueur_2 = f"{self.pokemon_adversaire.nom} perd {degats_joueur} PV !"
                self.afficher_message_progressif(message_joueur)
                self.afficher_message_progressif(message_joueur_2)
                time.sleep(2)

            if self.pokemon_adversaire.statistiques.points_de_vie <= 0:
                self.etat_combat = "FinCombat"
                self.afficher_message_progressif(f"{self.pokemon_joueur.nom} a gagné !")
                break

        # Afficher le message du vainqueur après la boucle de combat
        pygame.display.flip()
        pygame.time.Clock().tick(5)  # Ajout d'une attente pour limiter la fréquence d'actualisation
        self.afficher_message_progressif(f"{self.pokemon_joueur.nom} a gagné !")



    def afficher_statut_combat(self):
        fenetre.fill(NOIR)

        self.pokemon_joueur.afficher_image(50, 200)
        self.pokemon_joueur.afficher_statistiques(50, 170)
        self.pokemon_adversaire.afficher_image(largeur - 250, 200)
        self.pokemon_adversaire.afficher_statistiques(largeur - 250, 170)

        for i, attaque in enumerate(self.pokemon_joueur.capacites):
            rect = pygame.Rect(50, 400 + i * 30, 200, 30)
            pygame.draw.rect(fenetre, ROUGE if i == self.attaque_selectionnee else BLANC, rect, 2)
            texte_attaque = self.font.render(attaque.nom, True, BLANC)
            fenetre.blit(texte_attaque, (rect.x + 5, rect.y + 5))

        if self.etat_combat == "ChoixAttaque":
            self.afficher_box("Choisissez une attaque")
        elif self.etat_combat == "FinCombat":
            self.afficher_box(f"{self.pokemon_joueur.nom} a gagné !")

        # Affichage des PV et message
        self.afficher_pv()

        pygame.display.flip()
        pygame.time.Clock().tick(5)

        if self.pokemon_joueur.statistiques.points_de_vie <= 0:
            self.etat_combat = "FinCombat"
            self.afficher_box(f"{self.pokemon_adversaire.nom} a gagné !")

    def afficher_pv(self):
        pygame.draw.rect(fenetre, BLANC, (50, hauteur - 100, largeur - 100, 50))  # Boîte blanche
        font = pygame.font.Font(None, 36)
        texte_pv_joueur = font.render(f"PV: {self.pokemon_joueur.statistiques.points_de_vie}", True, NOIR)
        texte_pv_adversaire = font.render(f"PV: {self.pokemon_adversaire.statistiques.points_de_vie}", True, NOIR)
        fenetre.blit(texte_pv_joueur, (60, hauteur - 90))
        fenetre.blit(texte_pv_adversaire, (largeur - 250, hauteur - 90))

    def main(self):
        pygame.display.flip()
        self.pokemon_joueur = GameManager().choisir_pokemon()
        self.pokemon_adversaire = GameManager().choisir_pokemon()

        font = pygame.font.Font(None, 36)  # Ajout de cette ligne pour définir la police

        while self.pokemon_joueur.statistiques.points_de_vie > 0 and self.pokemon_adversaire.statistiques.points_de_vie > 0:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        if self.attaque_selectionnee is not None:
                            self.combat()
                            self.attaque_selectionnee = None

                    elif event.key == pygame.K_UP:
                        if self.attaque_selectionnee is not None:
                            self.attaque_selectionnee = (self.attaque_selectionnee - 1) % len(self.pokemon_joueur.capacites)

                    elif event.key == pygame.K_DOWN:
                        if self.attaque_selectionnee is not None:
                            self.attaque_selectionnee = (self.attaque_selectionnee + 1) % len(self.pokemon_joueur.capacites)

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:  # Bouton gauche de la souris
                        x, y = event.pos
                        # Vérifier si le clic est sur une attaque
                        for i, attaque in enumerate(self.pokemon_joueur.capacites):
                            attaque_rect = pygame.Rect(50, 400 + i * 30, 200, 30)
                            if attaque_rect.collidepoint(x, y):
                                self.attaque_selectionnee = i

            fenetre.fill(NOIR)

            self.pokemon_joueur.afficher_image(50, 200)
            self.pokemon_joueur.afficher_statistiques(50, 170)
            self.pokemon_adversaire.afficher_image(largeur - 250, 200)
            self.pokemon_adversaire.afficher_statistiques(largeur - 250, 170)

            for i, attaque in enumerate(self.pokemon_joueur.capacites):
                rect = pygame.Rect(50, 400 + i * 30, 200, 30)
                pygame.draw.rect(fenetre, ROUGE if i == self.attaque_selectionnee else BLANC, rect, 2)
                texte_attaque = font.render(attaque.nom, True, BLANC)
                fenetre.blit(texte_attaque, (rect.x + 5, rect.y + 5))

            self.afficher_message_progressif("Choisir une attaque !")

            pygame.display.flip()
            pygame.time.Clock().tick(5)

            if self.pokemon_joueur.statistiques.points_de_vie <= 0:
                self.afficher_message_progressif(f"{self.pokemon_adversaire.nom} a gagné !")
                break

            # Tour du joueur
            self.tour_joueur()

            # Tour de l'adversaire
            self.tour_adversaire()

        self.afficher_message_progressif(f"{self.pokemon_joueur.nom} a gagné !")
        pygame.display.flip()
        pygame.time.Clock().tick(5)

    def afficher_menu_attaques(self):
        font = pygame.font.Font(None, 36)
        attaques = self.pokemon_joueur.capacites

        for i, attaque in enumerate(attaques):
            texte_attaque = font.render(f"{i + 1}. {attaque.nom}", True, BLANC)
            fenetre.blit(texte_attaque, (50, 400 + i * 30))

    def choisir_attaque(self):
        attaque_selectionnee = None

        while not attaque_selectionnee:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:  # Bouton gauche de la souris
                        x, y = event.pos
                        attaque_selectionnee = self.verifier_clic_attaque(x, y)

            # Affichage en cours de choix d'attaque
            self.afficher_statut_combat()

        return attaque_selectionnee

    def verifier_clic_attaque(self, x, y):
        attaques = self.pokemon_joueur.capacites

        for i, attaque in enumerate(attaques):
            attaque_rect = pygame.Rect(50, 400 + i * 30, 200, 30)
            if attaque_rect.collidepoint(x, y):
                return i

        return None

    def choisir_attaque_souris(self):
        font = pygame.font.Font(None, 36)
        attaques = self.pokemon_joueur.capacites

        selection_effectuee = False
        attaque_selectionnee = None

        while not selection_effectuee:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:  # Bouton gauche de la souris
                        x, y = event.pos
                        # Vérifier si le clic est sur une attaque
                        for i, attaque in enumerate(attaques):
                            attaque_rect = pygame.Rect(50, 400 + i * 30, 200, 30)
                            if attaque_rect.collidepoint(x, y):
                                attaque_selectionnee = i
                                selection_effectuee = True

            self.pokemon_joueur.afficher_image(50, 200)
            self.pokemon_joueur.afficher_statistiques(50, 170)
            self.pokemon_adversaire.afficher_image(largeur - 250, 200)
            self.pokemon_adversaire.afficher_statistiques(largeur - 250, 170)

            if attaque_selectionnee is not None:
                pygame.draw.rect(fenetre, ROUGE, (50, 400 + attaque_selectionnee * 30, 200, 30), 2)

            self.afficher_menu_attaques()

            pygame.display.flip()
            pygame.time.Clock().tick(5)  # Ajout d'une attente pour limiter la fréquence d'actualisation

        self.attaque_selectionnee = attaque_selectionnee
        return self.attaque_selectionnee

    def choisir_attaque_clavier(self):
        attaques = self.pokemon_joueur.capacites

        selection_effectuee = False
        attaque_selectionnee = None

        while not selection_effectuee:
            fenetre.fill(NOIR)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:  # Bouton gauche de la souris
                        x, y = event.pos
                        # Vérifier si le clic est sur une attaque
                        for i, attaque in enumerate(attaques):
                            attaque_rect = pygame.Rect(50, 400 + i * 30, 200, 30)
                            if attaque_rect.collidepoint(x, y):
                                attaque_selectionnee = i
                                selection_effectuee = True
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        selection_effectuee = True
                    elif event.key == pygame.K_UP and attaque_selectionnee is not None:
                        attaque_selectionnee = (attaque_selectionnee - 1) % len(attaques)
                    elif event.key == pygame.K_DOWN and attaque_selectionnee is not None:
                        attaque_selectionnee = (attaque_selectionnee + 1) % len(attaques)

            self.pokemon_joueur.afficher_image(50, 200)
            self.pokemon_joueur.afficher_statistiques(50, 170)
            self.pokemon_adversaire.afficher_image(largeur - 250, 200)
            self.pokemon_adversaire.afficher_statistiques(largeur - 250, 170)

            # Afficher les attaques
            for i, attaque in enumerate(attaques):
                pygame.draw.rect(fenetre, ROUGE if i == attaque_selectionnee else BLANC, (50, 400 + i * 30, 200, 30), 2)
                texte_attaque = self.font.render(attaque.nom, True, BLANC)
                fenetre.blit(texte_attaque, (55, 400 + i * 30 + 5))

            pygame.display.flip()
            pygame.time.Clock().tick(30)

        return attaque_selectionnee

    def determiner_ordre_attaque(self):
        if self.pokemon_joueur.statistiques.vitesse > self.pokemon_adversaire.statistiques.vitesse:
            return self.pokemon_joueur, self.pokemon_adversaire
        elif self.pokemon_joueur.statistiques.vitesse < self.pokemon_adversaire.statistiques.vitesse:
            return self.pokemon_adversaire, self.pokemon_joueur
        else:
            # Égalité de vitesse, utilisez la randomisation
            return random.sample([self.pokemon_joueur, self.pokemon_adversaire], 2)


    
    def afficher_box(self, message):
        pygame.draw.rect(fenetre, BLANC, (50, hauteur - 100, largeur - 100, 50))  # Boîte blanche
        font = pygame.font.Font(None, 36)
        texte_message = font.render(message, True, NOIR)
        fenetre.blit(texte_message, (60, hauteur - 90))
        pygame.display.flip()  # Ajout de cette ligne pour afficher immédiatement la boîte
