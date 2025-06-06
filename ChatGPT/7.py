import numpy as np 

import matplotlib.pyplot as plt 

from matplotlib.widgets import Button, CheckButtons 

 

# Paramètres de la grille 

rows, cols = 10, 10 

 

# État initial 

world = np.zeros((rows, cols), dtype=int) # Grille réelle 

user_grid = np.zeros((rows, cols), dtype=int) # Grille utilisateur 

gravity_enabled = [False] # Booléen dans une liste pour être mutable dans les callbacks 

 

def apply_gravity(grid): 

new_grid = grid.copy() 

for col in range(cols): 

for row in range(rows - 2, -1, -1): # partir du bas -1 

if grid[row, col] == 1 and grid[row + 1, col] == 0: 

new_grid[row, col] = 0 

new_grid[row + 1, col] = 1 

return new_grid 

 

# === Affichage des grilles === 

fig, axes = plt.subplots(1, 2, figsize=(10, 5)) 

plt.subplots_adjust(left=0.25, bottom=0.25) 

 

ax_real, ax_user = axes 

img_real = ax_real.imshow(world, cmap='gray', vmin=0, vmax=1) 

img_user = ax_user.imshow(user_grid, cmap='gray', vmin=0, vmax=1) 

ax_real.set_title("Grille réelle") 

ax_user.set_title("Votre prédiction") 

for ax in axes: 

ax.set_xticks([]) 

ax.set_yticks([]) 

 

# === Boutons === 

ax_init = plt.axes([0.4, 0.05, 0.1, 0.075]) 

btn_init = Button(ax_init, 'INIT') 

 

ax_temp = plt.axes([0.52, 0.05, 0.1, 0.075]) 

btn_temp = Button(ax_temp, 'temp+1') 

 

# === Case à cocher Gravité === 

ax_check = plt.axes([0.05, 0.6, 0.15, 0.15]) 

chkbox = CheckButtons(ax_check, ['Gravité'], [False]) 

 

# === Affichage des erreurs === 

ax_error = plt.axes([0.4, 0.85, 0.4, 0.1]) 

error_text = ax_error.text(0.5, 0.5, "", ha='center', va='center', fontsize=12) 

ax_error.axis('off') 

 

def update_display(): 

img_real.set_data(world) 

img_user.set_data(user_grid) 

fig.canvas.draw_idle() 

 

def on_init(event): 

global world, user_grid 

world = np.random.choice([0, 1], size=(rows, cols)) 

user_grid = np.zeros((rows, cols), dtype=int) 

error_text.set_text("") 

update_display() 

 

def on_temp(event): 

global world 

if gravity_enabled[0]: 

world = apply_gravity(world) 

else: 

# Si tu veux un vrai "jeu de la vie", insère les règles ici 

pass 

update_display() 

# Calcul des erreurs 

errors = np.sum(np.abs(world - user_grid)) 

error_text.set_text(f"Nombre d'erreurs : {errors}") 

 

def on_gravity(label): 

gravity_enabled[0] = not gravity_enabled[0] 

 

def on_click(event): 

if event.inaxes == ax_user: 

x, y = int(event.xdata), int(event.ydata) 

user_grid[y, x] = 1 - user_grid[y, x] # Toggle entre 0 et 1 

update_display() 

 

# Connexion des événements 

btn_init.on_clicked(on_init) 

btn_temp.on_clicked(on_temp) 

chkbox.on_clicked(on_gravity) 

fig.canvas.mpl_connect('button_press_event', on_click) 

 

plt.show() 