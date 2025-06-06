import numpy as np 

import matplotlib.pyplot as plt 

from matplotlib.widgets import Button, CheckButtons 

import matplotlib.gridspec as gridspec 

 

# Dimensions de la grille 

rows, cols = 10, 10 

 

# Grilles 

world = np.zeros((rows, cols), dtype=int) # Monde réel 

user_grid = np.zeros((rows, cols), dtype=int) # Grille utilisateur 

 

# Activation de la gravité 

gravity_enabled = [False] 

 

# Fonctions 

def init_world(event): 

global world, user_grid 

world = np.random.choice([0, 1], size=(rows, cols), p=[0.8, 0.2]) 

user_grid[:] = 0 

update_display() 

error_text.set_text("") 

 

def apply_gravity(grid): 

new_grid = np.zeros_like(grid) 

for col in range(cols): 

white_cells = [grid[row, col] for row in range(rows) if grid[row, col] == 1] 

for i in range(len(white_cells)): 

new_grid[rows - 1 - i, col] = 1 

return new_grid 

 

def on_temp(event): 

global world 

if gravity_enabled[0]: 

world = apply_gravity(world) 

update_display() 

 

# Calcul des métriques 

vp = np.sum((world == 1) & (user_grid == 1)) 

fp = np.sum((world == 0) & (user_grid == 1)) 

fn = np.sum((world == 1) & (user_grid == 0)) 

vn = np.sum((world == 0) & (user_grid == 0)) 

total_errors = fp + fn 

precision = vp / (vp + fp) if (vp + fp) > 0 else 0.0 

recall = vp / (vp + fn) if (vp + fn) > 0 else 0.0 

 

# Affichage clair 

result_str = ( 

f"Evaluation de votre prédiction\n" 

f"------------------------------\n" 

f"Vrais positifs (VP) : {vp}\n" 

f"Faux positifs (FP) : {fp}\n" 

f"Faux négatifs (FN) : {fn}\n" 

f"Vrais négatifs (VN) : {vn}\n" 

f"Total d’erreurs : {total_errors}\n" 

f"\n" 

f"Precision : {precision:.2f}\n" 

f"Rappel : {recall:.2f}" 

) 

error_text.set_text(result_str) 

fig.canvas.draw_idle() 

 

def update_display(): 

im1.set_data(world) 

im2.set_data(user_grid) 

fig.canvas.draw_idle() 

 

def on_click(event): 

if event.inaxes == ax_user and event.xdata is not None and event.ydata is not None: 

x, y = int(np.floor(event.xdata)), int(np.floor(event.ydata)) 

if 0 <= x < cols and 0 <= y < rows: 

user_grid[y, x] = 1 - user_grid[y, x] 

update_display() 

 

def on_gravity(label): 

gravity_enabled[0] = not gravity_enabled[0] 

 

# Interface graphique 

fig = plt.figure(figsize=(12, 8)) 

gs = gridspec.GridSpec(3, 3, figure=fig) 

 

ax_world = fig.add_subplot(gs[0:2, 1]) 

ax_user = fig.add_subplot(gs[0:2, 2]) 

ax_error = fig.add_subplot(gs[2, :]) 

ax_world.set_title("Grille réelle (temp)") 

ax_user.set_title("Prédiction utilisateur") 

ax_error.axis('off') 

 

# Affichage des grilles 

im1 = ax_world.imshow(world, cmap='gray_r', vmin=0, vmax=1) 

im2 = ax_user.imshow(user_grid, cmap='gray_r', vmin=0, vmax=1) 

 

# Texte d'évaluation 

error_text = ax_error.text(0.01, 0.95, "", fontsize=11, va='top', ha='left', family='monospace') 

 

# Boutons INIT et temp+1 

ax_init = plt.axes([0.4, 0.05, 0.1, 0.05]) 

btn_init = Button(ax_init, 'INIT') 

btn_init.on_clicked(init_world) 

 

ax_temp = plt.axes([0.52, 0.05, 0.1, 0.05]) 

btn_temp = Button(ax_temp, 'temp+1') 

btn_temp.on_clicked(on_temp) 

 

# Case à cocher pour gravité 

ax_check = plt.axes([0.05, 0.4, 0.15, 0.15]) 

check = CheckButtons(ax_check, ['Gravité'], [gravity_enabled[0]]) 

check.on_clicked(on_gravity) 

 

# Connexion du clic utilisateur 

fig.canvas.mpl_connect('button_press_event', on_click) 

 

plt.subplots_adjust(left=0.1, right=0.95, top=0.92, bottom=0.2, hspace=0.5) 

plt.show() 
