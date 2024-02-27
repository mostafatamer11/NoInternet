import pygame as pg

# Set up the player class
class Player(pg.sprite.Sprite):
    def __init__(self, screen: pg.Surface):
        super().__init__()
        self.image = pg.Surface((100, 150))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.bottomleft = (screen.get_width() // 2, screen.get_height() // 2)
        self.vel = pg.Vector2(0, 0)
        self.speed = 5

    def update(self):
        keys = pg.key.get_pressed()

        self.vel.x = (keys[pg.K_RIGHT] - keys[pg.K_LEFT]) * self.speed
        self.vel.y = (keys[pg.K_DOWN] - keys[pg.K_UP]) * self.speed


