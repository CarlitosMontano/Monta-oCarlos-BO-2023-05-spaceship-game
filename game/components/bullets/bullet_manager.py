import pygame

class BulletManager:
    def __init__(self):
        self.player_bullets = []
        self.enemy_bullets = []

    def update(self, game):
        self.add_bullet

        for bullet in self.enemy_bullets:
            bullet.update(self.enemy_bullets)

            if bullet.rect.colliderect(game.player) and bullet.owner == 'enemy':
                game.playing = False
                pygame.time.delay(2000)
                break
            
        for bullet in self.player_bullets:
            bullet.update(self.player_bullets)
                
    def draw(self, screen):
        for bullet in self.enemy_bullets:
            bullet.draw(screen)

        for bullet in self.player_bullets:
            bullet.draw(screen)

    def add_bullet(self, bullet):
        if bullet.owner == 'enemy' and len(self.enemy_bullets) < 4:
            self.enemy_bullets.append(bullet)

        if bullet.owner == 'player' and len(self.player_bullets) < 2:
            self.enemy_bullets.append(bullet)
