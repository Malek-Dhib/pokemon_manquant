class TypePokemon:
    def __init__(self, nom):
        self.nom = nom
        self.relations = {}

    # Initialisation des types
types_pokemon = {
    "normal": TypePokemon("Normal"),
    "feu": TypePokemon("Feu"),
    "plante": TypePokemon("Plante"),
    "eau": TypePokemon("Eau"),
    "roche": TypePokemon("Roche"),
    "combat": TypePokemon("Combat"),
    "insecte": TypePokemon("Insecte"),
    "poison": TypePokemon("Poison"),
    "acier": TypePokemon("Acier"),
    "électrik": TypePokemon("Électrik"),
    "psy": TypePokemon("Psy"),
    "ténèbres": TypePokemon("Ténèbres"),
    "spectre": TypePokemon("Spectre"),
    "dragon": TypePokemon("Dragon"),
    "glace": TypePokemon("Glace"),
    "fée": TypePokemon("Fée"),
    "vol": TypePokemon("Vol"),
    "sol": TypePokemon("Sol"),
}

# Relations d'avantage/désavantage pour chaque type
types_pokemon["eau"].relations = {
    "Normal":1, "Feu": 2, "Acier": 1, "Eau": 0.5, "Dragon": 0.5, "Combat": 1,
    "Fée": 1, "Électrik": 1, "Plante": 0.5, "Glace": 1, "Insecte": 1,
    "Poison": 1, "Psy": 1, "Sol": 2, "Spectre": 1, "Ténèbres": 1, "Vol": 1, "Roche": 2
}

types_pokemon["feu"].relations = {

    "Normal":1, "Feu": 0.5, "Acier": 2, "Eau": 0.5, "Dragon": 0.5, "Combat": 1,
    "Fée": 1, "Électrik": 1, "Plante": 2, "Glace": 2, "Insecte": 2,
    "Poison": 1, "Psy": 1, "Sol": 1, "Spectre": 1, "Ténèbres": 1, "Vol": 1, "Roche": 0.5
}

types_pokemon["plante"].relations = {

    "Normal":1, "Feu": 0.5, "Acier": 0.5, "Eau": 2, "Dragon": 0.5, "Combat": 1,
    "Fée": 1, "Électrik": 1, "Plante": 0.5, "Glace": 1, "Insecte": 0.5,
    "Poison": 0.5, "Psy": 1, "Sol": 2, "Spectre": 1, "Ténèbres": 1, "Vol": 0.5, "Roche": 2
}

types_pokemon["normal"].relations = {
 
    "Normal":1, "Feu": 1, "Acier": 0.5, "Eau": 1, "Dragon": 0.5, "Combat": 1,
    "Fée": 1, "Électrik": 1, "Plante": 1, "Glace": 1, "Insecte": 1,
    "Poison": 1, "Psy": 1, "Sol": 1, "Spectre": 0, "Ténèbres": 1, "Vol": 1, "Roche": 0.5
}

types_pokemon["acier"].relations = {

    "Normal":1, "Feu": 0.5, "Acier": 0.5, "Eau": 0.5, "Dragon": 0.5, "Combat": 1,
    "Fée": 2, "Électrik": 0.5, "Plante": 1, "Glace": 2, "Insecte": 1,
    "Poison": 1, "Psy": 1, "Sol": 1, "Spectre": 1, "Ténèbres": 1, "Vol": 1, "Roche": 2
}

types_pokemon["combat"].relations = {

    "Normal":0.5, "Feu": 1, "Acier": 2, "Eau": 1, "Dragon": 0.5, "Combat": 1,
    "Fée": 0.5, "Électrik": 1, "Plante": 1, "Glace": 2, "Insecte": 0.5,
    "Poison": 0.5, "Psy": 0.5, "Sol": 1, "Spectre": 1, "Ténèbres": 2, "Vol": 0.5, "Roche": 2
}

types_pokemon["dragon"].relations = {

    "Normal":1, "Feu": 1, "Acier": 0.5, "Eau": 1, "Dragon": 2, "Combat": 1,
    "Fée": 0, "Électrik": 1, "Plante": 1, "Glace": 1, "Insecte": 1,
    "Poison": 1, "Psy": 1, "Sol": 1, "Spectre": 1, "Ténèbres": 1, "Vol": 1, "Roche": 1
}

types_pokemon["électrik"].relations = {

    "Normal":1, "Feu": 1, "Acier": 1, "Eau": 2, "Dragon": 0.5, "Combat": 1,
    "Fée": 1, "Électrik": 0.5, "Plante": 0.5, "Glace": 1, "Insecte": 0.5,
    "Poison": 1, "Psy": 1, "Sol": 0, "Spectre": 1, "Ténèbres": 1, "Vol": 2, "Roche": 1
}

types_pokemon["fée"].relations = {

    "Normal":1, "Feu": 0.5, "Acier": 0.5, "Eau": 1, "Dragon": 2, "Combat": 2,
    "Fée": 1, "Électrik": 1, "Plante": 1, "Glace": 1, "Insecte": 1,
    "Poison": 0.5, "Psy": 1, "Sol": 1, "Spectre": 1, "Ténèbres": 2, "Vol": 1, "Roche": 1
}

types_pokemon["psy"].relations = {

    "Normal":1, "Feu": 1, "Acier": 0.5, "Eau": 1, "Dragon": 1, "Combat": 2,
    "Fée": 1, "Électrik": 1, "Plante": 1, "Glace": 1, "Insecte": 1,
    "Poison": 2, "Psy": 0.5, "Sol": 1, "Spectre": 1, "Ténèbres": 0, "Vol": 1, "Roche": 1
}

types_pokemon["glace"].relations = {

    "Normal":1, "Feu": 0.5, "Acier": 0.5, "Eau": 0.5, "Dragon": 2, "Combat": 0.5,
    "Fée": 1, "Électrik": 1, "Plante": 2, "Glace": 0.5, "Insecte": 1,
    "Poison": 1, "Psy": 1, "Sol":2, "Spectre": 1, "Ténèbres": 2, "Vol": 2, "Roche": 1
}

types_pokemon["poison"].relations = {

    "Normal":1, "Feu": 1, "Acier": 0, "Eau": 1, "Dragon": 1, "Combat": 2,
    "Fée": 2, "Électrik": 1, "Plante": 2, "Glace": 1, "Insecte": 1,
    "Poison": 0.5, "Psy": 1, "Sol": 0.5, "Spectre": 0.5, "Ténèbres": 1, "Vol": 1, "Roche": 0.5
}

types_pokemon["roche"].relations = {

    "Normal":1, "Feu": 2, "Acier": 0.5, "Eau": 1, "Dragon": 1, "Combat": 0.5,
    "Fée": 1, "Électrik": 1, "Plante": 1, "Glace": 2, "Insecte": 2,
    "Poison": 1, "Psy": 1, "Sol": 0.5, "Spectre": 1, "Ténèbres": 1, "Vol": 2, "Roche": 1
}

types_pokemon["sol"].relations = {

    "Normal":1, "Feu": 2, "Acier": 2, "Eau": 1, "Dragon": 1, "Combat": 1,
    "Fée": 1, "Électrik": 2, "Plante": 0.5, "Glace": 0.5, "Insecte": 1,
    "Poison": 2, "Psy": 1, "Sol": 1, "Spectre": 1, "Ténèbres": 1, "Vol": 0, "Roche": 2
}

types_pokemon["spectre"].relations = {

    "Normal":0, "Feu": 1, "Acier": 1, "Eau": 1, "Dragon": 1, "Combat": 1,
    "Fée": 1, "Électrik": 1, "Plante": 1, "Glace": 1, "Insecte": 1,
    "Poison": 1, "Psy": 2, "Sol": 1, "Spectre": 2, "Ténèbres": 0.5, "Vol": 1, "Roche": 1
}

types_pokemon["ténèbres"].relations = {

    "Normal":1, "Feu": 1, "Acier": 1, "Eau": 1, "Dragon": 1, "Combat": 0.5,
    "Fée": 0.5, "Électrik": 1, "Plante": 1, "Glace": 1, "Insecte": 1,
    "Poison": 1, "Psy": 2, "Sol": 1, "Spectre": 2, "Ténèbres": 0.5, "Vol": 1, "Roche": 1
}

types_pokemon["vol"].relations = {

    "Normal":1, "Feu": 1, "Acier": 0.5, "Eau": 1, "Dragon": 1, "Combat": 2,
    "Fée": 1, "Électrik": 0.5, "Plante": 2, "Glace": 1, "Insecte": 2,
    "Poison": 1, "Psy": 1, "Sol": 1, "Spectre": 1, "Ténèbres": 1, "Vol": 1, "Roche": 0.5
}

types_pokemon["insecte"].relations = {

    "Normal":1, "Feu": 0.5, "Acier": 0.5, "Eau": 1, "Dragon": 1, "Combat": 0.5,
    "Fée": 0.5, "Électrik": 1, "Plante": 2, "Glace": 1, "Insecte": 1,
    "Poison": 0.5, "Psy": 2, "Sol": 1, "Spectre": 0.5, "Ténèbres": 2, "Vol": 0.5, "Roche": 0.5
}
