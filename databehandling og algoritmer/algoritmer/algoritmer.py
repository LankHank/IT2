liste = []

# Høyeste tall i en liste
def høyeste(liste: list[int]):
    høyest = liste[0]
    for tall in liste:
        if tall > høyest:
            høyest = tall
    return høyest

# Gjennomsnitt av liste
def gjennomsnitt(liste: list[int]):
    total = 0
    antall = 0
    for tall in liste:
        total += tall
        antall += 1
    return total/antall

# Nest høyest i en liste
def nest_høyest(liste: list[int]):
    høyest = float("-inf")
    nest_høyest = float("-inf")
    for tall in liste:
        if tall > høyest:
            nest_høyest = høyest
            høyest = tall
        elif tall > nest_høyest:
            nest_høyest = tall
    return nest_høyest  

def n_høyest(liste: list[int], n):
    høyeste_n = []
    for i in range(0, n):
        høyest = høyeste(liste)
        liste.remove(høyest)
        høyeste_n.append(høyest)
    return høyeste_n

def n_høyest_alt(liste:list[int], n: int):
    liste.sort(reverse=True)
    return liste[:n]





