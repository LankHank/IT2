from spillobjekt import Spillobjekt

class Hindring(Spillobjekt):
    def __init__(self, x: int, y: int) -> None:
        super().__init__(x, y)