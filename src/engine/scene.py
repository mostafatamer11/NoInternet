import pygame as pg


class Scene:
    def __init__(self):
        self.running = True

    def run(self):
        while self.running:
            for event in pg.event.get():
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        print("hi")
                        self.running = False