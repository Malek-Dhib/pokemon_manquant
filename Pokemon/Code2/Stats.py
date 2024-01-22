import random

class Statistiques:
    def __init__(self):
        self.points_de_vie = 20
        self.attaque = random.randint(1, 15)
        self.defense = random.randint(1, 15)
        self.attaque_speciale = random.randint(1, 15)
        self.defense_speciale = random.randint(1, 15)
        self.vitesse = random.randint(1, 15)
        self.niveau = 5

    def calculer_degats(self, attaquant, adversaire, capacite):
        att_stat = attaquant.statistiques.attaque
        att_speciale_stat = attaquant.statistiques.attaque_speciale
        def_stat = adversaire.statistiques.defense
        def_speciale_stat = adversaire.statistiques.defense_speciale

        if capacite.classe_capacite == "Physique":
            attaque_utilisee = att_stat
            defense_utilisee = def_stat
        else:
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
                                ) * capacite.puissance * attaque_utilisee / 50
                            ) / defense_utilisee
                        ) * capacite.coup_critique * capacite.r / 100
                    ) + 2
                ) * capacite.stab * capacite.type1_multiplier * capacite.type2_multiplier
            )
        )

        # Dégâts minimum de 1 si le défenseur n'est pas immunisé
        return max(degats, 1)

def baisser_statistiques_aleatoires(self, pourcentage):
        # Liste des statistiques à réduire
        statistiques_a_reduire = ["attaque", "defense", "attaque_speciale", "defense_speciale", "vitesse", "points_de_vie"]

        # Boucle sur chaque statistique
        for statistique in statistiques_a_reduire:
            # Obtenez la valeur actuelle de la statistique
            valeur_actuelle = getattr(self, statistique)
            
            # Calculez la réduction basée sur le pourcentage
            reduction = int(valeur_actuelle * (pourcentage / 100))
            
            # Appliquez la réduction de manière aléatoire
            reduction_aleatoire = random.randint(0, reduction)
            
            # Mettez à jour la statistique réduite
            setattr(self, statistique, max(0, valeur_actuelle - reduction_aleatoire))