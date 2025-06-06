import matplotlib.pyplot as plt 

import numpy as np 

from matplotlib.widgets import Button, CheckButtons 

import time 

import threading 

 

TAILLE = 10 # Grille 10x10 

 

 

class Monde2D: 

def __init__(self, taille): 

self.taille = taille 

self.etats = np.random.randint(0, 2, (taille, taille)) # 0 = noir, 1 = blanc 

self.temps = 0 

 

self.play_active = False 

self.afficher_grille = False 

self.apocalypse_active = False 

self.gravite_active = False 

self.esperance_vie_active = False 

 

self.fig, self.ax = plt.subplots(figsize=(6, 6)) 

self.fig.subplots_adjust(left=0.05, right=0.7) 

self.ax.set_xlim(0, taille) 

self.ax.set_ylim(0, taille) 

self.ax.set_aspect('equal') 

self.ax.axis('off') 

 

self.patches = [] 

for i in range(taille): 

ligne = [] 

for j in range(taille): 

rect = plt.Rectangle((j, taille - 1 - i), 1, 1, 

facecolor='white' if self.etats[i, j] else 'black', 

edgecolor='none') 

self.ax.add_patch(rect) 

ligne.append(rect) 

self.patches.append(ligne) 

 

self.text_temps = self.ax.text(taille / 2, taille + 0.3, 

f'Temps : {self.temps}', 

ha='center', fontsize=12) 

 

ax_btn1 = plt.axes([0.75, 0.7, 0.2, 0.08]) 

self.btn_temps = Button(ax_btn1, 'Temps +1') 

self.btn_temps.on_clicked(self.incremente_temps) 

 

ax_btn2 = plt.axes([0.75, 0.6, 0.2, 0.08]) 

self.btn_play = Button(ax_btn2, 'Play') 

self.btn_play.on_clicked(self.toggle_play) 

 

ax_check = plt.axes([0.75, 0.25, 0.2, 0.3]) 

self.check = CheckButtons(ax_check, 

['Afficher quadrillage', 'Apocalypse', 

'Gravité', 'Espérance de vie'], 

[False, False, False, False]) 

self.check.on_clicked(self.toggle_option) 

 

self.fig.canvas.mpl_connect('button_press_event', self.on_click) 

 

plt.show() 

 

def on_click(self, event): 

if event.inaxes != self.ax: 

return 

x, y = int(event.xdata), int(event.ydata) 

i, j = self.taille - 1 - y, x 

if 0 <= i < self.taille and 0 <= j < self.taille: 

self.etats[i, j] = 1 - self.etats[i, j] 

self.maj_cellule(i, j) 

self.fig.canvas.draw_idle() 

 

def maj_cellule(self, i, j): 

couleur = 'white' if self.etats[i, j] == 1 else 'black' 

bordure = 'gray' if self.afficher_grille else 'none' 

self.patches[i][j].set_facecolor(couleur) 

self.patches[i][j].set_edgecolor(bordure) 

 

def incremente_temps(self, event=None): 

self.temps += 1 

self.text_temps.set_text(f'Temps : {self.temps}') 

 

if self.apocalypse_active: 

self.etats.fill(0) 

 

if self.gravite_active: 

for j in range(self.taille): 

colonne = self.etats[:, j] 

blancs = colonne[colonne == 1] 

nouveaux = np.zeros(self.taille, dtype=int) 

nouveaux[-len(blancs):] = 1 

self.etats[:, j] = nouveaux 

 

if self.esperance_vie_active: 

prob = np.random.rand(*self.etats.shape) 

self.etats = np.where((self.etats == 1) & (prob < 0.1), 0, self.etats) 

 

for i in range(self.taille): 

for j in range(self.taille): 

self.maj_cellule(i, j) 

self.fig.canvas.draw_idle() 

 

def toggle_play(self, event=None): 

self.play_active = not self.play_active 

self.btn_play.label.set_text('Stop' if self.play_active else 'Play') 

if self.play_active: 

threading.Thread(target=self.auto_increment, daemon=True).start() 

 

def auto_increment(self): 

while self.play_active: 

time.sleep(0.5) 

self.incremente_temps() 

 

def toggle_option(self, label): 

if label == 'Afficher quadrillage': 

self.afficher_grille = not self.afficher_grille 

elif label == 'Apocalypse': 

self.apocalypse_active = not self.apocalypse_active 

elif label == 'Gravité': 

self.gravite_active = not self.gravite_active 

elif label == 'Espérance de vie': 

self.esperance_vie_active = not self.esperance_vie_active 

 

for i in range(self.taille): 

for j in range(self.taille): 

self.maj_cellule(i, j) 

self.fig.canvas.draw_idle() 

 

 

if __name__ == "__main__": 

Monde2D(TAILLE) 

 