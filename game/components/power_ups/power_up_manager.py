import pygame
import random

from game.components.power_ups.shield import Shield
from game.components.power_ups.speed_bost import SpeedBoost
from game.utils.constants import SPACESHIP_SHIELD, SPEED_BOOST, NORMAL_GAME_SPEED

class PowerUpManager:
    def __init__(self):
        self.power_ups = []
        self.when_appears = random.randint(5000, 10000)
        self.duration = random.randint(3000, 5000)
        self.start_time = 0

    def update(self, game):
        current_time = pygame.time.get_ticks()

        if len(self.power_ups) == 0 and current_time >= self.when_appears:
            self.generate_power_up()

        for power_up in self.power_ups:
            power_up.update(game.game_speed, self.power_ups)

            if game.player.rect.colliderect(power_up):
                self.start_time = pygame.time.get_ticks()  # Almacenar el tiempo actual
                game.player.has_power_up = True
                game.player.power_up_type = power_up.type
                if power_up.type == "Speedboost":
                    game.game_speed = NORMAL_GAME_SPEED + 5
                game.player.power_up_time_up = self.start_time + self.duration  # Establecer el tiempo de finalización del power-up
                game.player.set_image(SPACESHIP_SHIELD, (65, 75))
                self.power_ups.remove(power_up)
            if game.game_speed > NORMAL_GAME_SPEED:
                if current_time >= game.player.power_up_time_up:
                    game.game_speed = NORMAL_GAME_SPEED
                    game.player.has_power_up = False
                
    def draw(self, screen):
        for power_up in self.power_ups:
            power_up.draw(screen)

    def generate_power_up(self):
        power_up_type = random.choice(["Shield", "SpeedBoost"]) #para escoger entre uno de los 2 de forma random
        if power_up_type == "Shield":
            power_up = Shield()
        elif power_up_type == "SpeedBoost":
            power_up = SpeedBoost(SPEED_BOOST)

        self.when_appears += random.randint(5000, 10000)
        self.power_ups.append(power_up)

    def reset(self):
        now = pygame.time.get_ticks()
        self.power_ups = []
        self.when_appears = random.randint(now + 5000, now + 10000)