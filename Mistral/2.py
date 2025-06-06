import matplotlib.pyplot as plt 

import matplotlib.patches as patches 

from matplotlib.widgets import Button 

 

class Monde1D: 

def __init__(self, taille): 

self.taille = taille 

self.cases = ['blanc'] * taille # Initialise toutes les cases à blanches 

self.fig, self.ax = plt.subplots(figsize=(10, 3)) 

self.patches = [] 

 

# Dessiner les cases 

for i in range(self.taille): 

rect = patches.Rectangle((i, 0), 1, 1, facecolor='white', edgecolor='grey') 

self.ax.add_patch(rect) 

self.patches.append(rect) 

 

self.ax.set_xlim(0, self.taille) 

self.ax.set_ylim(0, 1) 

self.ax.set_aspect('equal') 

self.ax.axis('off') # Cache les axes 

plt.title('Monde à une dimension') 

 

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

if 0 <= x_click < self.taille: 

if self.cases[x_click] == 'blanc': 

self.cases[x_click] = 'noir' 

self.patches[x_click].set_facecolor('black') 

else: 

self.cases[x_click] = 'blanc' 

self.patches[x_click].set_facecolor('white') 

self.fig.canvas.draw() 

 

def inverser_couleurs(self, event): 

for i in range(self.taille): 

if self.cases[i] == 'blanc': 

self.cases[i] = 'noir' 

self.patches[i].set_facecolor('black') 

else: 

self.cases[i] = 'blanc' 

self.patches[i].set_facecolor('white') 

self.fig.canvas.draw() 

 

# Exemple d'utilisation 

taille_monde = 20 

monde = Monde1D(taille_monde) 

 

# Colorier quelques cases en noir 

monde.cases[2] = 'noir' 

monde.patches[2].set_facecolor('black') 

monde.cases[5] = 'noir' 

monde.patches[5].set_facecolor('black') 

monde.cases[8] = 'noir' 

monde.patches[8].set_facecolor('black') 

monde.cases[10] = 'noir' 

monde.patches[10].set_facecolor('black') 

monde.cases[15] = 'noir' 

monde.patches[15].set_facecolor('black') 