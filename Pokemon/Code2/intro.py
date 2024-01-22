import pygame
import sys
import time

def lancer_intro():
    pygame.init()

    # Paramètres de la fenêtre
    largeur_fenetre = 800
    hauteur_fenetre = 600
    fenetre = pygame.display.set_mode((largeur_fenetre, hauteur_fenetre))
    pygame.display.set_caption("Introduction Pokémon")

    # Chargement de l'image du personnage
    personnage_image = pygame.image.load("Code2/Chen1.png")
    personnage_rect = personnage_image.get_rect(center=(largeur_fenetre // 2, hauteur_fenetre // 2))

    # Couleurs
    couleur_bleu_ciel = (173, 216, 230)
    couleur_texte = (0, 0, 0)
    couleur_box = (255, 255, 255)

    # Musique de fond
    pygame.mixer.music.load("Code2/intro.mp3")
    pygame.mixer.music.play(-1)  # -1 signifie la répétition indéfinie

    # Police pour le texte
    pygame.font.init()
    police = pygame.font.Font(None, 36)

    # Dialogue du personnage
    dialogue = [
        "Bien le bonjour!",
        "Bienvenue dans le monde magique des Pokémon!",
        "Mon nom est Chen! ",
        "Les gens m'appellent souvent le Prof Pokémon!",
        "Pour certains, les Pokémon sont des animaux domestiques, ",
        "pour d'autres, ils sont un moyen de combattre.",
        "Pour ma part... L'étude des Pokémon est ma profession.",
        "Je suppose que si tu es ici, c'est que tu es aussi intéressé par ces créatures fantastiques. ",
        "Je me réjouis de t'avoir à mes côtés. Je suis sûr que tu vas grandement m'aider!",
        "Ta quête des Pokémon est sur le point de commencer!",
        "Un tout nouveau monde de rêves, d'aventures et de Pokémon t'attend!",
        "Aujourd'hui, tu commenceras ton voyage en choisissant ton premier Pokémon.",
        "Les Pokémon sont des créatures étonnantes avec lesquelles tu feras équipe.",
        "Sélectionne ton Pokémon de départ, affronte ton adversaire et que l'aventure commence!"
    ]

    # Affichage progressif du dialogue
    def afficher_dialogue_progressif(message, x, y, largeur, hauteur):
        texte = ""
        surface_texte = pygame.Surface((largeur, hauteur), pygame.SRCALPHA)
        surface_texte.fill((255, 255, 255, 0))  # Fond transparent
        fenetre.blit(surface_texte, (x, y))
        pygame.display.flip()

        for lettre in message:
            texte += lettre
            texte_surface = police.render(texte, True, couleur_texte)
            fenetre.blit(surface_texte, (x, y))
            fenetre.blit(texte_surface, (x + 10, y + 10))
            pygame.display.flip()
            pygame.time.wait(50)  # Pause de 50 millisecondes entre chaque lettre

    # Affichage progressif de l'image
    def afficher_image_progressive(image, rect, x, y, largeur, hauteur):
        fenetre.blit(image, rect.topleft)
        pygame.display.flip()

        for i in range(255):
            pygame.time.Clock().tick(60)
            fenetre.fill(couleur_bleu_ciel)

            alpha_surface = pygame.Surface((largeur, hauteur), pygame.SRCALPHA)
            alpha_surface.fill((255, 255, 255, i))
            fenetre.blit(alpha_surface, (x, y))

            fenetre.blit(image, rect.topleft)
            pygame.display.flip()

    # Boucle principale
    clock = pygame.time.Clock()
    running = True
    index_dialogue = 0

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Passer à la phrase suivante en cliquant ou appuyant sur espace
            if event.type == pygame.MOUSEBUTTONDOWN or (event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE):
                index_dialogue += 1
                if index_dialogue >= len(dialogue):
                    running = False

        # Affichage progressif de l'image
        afficher_image_progressive(personnage_image, personnage_rect, 50, 50, 700, 500)

        # Affichage progressif du dialogue
        if index_dialogue < len(dialogue):
            afficher_dialogue_progressif(dialogue[index_dialogue], 50, hauteur_fenetre - 200, largeur_fenetre - 100, 150)

        pygame.display.flip()

        clock.tick(30)  # Limite de 30 images par seconde

lancer_intro()
