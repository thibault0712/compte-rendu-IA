from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg 

import tkinter as tk 

from tkinter import ttk 

 

class GameOfLifeApp: 

def __init__(self, root): 

self.root = root 

self.root.title("Game of Life") 

 

self.size = 10 

self.grid = np.zeros((self.size, self.size)) 

self.user_grid = np.zeros((self.size, self.size)) 

self.gravity = tk.BooleanVar() 

 

self.setup_ui() 

 

def setup_ui(self): 

# Frame pour les boutons et les cases à cocher 

control_frame = ttk.Frame(self.root) 

control_frame.pack(side=tk.LEFT, fill=tk.Y) 

 

# Case à cocher pour la gravité 

gravity_check = ttk.Checkbutton(control_frame, text="Gravité", variable=self.gravity) 

gravity_check.pack(pady=10) 

 

# Bouton pour initialiser la grille 

init_button = ttk.Button(control_frame, text="INIT", command=self.initialize_grid) 

init_button.pack(pady=10) 

 

# Bouton pour avancer dans le temps 

next_button = ttk.Button(control_frame, text="temp+1", command=self.next_step) 

next_button.pack(pady=10) 

 

# Frame pour les grilles 

grid_frame = ttk.Frame(self.root) 

grid_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True) 

 

# Création des figures et des canevas pour les grilles 

self.fig1, self.ax1 = plt.subplots() 

self.canvas1 = FigureCanvasTkAgg(self.fig1, master=grid_frame) 

self.canvas1.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH, expand=True) 

 

self.fig2, self.ax2 = plt.subplots() 

self.canvas2 = FigureCanvasTkAgg(self.fig2, master=grid_frame) 

self.canvas2.get_tk_widget().pack(side=tk.RIGHT, fill=tk.BOTH, expand=True) 

 

# Liaison de l'événement de clic sur la grille de l'utilisateur 

self.canvas2.mpl_connect("button_press_event", self.on_click) 

 

# Affichage initial des grilles 

self.update_grid_display() 

 

def initialize_grid(self): 

self.grid = np.random.choice([0, 1], size=(self.size, self.size), p=[0.5, 0.5]) 

self.update_grid_display() 

 

def next_step(self): 

new_grid = self.grid.copy() 

 

for i in range(self.size): 

for j in range(self.size): 

total = (self.grid[i, (j-1)%self.size] + self.grid[i, (j+1)%self.size] + 

self.grid[(i-1)%self.size, j] + self.grid[(i+1)%self.size, j] + 

self.grid[(i-1)%self.size, (j-1)%self.size] + self.grid[(i-1)%self.size, (j+1)%self.size] + 

self.grid[(i+1)%self.size, (j-1)%self.size] + self.grid[(i+1)%self.size, (j+1)%self.size]) 

 

if self.grid[i, j] == 1: 

if (total < 2) or (total > 3): 

new_grid[i, j] = 0 

else: 

if total == 3: 

new_grid[i, j] = 1 

 

if self.gravity.get(): 

new_grid = self.apply_gravity(new_grid) 

 

self.grid = new_grid 

self.update_grid_display() 

 

# Calcul des métriques 

VP, VN, FP, FN = self.calculate_metrics() 

precision, recall = self.calculate_precision_recall(VP, FP, FN) 

print(f"Vrais Positifs: {VP}, Vrais Négatifs: {VN}, Faux Positifs: {FP}, Faux Négatifs: {FN}") 

print(f"Précision: {precision:.2f}, Rappel: {recall:.2f}") 

 

def apply_gravity(self, grid): 

new_grid = grid.copy() 

moved = True 

while moved: 

moved = False 

for i in range(self.size - 1): 

for j in range(self.size): 

if grid[i, j] == 1 and grid[i + 1, j] == 0: 

new_grid[i, j] = 0 

new_grid[i + 1, j] = 1 

moved = True 

grid = new_grid.copy() 

return new_grid 

 

def on_click(self, event): 

if event.inaxes != self.ax2: 

return 

x, y = event.xdata, event.ydata 

if x is not None and y is not None: 

j, i = int(x), int(y) 

if 0 <= i < self.size and 0 <= j < self.size: 

self.user_grid[i, j] = 1 - self.user_grid[i, j] 

self.update_grid_display() 

 

def update_grid_display(self): 

self.ax1.clear() 

self.ax1.imshow(self.grid, cmap='binary', interpolation='nearest') 

self.ax1.set_title("Grille du jeu") 

self.canvas1.draw() 

 

self.ax2.clear() 

self.ax2.imshow(self.user_grid, cmap='binary', interpolation='nearest') 

self.ax2.set_title("Grille de l'utilisateur") 

self.canvas2.draw() 

 

def calculate_metrics(self): 

VP = np.sum((self.grid == 1) & (self.user_grid == 1)) 

VN = np.sum((self.grid == 0) & (self.user_grid == 0)) 

FP = np.sum((self.grid == 0) & (self.user_grid == 1)) 

FN = np.sum((self.grid == 1) & (self.user_grid == 0)) 

return VP, VN, FP, FN 

 

def calculate_precision_recall(self, VP, FP, FN): 

precision = VP / (VP + FP) if (VP + FP) > 0 else 0 

recall = VP / (VP + FN) if (VP + FN) > 0 else 0 

return precision, recall 

 

if __name__ == "__main__": 

root = tk.Tk() 

app = GameOfLifeApp(root) 

root.mainloop() 

 
