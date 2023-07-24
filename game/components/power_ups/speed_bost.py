import random
import pygame

from pygame.sprite import Sprite
from game.utils.constants import SCREEN_HEIGHT, SCREEN_WIDTH, SPEED_BOOST

class SpeedBoost(Sprite):
    SPEED_BOOST_WIDTH = 40
    SPEED_BOOST_HEIGHT = 60
    def __init__(self, boost_amount):
        self.image = boost_amount
        self.image = pygame.transform.scale(self.image, (self.SPEED_BOOST_HEIGHT, self.SPEED_BOOST_WIDTH))
        self.image = SPEED_BOOST
        self.rect = self.image.get_rect(midtop=(random.randint(120, SCREEN_WIDTH - 120), 0))
        self.type = "Speedboost"

    def apply_power_up(self):
        # Aquí aumentamos temporalmente la velocidad del juego cuando el power-up es recolectado
        global GAME_SPEED
        GAME_SPEED += 20  # Puedes ajustar el valor según cuánto deseas aumentar la velocidad

    def update(self, game_speed, power_ups):
        self.rect.y += game_speed
        if self.rect.y < 0 or self.rect.y >= SCREEN_HEIGHT:
            power_ups.remove(self)

    def draw(self, screen):
        screen.blit(self.image, self.rect)