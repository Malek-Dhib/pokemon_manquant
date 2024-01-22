import random
import pygame
from pokemon_type import types_pokemon
from Stats import Statistiques

class Capacite:
    coup_critique = 1
    r = 1.0
    stab = 1.0
    type1_multiplier = 1.0
    type2_multiplier = 1.0


    def __init__(self, nom, puissance, precision, pp, type_capacite, classe_capacite, effet_statistique=None, niveau_attaquant=5):
        self.nom = nom
        self.puissance = puissance
        self.precision = precision
        self.pp = pp
        self.type_capacite = type_capacite.lower()
        self.classe_capacite = classe_capacite
        self.effet_statistique = effet_statistique
        self.niveau_attaquant = niveau_attaquant

    def _evaluer_efficacite(self, adversaire):
        type_attaque = self.type_capacite
        type_adversaire = adversaire.type[0].lower()

        if len(adversaire.type) == 2:
            type_adversaire = adversaire.type[1].lower()

        effectiveness = types_pokemon[type_attaque].relations.get(type_adversaire)

        if effectiveness == 2:
            print(f"L'attaque est super efficace !")
        elif effectiveness == 1:
            print(f"L'attaque est efficace")
        elif effectiveness == 0.5:
            print(f"L'attaque n'est pas très efficace.")
        elif effectiveness == 0:
            print(f"L'attaque n'a aucun effet.")

    def calculer_degats(self, attaquant, adversaire):
        att_stat = attaquant.statistiques.attaque
        att_speciale_stat = attaquant.statistiques.attaque_speciale
        def_stat = adversaire.statistiques.defense
        def_speciale_stat = adversaire.statistiques.defense_speciale

        attaque_utilisee = att_stat
        defense_utilisee = def_stat

        if self.classe_capacite == "Speciale":
            attaque_utilisee = att_speciale_stat
            defense_utilisee = def_speciale_stat

        # Calcul des dégâts selon la formule avec prise en compte des types
        degats = int(
            (
                (
                    (
                        (
                            (
                                (
                                    (attaquant.niveau * 2 / 5) + 2
                                ) * self.puissance * attaque_utilisee / 50
                            ) / defense_utilisee
                        ) * self.coup_critique * self.r / 100
                    ) + 2
                ) * self.stab * self.type1_multiplier * self.type2_multiplier
            )
        )

        # Dégâts minimum de 1 si le défenseur n'est pas immunisé
        return max(degats, 1)

    def utiliser(self, attaquant, adversaire):
        if self.classe_capacite == "Statut" and self.effet_statistique is not None:
            # Appliquer l'effet statistique
            degats, message = self.effet_statistique.utiliser(attaquant, adversaire)
        else:
            # Calcul des dégâts
            degats = self.calculer_degats(attaquant, adversaire)

        # Choix de la statistique d'attaque en fonction de la classe de la capacité
        attaque_utilisee = attaquant.statistiques.attaque
        defense_utilisee = adversaire.statistiques.defense

        if self.classe_capacite == "Speciale":
            attaque_utilisee = attaquant.statistiques.attaque_speciale
            defense_utilisee = adversaire.statistiques.defense_speciale

        # Calcul des dégâts de base
        self.coup_critique = 2 if random.randint(1, 100) <= 10 else 1  # 10% de chance de coup critique

        # Calcul du modificateur aléatoire R
        self.r = random.choice([i for i in range(85, 100)] * 2 + [100]) / 255.0

        # STAB
        self.stab = 2 if self.type_capacite in attaquant.type else 1

        # Type de l'attaque par rapport aux types du défenseur
        type_attaque = self.type_capacite.lower()
        type_adversaire = adversaire.type[0].lower()

        self.type2_multiplier = 1.0
        if len(adversaire.type) == 2:
            type_adversaire_2 = adversaire.type[1].lower()
            self.type2_multiplier = types_pokemon[type_attaque].relations.get(type_adversaire_2, 1.0)

        self.type1_multiplier = types_pokemon[type_attaque].relations.get(type_adversaire, 1.0)

        # Dégâts minimum de 1 si le défenseur n'est pas immunisé
        degats = max(degats, 1)

        adversaire.infliger_degats(degats)

        # Afficher le message approprié en fonction du type de capacité
        message = f"{attaquant.nom} utilise {self.nom} et inflige {degats} dégâts."

        if degats == 0:
            print(f"{attaquant.nom} utilise {self.nom} et {message}.")
        else:
            print(f"{attaquant.nom} utilise {self.nom} et inflige {degats} dégâts.")

        # Ajout d'une attente pour limiter la fréquence d'actualisation
        pygame.time.Clock().tick(5)

        self._evaluer_efficacite(adversaire)

        return degats  # Retourner la valeur des dégâts

# Exemple d'instanciation d'une capacité
Charge = Capacite("Charge", 40, 100, 35, "Normal", "Physique")
Flammeche = Capacite("Flammèche", 40, 100, 25, "Feu", "Speciale")
Pistolet_a_O = Capacite("Pistolet à O", 40, 100, 25, "Eau", "Speciale")
Fouet_Lianes = Capacite("Fouet Lianes", 40, 100, 25, "Plante", "Speciale")
