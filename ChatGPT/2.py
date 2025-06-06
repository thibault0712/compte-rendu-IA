import pygame 

import random 

import sys 

 

# Configuration 

LARGEUR = 800 

HAUTEUR = 150 

TAILLE_CASE = 20 

COLONNES = LARGEUR // TAILLE_CASE 

HAUTEUR_LIGNE = 100 

 

# Couleurs 

NOIR = (0, 0, 0) 

BLANC = (255, 255, 255) 

GRIS = (200, 200, 200) 

BLEU = (70, 130, 180) 

 

def creer_ligne(): 

return [random.choice([0, 1]) for _ in range(COLONNES)] 

 

def inverser_ligne(ligne): 

return [1 - case for case in ligne] 

 

def afficher_ligne(surface, ligne): 

for i, case in enumerate(ligne): 

couleur = NOIR if case == 1 else BLANC 

rect = pygame.Rect(i * TAILLE_CASE, 0, TAILLE_CASE, TAILLE_CASE) 

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

ecran = pygame.display.set_mode((LARGEUR, HAUTEUR)) 

pygame.display.set_caption("Monde 1D - Interactif") 

clock = pygame.time.Clock() 

 

ligne = creer_ligne() 

 

# Définition du bouton INIT 

bouton_rect = pygame.Rect((LARGEUR // 2) - 50, HAUTEUR_LIGNE + 10, 100, 30) 

 

running = True 

while running: 

clock.tick(30) 

for event in pygame.event.get(): 

if event.type == pygame.QUIT: 

running = False 

 

elif event.type == pygame.MOUSEBUTTONDOWN: 

x, y = event.pos 

if bouton_rect.collidepoint(x, y): 

ligne = inverser_ligne(ligne) 

elif y < TAILLE_CASE: 

index = x // TAILLE_CASE 

if 0 <= index < len(ligne): 

ligne[index] = 1 - ligne[index] 

 

ecran.fill(BLANC) 

afficher_ligne(ecran, ligne) 

dessiner_bouton(ecran, bouton_rect, "INIT") 

pygame.display.flip() 

 

pygame.quit() 

sys.exit() 

 

if __name__ == "__main__": 

main() 

 