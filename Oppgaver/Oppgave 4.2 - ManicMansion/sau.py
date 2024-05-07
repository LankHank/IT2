import random
from spillobjekt import Spillobjekt

class Sau(Spillobjekt):
    def __init__(self) -> None:
        super().__init__("grey")
        self.blebaeret: bool = False
        tilfeldig_y = random.randint(50, 550)
        self.plassering(525,tilfeldig_y)

    