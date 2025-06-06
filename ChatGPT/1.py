import pygame 

import random 

import sys 

 

# Configuration 

LARGEUR = 800 

HAUTEUR = 100 

TAILLE_CASE = 20 

COLONNES = LARGEUR // TAILLE_CASE 

 

def creer_ligne(): 

# Génère une seule ligne aléatoire de 0 (blanc) et 1 (noir) 

return [random.choice([0, 1]) for _ in range(COLONNES)] 

 

def afficher_ligne(surface, ligne): 

for i, case in enumerate(ligne): 

couleur = (0, 0, 0) if case == 1 else (255, 255, 255) 

rect = pygame.Rect(i * TAILLE_CASE, 0, TAILLE_CASE, TAILLE_CASE) 

pygame.draw.rect(surface, couleur, rect) 

pygame.draw.rect(surface, (200, 200, 200), rect, 1) # bordures grises 

 

def main(): 

pygame.init() 

ecran = pygame.display.set_mode((LARGEUR, HAUTEUR)) 

pygame.display.set_caption("Monde 1D - Ligne Statique") 

clock = pygame.time.Clock() 

 

ligne = creer_ligne() # Une seule fois au lancement 

 

running = True 

while running: 

clock.tick(30) # 30 FPS pour fluidité (utile si on ajoute interaction plus tard) 

for event in pygame.event.get(): 

if event.type == pygame.QUIT: 

running = False 

 

ecran.fill((255, 255, 255)) 

afficher_ligne(ecran, ligne) 

pygame.display.flip() 

 

pygame.quit() 

sys.exit() 

 

if __name__ == "__main__": 

main() 