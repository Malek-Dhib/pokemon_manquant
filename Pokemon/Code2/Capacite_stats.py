import random 
from pokemon_type import types_pokemon
from Stats import Statistiques

class CapaciteStatistique:
    def __init__(self, nom_stat, precision, pp, type_capacite, classe_capacite, effet_statistique,):
        self.nom_stat= nom_stat
        self.precision = precision
        self.pp = pp
        self.type_capacite = type_capacite.lower()
        self.classe_capacite = classe_capacite
        self.effet_statistique = effet_statistique

    def utiliser(self, attaquant, adversaire):
        # Altération des statistiques de l'adversaire
        adversaire.statistiques.baisser_statistiques_aleatoires(pourcentage=10)
        return 0, f"{attaquant.nom} utilise {self.nom_stat}, l'attaque de {adversaire.nom} a baissé." if self.nom_stat == "Rugissement" else f"{attaquant.nom} utilise {self.nom_stat}, la défense de {adversaire.nom} a baissé."

# Exemple d'instanciation d'une capacité statistique
Rugissement = CapaciteStatistique("Rugissement", 100, 40, "Normal", "Statut", {'statistique': 'Attaque'})
Mimi_Queue = CapaciteStatistique("Mimi-Queue", 100, 30, "Normal", "Statut", {'statistique': 'Defense'})

