import pygame
from spillobjekt import Spillobjekt
from menneske import Menneske

class Spillebrett:
    def __init__(self, hoyde, bredde) -> None:
        self.hoyde:int = hoyde
        self.bredde:int = bredde
        self.objekter: list[Spillobjekt] = []

        # Alle "ting" i pygame må ha en surface og en rect
        self.surface = pygame.Surface((self.bredde, self.hoyde))
        self.rect = self.surface.get_rect()

        # Plasserer spillbrettet i (x, y)
        self.rect.topleft = (0, 0)

        self.surface.fill("white")

        self.spiller1 = Menneske() # Oppretter en spiller som er et menneske

    def legg_til_objekt(self, nytt_objekt: Spillobjekt):
        # legg til nytt spillobjekt i listen self.objekter
        self.objekter.append(nytt_objekt)

    def fjern_objekt(self, objekt: Spillobjekt):
        # fjerner spillobjekt fra listen self.objekter
        self.objekter.remove(objekt)

    def tegn(self, vindu: pygame.Surface):
        # tegner spillbrettets surface i posisjonen til spillbrettets rect på vinduet
        vindu.blit(self.surface, self.rect)
        self.spiller1.tegn(self.surface )