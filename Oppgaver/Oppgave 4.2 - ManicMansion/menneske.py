from spillobjekt import Spillobjekt

class Menneske(Spillobjekt):
    def __init__(self, x, y) -> None:
        super().__init__(x, y)
        self.fart_x: int = 0
        self.fart_y: int = 0
        self.poeng: int
        self.baerer_sau: bool
        self.plassering(75, 300)
        self.surface.fill("green")
    
    def beveg(self):
        if self.baerer_sau:
            self.flytt(self.fart_x*0.8, self.fart_y*0.8)
        else: 
            self.flytt(self.fart_x, self.fart_y)

