from game.utils.constants import HEART


class Heart():
    def __init__(self):
        self.image = HEART
        self.count = 3 # para que dibuje 3 corazones

    def delete_heart(self):
        self.count -= 1

    def draw(self, screen):
        heart_x = 20
        heart_y = 20
        for index in range (self.count):
            screen.blit(self.image, (heart_x, heart_y))
            heart_x += 50