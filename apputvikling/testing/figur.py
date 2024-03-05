class Figur:
    def __init__(self, x: int, y: int) -> None:
        self.x: int = x
        self.y: int = y

    def __str__(self) -> str:
        return f"({self.x}, {self.y})"
    
class Trekant():
    def __init__(self, grunnlinje: int, høyde: int) -> None:
        self.grunnlinje: int = grunnlinje
        self.høyde: int = høyde

    def areal(self):
        return (self.grunnlinje * self.høyde) / 2
    
if __name__ == "__main__":
    print("Testing")

    min_figur = Figur(10,20)
    print(min_figur)