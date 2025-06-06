import matplotlib.pyplot as plt 

import matplotlib.patches as patches 

 

class Monde1D: 

def __init__(self, taille): 

self.taille = taille 

self.cases = ['blanc'] * taille # Initialise toutes les cases à blanches 

 

def afficher(self): 

fig, ax = plt.subplots(figsize=(10, 2)) 

 

for i, couleur in enumerate(self.cases): 

rect = patches.Rectangle((i, 0), 1, 1, facecolor='black' if couleur == 'noir' else 'white', edgecolor='grey') 

ax.add_patch(rect) 

 

ax.set_xlim(0, self.taille) 

ax.set_ylim(0, 1) 

ax.set_aspect('equal') 

ax.axis('off') # Cache les axes 

plt.title('Monde à une dimension') 

plt.show() 

 

def colorier_case(self, index, couleur): 

if index < 0 or index >= self.taille: 

print("Index hors limites") 

return 

self.cases[index] = couleur 

 

# Exemple d'utilisation 

taille_monde = 20 

monde = Monde1D(taille_monde) 

 

# Colorier quelques cases en noir 

monde.colorier_case(2, 'noir') 

monde.colorier_case(5, 'noir') 

monde.colorier_case(8, 'noir') 

monde.colorier_case(10, 'noir') 

monde.colorier_case(15, 'noir') 

 

# Afficher le monde 

monde.afficher() 