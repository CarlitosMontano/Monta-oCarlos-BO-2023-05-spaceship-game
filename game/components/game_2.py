import pygame

from game.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, FONT_STYLE

class Game_2:
    def __init__(self, screen):
        self.screen = screen
        self.last_score = 0

    def draw_score(self, score):
        font = pygame.font.Font(FONT_STYLE, 30)
        text = font.render(f'Score: {score}', False, 'White')
        text_rect = text.get_rect(topright = (SCREEN_WIDTH - 30, 30))
        self.screen.blit(text, text_rect)

    def show_score(self, score):
        font = pygame.font.Font(FONT_STYLE, 20)
        text = font.render(f"Your Score: {score}", False, ('Black'))
        text_rect = text.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 50))
        self.screen.blit(text, text_rect)

    def show_death_score(self, score):
        font = pygame.font.Font(FONT_STYLE, 20)
        text = font.render(f"Death Score: {score}", False, ('Black'))
        text_rect = text.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 70))
        self.screen.blit(text, text_rect)

    def show_highest_score(self, score):
        font = pygame.font.Font(FONT_STYLE, 20)
        text = font.render(f"Highest Score: {score}", False, ('Black'))
        text_rect = text.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 90))
        self.screen.blit(text, text_rect)