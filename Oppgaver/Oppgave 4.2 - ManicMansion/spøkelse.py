from spillobjekt import Spillobjekt

class Spokelse(Spillobjekt):
    def __init__(self, x: int, y: int) -> None:
        super().__init__(x, y)

    def endre_retning(self):
        pass