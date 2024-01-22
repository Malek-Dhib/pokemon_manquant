import pygame
import sys
from PIL import Image
from CombatManager import *
from fenetre import *

pygame.init()


if __name__ == "__main__":
    combat_manager = CombatManager(None, None)
    combat_manager.main()  