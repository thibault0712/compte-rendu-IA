import pygame 

import random 

import sys 

 

# Configuration 

TAILLE_CASE = 20 

COLONNES = 40 

LIGNES = 30 

HAUTEUR_GRILLE = TAILLE_CASE * LIGNES 

HAUTEUR_TOTALE = HAUTEUR_GRILLE + 50 # pour le bouton 

LARGEUR = TAILLE_CASE * COLONNES 

 

# Couleurs 

NOIR = (0, 0, 0) 

BLANC = (255, 255, 255) 

GRIS = (200, 200, 200) 

BLEU = (70, 130, 180) 

 

def creer_monde_2d(): 

return [[random.choice([0, 1]) for _ in range(COLONNES)] for _ in range(LIGNES)] 

 

def afficher_monde(surface, monde): 

for y, ligne in enumerate(monde): 

for x, case in enumerate(ligne): 

couleur = NOIR if case == 1 else BLANC 

rect = pygame.Rect(x * TAILLE_CASE, y * TAILLE_CASE, TAILLE_CASE, TAILLE_CASE) 

pygame.draw.rect(surface, couleur, rect) 

pygame.draw.rect(surface, GRIS, rect, 1) 

 

def dessiner_bouton(surface, rect, texte): 

pygame.draw.rect(surface, BLEU, rect) 

pygame.draw.rect(surface, NOIR, rect, 2) 

font = pygame.font.SysFont(None, 30) 

text_surf = font.render(texte, True, BLANC) 

text_rect = text_surf.get_rect(center=rect.center) 

surface.blit(text_surf, text_rect) 

 

def main(): 

pygame.init() 

ecran = pygame.display.set_mode((LARGEUR, HAUTEUR_TOTALE)) 

pygame.display.set_caption("Monde 2D - Clic sur case + INIT") 

clock = pygame.time.Clock() 

 

monde = creer_monde_2d() 

 

bouton_rect = pygame.Rect((LARGEUR // 2) - 50, HAUTEUR_GRILLE + 10, 100, 30) 

 

running = True 

while running: 

clock.tick(30) 

for event in pygame.event.get(): 

if event.type == pygame.QUIT: 

running = False 

 

elif event.type == pygame.MOUSEBUTTONDOWN: 

if bouton_rect.collidepoint(event.pos): 

monde = creer_monde_2d() # Regénère 

else: 

# Clic dans la grille ? 

x, y = event.pos 

if y < HAUTEUR_GRILLE: 

case_x = x // TAILLE_CASE 

case_y = y // TAILLE_CASE 

# Inverse la couleur de la case cliquée 

monde[case_y][case_x] = 1 - monde[case_y][case_x] 

 

ecran.fill(BLANC) 

afficher_monde(ecran, monde) 

dessiner_bouton(ecran, bouton_rect, "INIT") 

pygame.display.flip() 

 

pygame.quit() 

sys.exit() 

 

if __name__ == "__main__": 

main() 