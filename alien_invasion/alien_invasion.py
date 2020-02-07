import sys
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf


def run_game():
    pygame.init()
    pygame.display.set_caption("Alien Invasion")

    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))

    ship = Ship(screen)
    while True:

        gf.check_events()

        screen.fill(ai_settings.bg_color)
        ship.blit_me()
        pygame.display.flip()


run_game()
