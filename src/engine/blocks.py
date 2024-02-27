import pygame as pg


class Block(pg.sprite.Sprite):
    def __init__(self, x, y, width, height, color):
        super().__init__()
        self.image = pg.Surface((width, height))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.mask = pg.mask.from_surface(self.image)

    def update(self, vel: pg.Vector2) -> None:
        self.rect.center += vel