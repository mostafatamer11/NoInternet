import pygame as pg
import sys

from .player import Player
from .blocks import Block
from .scene import Scene


class Engine:
    def __init__(self, width, height, caption):
        pg.init()
        self.width = width
        self.height = height
        self.screen = pg.display.set_mode((width, height))
        pg.display.set_caption(caption)
        self.clock = pg.time.Clock()

        self.white = (255, 255, 255)

        self.player = Player(self.screen)

        self.tests = pg.sprite.Group()
        self.tests.add(Block(100, 200, 25, 25, (100, 100, 100)))
        self.scene = Scene()
        self.scene.run()

    def run(self):
        running = True
        while running:
            events = pg.event.get()
            for event in events:
                if event.type == pg.QUIT:
                    running = False

                self.player.update()

            self.tests.update(self.player.vel)

            for block in self.tests.sprites():
                if pg.sprite.collide_mask(self.player, block):
                    if self.player.vel.y > 0:
                        self.player.rect.top = block.rect.bottom
                    elif self.player.vel.y < 0:
                        self.player.rect.bottom = block.rect.top
                    elif self.player.vel.x < 0:
                        self.player.rect.right = block.rect.left
                    elif self.player.vel.x > 0:
                        self.player.rect.left = block.rect.right

            self.screen.fill((50, 100, 150))

            self.screen.blit(self.player.image, self.player.rect)
            self.tests.draw(self.screen)

            pg.display.flip()

            self.clock.tick(60)

        self.quit()

    def quit(self):
        pg.quit()
        sys.exit()
