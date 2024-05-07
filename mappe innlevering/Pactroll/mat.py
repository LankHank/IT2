from spillobjekt import Spillobjekt
from random import randint

class Mat(Spillobjekt):
    def __init__(self, farge: str) -> None:
        super().__init__(farge)
        self.x = randint(25, 575)
        self.y = randint(25, 575)

    def posisjon(self):
        self.plassering(self.x, self.y)
