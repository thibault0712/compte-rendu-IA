import matplotlib.pyplot as plt 

import numpy as np 

from matplotlib.widgets import Button, CheckButtons 

import time 

 

class Monde2D: 

def __init__(self, taille): 

self.taille = taille 

self.etats = np.random.choice([0, 1], size=(taille, taille)) # 0 = noir, 1 = blanc 

self.age = np.zeros((taille, taille), dtype=int) 

self.vie_max = np.random.randint(3, 6, size=(taille, taille)) 

 

self.compteur = 0 

self.play = False 

self.apocalypse_active = False 

self.esperance_vie_active = False 

self.gravite_active = False 

self.jeu_vie_active = False 

 

self.fig, self.ax = plt.subplots(figsize=(8, 8)) 

self.ax.set_xlim(0, taille) 

self.ax.set_ylim(0, taille) 

self.ax.set_aspect('equal') 

self.ax.axis('off') 

plt.title('Monde 2D') 

 

self.rects = [] 

for i in range(taille): 

for j in range(taille): 

rect = plt.Rectangle((j, taille - 1 - i), 1, 1, 

facecolor='white' if self.etats[i, j] else 'black', 

edgecolor='gray') 

self.ax.add_patch(rect) 

self.rects.append(rect) 

 

# Texte compteur 

self.text = self.ax.text(taille // 2, taille + 0.5, f'Temps : {self.compteur}', ha='center', fontsize=12) 

 

# Bouton Temps +1 

self.bouton_ax = plt.axes([0.7, 0.05, 0.2, 0.07]) 

self.bouton = Button(self.bouton_ax, 'Temps +1') 

self.bouton.on_clicked(self.incremente_temps) 

 

# Bouton Play 

self.play_ax = plt.axes([0.5, 0.05, 0.15, 0.07]) 

self.play_bouton = Button(self.play_ax, 'Play') 

self.play_bouton.on_clicked(self.toggle_play) 

 

# Checkboxes 

self.checkbox_ax = plt.axes([0.85, 0.6, 0.13, 0.25]) 

self.checkbox = CheckButtons(self.checkbox_ax, 

['Apocalypse', 'Espérance de vie', 'Gravité', 'Jeu de la vie'], 

[False, False, False, False]) 

self.checkbox.on_clicked(self.toggle_checkbox) 

 

self.fig.canvas.mpl_connect('button_press_event', self.clic_cellule) 

 

plt.show() 

 

def toggle_checkbox(self, label): 

if label == 'Apocalypse': 

self.apocalypse_active = not self.apocalypse_active 

elif label == 'Espérance de vie': 

self.esperance_vie_active = not self.esperance_vie_active 

elif label == 'Gravité': 

self.gravite_active = not self.gravite_active 

elif label == 'Jeu de la vie': 

self.jeu_vie_active = not self.jeu_vie_active 

 

def toggle_play(self, event): 

self.play = not self.play 

self.play_bouton.label.set_text('Stop' if self.play else 'Play') 

if self.play: 

while self.play: 

self.incremente_temps(None) 

plt.pause(0.3) 

 

def clic_cellule(self, event): 

if event.inaxes != self.ax: 

return 

x, y = int(event.xdata), int(event.ydata) 

i = self.taille - 1 - y 

j = x 

if 0 <= i < self.taille and 0 <= j < self.taille: 

self.etats[i, j] = 1 - self.etats[i, j] 

index = i * self.taille + j 

self.rects[index].set_facecolor('white' if self.etats[i, j] else 'black') 

self.fig.canvas.draw() 

 

def incremente_temps(self, event): 

self.compteur += 1 

self.text.set_text(f'Temps : {self.compteur}') 

 

if self.apocalypse_active: 

self.etats.fill(1) # Blanc 

self.age.fill(0) 

 

if self.jeu_vie_active: 

self.appliquer_jeu_vie() 

 

if self.esperance_vie_active: 

self.age += self.etats 

self.etats[self.age >= self.vie_max] = 0 

self.age[self.etats == 0] = 0 # Réinitialise âge 

 

if self.gravite_active: 

self.appliquer_gravite() 

 

# Met à jour l'affichage 

for i in range(self.taille): 

for j in range(self.taille): 

index = i * self.taille + j 

self.rects[index].set_facecolor('white' if self.etats[i, j] else 'black') 

self.fig.canvas.draw() 

 

def appliquer_jeu_vie(self): 

nouv_etats = self.etats.copy() 

for i in range(self.taille): 

for j in range(self.taille): 

voisins = self.nb_voisins(i, j) 

if self.etats[i, j] == 1: 

if voisins < 2 or voisins > 3: 

nouv_etats[i, j] = 0 

else: 

if voisins == 3: 

nouv_etats[i, j] = 1 

self.etats = nouv_etats 

 

def nb_voisins(self, i, j): 

voisins = 0 

for dx in [-1, 0, 1]: 

for dy in [-1, 0, 1]: 

if dx == 0 and dy == 0: 

continue 

ni, nj = i + dx, j + dy 

if 0 <= ni < self.taille and 0 <= nj < self.taille: 

voisins += self.etats[ni, nj] 

return voisins 

 

def appliquer_gravite(self): 

for j in range(self.taille): 

for i in range(self.taille - 2, -1, -1): 

if self.etats[i, j] == 1 and self.etats[i + 1, j] == 0: 

self.etats[i + 1, j] = 1 

self.etats[i, j] = 0 

self.age[i + 1, j] = self.age[i, j] 

self.age[i, j] = 0 

 

# Lancer le monde 

Monde2D(taille=10) 