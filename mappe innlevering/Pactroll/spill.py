import pygame
from troll import Troll
from mat import Mat
from hindring import Hindring
 
# Oppsett av pygame
pygame.init()
BREDDE = 600 # bredde på vinduet
HOYDE = 600  # høyde på vinduet
vindu = pygame.display.set_mode((BREDDE, HOYDE))
klokke = pygame.time.Clock()
kjorer = True
dx = 0
dy = 0
matliste: list[Mat] = []
hindringliste: list[Hindring] = []

# OPPSETT AV SPILL HER:
troll = Troll("green")
troll.plassering(BREDDE/2, HOYDE/2)

for i in range(3):
    ny_mat = Mat("yellow")
    ny_mat.posisjon()
    matliste.append(ny_mat)



while kjorer:
    # fyll skjermen med en farge for å fjerne alt fra forrige frame
    vindu.fill("black")

    # gjør at trollet kan flytte seg
    troll.flytt(dx,dy)
    if troll.rect.right >= 600 or troll.rect.left <= 0:
            dx = 0
            dy = 0
    if troll.rect.top <= 0 or troll.rect.bottom >= 600:
            dx = 0
            dy = 0

    # Hendelser
    for hendelse in pygame.event.get():
        # pygame.QUIT hendelsen skjer når brukeren klikke på X for å lukke vinduet
        if hendelse.type == pygame.QUIT:
            kjorer = False

    for mat in matliste:
         if mat.rect.colliderect(troll.rect):
            dx,dy = 0,0
            
            ny_hindring = Hindring("grey")
            ny_hindring.plassering(mat.rect.centerx, mat.rect.centery)
            hindringliste.append(ny_hindring)

            matliste.remove(mat)
            ny_mat = Mat("yellow")
            ny_mat.posisjon()
            matliste.append(ny_mat)

            troll.poeng += 1

    for hindring in hindringliste:
        if hindring.rect.right == troll.rect.left or hindring.rect.left == troll.rect.right or hindring.rect.bottom == troll.rect.top or hindring.rect.top == hindring.rect.bottom:
            kjorer = False
            
 
    # Input fra tastatur:
    taster = pygame.key.get_pressed()
    if taster[pygame.K_UP]:
        dx = 0
        dy = -1 * troll.fart
    if taster[pygame.K_DOWN]:
        dx = 0
        dy = troll.fart
    if taster[pygame.K_RIGHT]:
        dx = troll.fart
        dy = 0
    if taster[pygame.K_LEFT]:
        dx = -1 * troll.fart
        dy = 0
    if taster[pygame.K_ESCAPE]:
        kjorer = False
 
    # Input fra mus:
    mus_posisjon = pygame.mouse.get_pos()
    mus_klikk = pygame.mouse.get_pressed()
    if mus_klikk[0]:
        print(f"Venstre klikk i posisjon {mus_posisjon}")
    if mus_klikk[1]:
        print(f"Hjul-klikk i posisjon {mus_posisjon}")
    if mus_klikk[2]:
        print(f"Høyreklikk i posisjon {mus_posisjon}")
 
    # Oppdater spill her:
 
 
    # Tegn på skjermen her:)
    troll.tegn(vindu)
    troll.tegn_poeng(vindu)
    for mat in matliste:
        mat.tegn(vindu)
    for hindring in hindringliste:
         hindring.tegn(vindu)

    # flip() oppdater vinduet med alle endringer
    pygame.display.flip()
 
    # klokke.tick(60) begrenser spillet til 60 FPS (frames per second)
    klokke.tick(60) 
 
pygame.quit()