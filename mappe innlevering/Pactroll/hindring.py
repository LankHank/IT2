from spillobjekt import Spillobjekt

class Hindring(Spillobjekt):
    def __init__(self, farge: str) -> None:
        super().__init__(farge)