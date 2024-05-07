import pygame.freetype
from spillobjekt import Spillobjekt

class Troll(Spillobjekt):
    def __init__(self, farge: str) -> None:
        super().__init__(farge)
        self.poeng = 0
        self.font = pygame.freetype.SysFont("Consolas", 40)
        self.fart = 3

    def tegn_poeng(self, vindu: pygame.Surface):
        self.font.render_to(vindu, (40,40), f"{self.poeng}","white")

    