import matplotlib.pyplot as plt 

import numpy as np 

from matplotlib.widgets import Button, CheckButtons 

 

class Monde2D: 

def __init__(self, largeur, hauteur): 

self.largeur = largeur 

self.hauteur = hauteur 

self.cases = np.random.choice([True, False], size=(hauteur, largeur)) 

self.age_cases = np.zeros((hauteur, largeur), dtype=int) 

self.life_expectancy = np.zeros((hauteur, largeur), dtype=int) 

self.compteur = 0 

self.apocalypse_active = False 

self.esperance_vie_active = False 

self.gravite_active = False 

 

self.fig = plt.figure(figsize=(12, 10)) 

self.ax = self.fig.add_subplot(111) 

 

# Dessiner les cases 

self.patches = [] 

for i in range(self.hauteur): 

for j in range(self.largeur): 

rect = plt.Rectangle((j, i), 1, 1, facecolor='white' if not self.cases[i, j] else 'black', edgecolor='grey') 

self.ax.add_patch(rect) 

self.patches.append(rect) 

 

self.ax.set_xlim(0, self.largeur) 

self.ax.set_ylim(0, self.hauteur) 

self.ax.set_aspect('equal') 

self.ax.axis('off') 

plt.title('Monde à deux dimensions') 

 

# Ajouter un bouton pour incrémenter le compteur 

ax_button = plt.axes([0.7, 0.05, 0.2, 0.075]) 

self.button = Button(ax_button, 'Temps +1') 

self.button.on_clicked(self.incrementer_compteur) 

 

# Ajouter des cases à cocher pour les options 

ax_checkbox = plt.axes([0.85, 0.7, 0.1, 0.25]) 

self.check = CheckButtons(ax_checkbox, ['Apocalypse', 'Espérance de vie', 'Gravité'], [False, False, False]) 

self.check.on_clicked(self.toggle_options) 

 

# Afficher le compteur 

self.text_compteur = self.ax.text(0.5, self.hauteur + 0.5, f'Temps: {self.compteur}', fontsize=12, ha='center') 

 

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

if self.cases[y_click, x_click]: 

self.age_cases[y_click, x_click] = 0 

self.life_expectancy[y_click, x_click] = np.random.randint(3, 6) # Espérance de vie aléatoire entre 3 et 5 

index = y_click * self.largeur + x_click 

if self.cases[y_click, x_click]: 

self.patches[index].set_facecolor('black') 

else: 

self.patches[index].set_facecolor('white') 

self.fig.canvas.draw() 

 

def toggle_options(self, label): 

if label == 'Apocalypse': 

self.apocalypse_active = not self.apocalypse_active 

elif label == 'Espérance de vie': 

self.esperance_vie_active = not self.esperance_vie_active 

elif label == 'Gravité': 

self.gravite_active = not self.gravite_active 

 

def incrementer_compteur(self, event): 

self.compteur += 1 

self.text_compteur.set_text(f'Temps: {self.compteur}') 

 

if self.apocalypse_active: 

self.apocalypse() 

 

if self.esperance_vie_active: 

self.tuer_cases_vieillissantes() 

 

if self.gravite_active: 

self.appliquer_gravite() 

 

self.fig.canvas.draw() 

 

def appliquer_gravite(self): 

for i in range(self.hauteur - 1): 

for j in range(self.largeur): 

if not self.cases[i, j] and self.cases[i + 1, j]: 

self.cases[i, j] = True 

self.cases[i + 1, j] = False 

self.age_cases[i, j] = self.age_cases[i + 1, j] 

self.life_expectancy[i, j] = self.life_expectancy[i + 1, j] 

self.age_cases[i + 1, j] = 0 

self.life_expectancy[i + 1, j] = 0 

index1 = i * self.largeur + j 

index2 = (i + 1) * self.largeur + j 

self.patches[index1].set_facecolor('black') 

self.patches[index2].set_facecolor('white') 

 

def apocalypse(self): 

self.cases.fill(False) 

self.age_cases.fill(0) 

for patch in self.patches: 

patch.set_facecolor('white') 

 

def tuer_cases_vieillissantes(self): 

for i in range(self.hauteur): 

for j in range(self.largeur): 

if self.cases[i, j]: 

self.age_cases[i, j] += 1 

if self.age_cases[i, j] >= self.life_expectancy[i, j]: 

self.cases[i, j] = False 

index = i * self.largeur + j 

self.patches[index].set_facecolor('white') 

 

# Exemple d'utilisation 

largeur_monde = 10 

hauteur_monde = 10 

monde = Monde2D(largeur_monde, hauteur_monde) 

 

 

 