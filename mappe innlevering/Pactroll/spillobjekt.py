import pygame

class Spillobjekt:
    def __init__(self, farge: str) -> None:
        self.surface = pygame.Surface((50, 50)) # Lager et pygamesurface som er 50px høyt og bredt
        self.rect = self.surface.get_rect() # lager en rect som ligger rundt surface-en
        self.surface.fill(farge)

    def plassering(self, x: int, y: int):
        self.rect.center = (x, y)

    def flytt(self, dx: int, dy: int):
        self.rect.move_ip(dx, dy)

    def tegn(self, vindu: pygame.Surface):
        vindu.blit(self.surface, self.rect )