import matplotlib.pyplot as plt 

import matplotlib.patches as patches 

from matplotlib.widgets import Button 

import numpy as np 

 

class Monde2D: 

def __init__(self, largeur, hauteur): 

self.largeur = largeur 

self.hauteur = hauteur 

self.cases = np.zeros((hauteur, largeur), dtype=bool) # Initialise toutes les cases à blanches (False) 

 

self.fig, self.ax = plt.subplots(figsize=(10, 10)) 

self.patches = [] 

 

# Dessiner les cases 

for i in range(self.hauteur): 

for j in range(self.largeur): 

rect = patches.Rectangle((j, i), 1, 1, facecolor='white', edgecolor='grey') 

self.ax.add_patch(rect) 

self.patches.append(rect) 

 

self.ax.set_xlim(0, self.largeur) 

self.ax.set_ylim(0, self.hauteur) 

self.ax.set_aspect('equal') 

self.ax.axis('off') # Cache les axes 

plt.title('Monde à deux dimensions') 

 

# Ajouter un bouton 

ax_button = plt.axes([0.4, 0.05, 0.2, 0.075]) 

self.button = Button(ax_button, 'Init') 

self.button.on_clicked(self.inverser_couleurs) 

 

# Connecter l'événement de clic 

self.fig.canvas.mpl_connect('button_press_event', self.on_click) 

 

plt.show() 

 

def on_click(self, event): 

if event.inaxes != self.ax: 

return 

x_click = int(event.xdata) 

y_click = int(event.ydata) 

if 0 <= x_click < self.largeur and 0 <= y_click < self.hauteur: 

self.cases[y_click, x_click] = not self.cases[y_click, x_click] 

index = y_click * self.largeur + x_click 

if self.cases[y_click, x_click]: 

self.patches[index].set_facecolor('black') 

else: 

self.patches[index].set_facecolor('white') 

self.fig.canvas.draw() 

 

def inverser_couleurs(self, event): 

for i in range(self.hauteur): 

for j in range(self.largeur): 

self.cases[i, j] = not self.cases[i, j] 

index = i * self.largeur + j 

if self.cases[i, j]: 

self.patches[index].set_facecolor('black') 

else: 

self.patches[index].set_facecolor('white') 

self.fig.canvas.draw() 

 

# Exemple d'utilisation 

largeur_monde = 10 

hauteur_monde = 10 

monde = Monde2D(largeur_monde, hauteur_monde) 