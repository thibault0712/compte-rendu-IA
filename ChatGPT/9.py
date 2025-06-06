class TuringMachine: 

def __init__(self, tape, transitions, initial_state, blank_symbol='□', final_states=None): 

self.tape = list(tape) 

self.head = 0 

self.state = initial_state 

self.blank_symbol = blank_symbol 

self.transitions = transitions 

self.final_states = final_states if final_states else set() 

 

def step(self): 

# Lire le symbole actuel (ou blank) 

if self.head >= len(self.tape): 

self.tape.append(self.blank_symbol) 

 

current_symbol = self.tape[self.head] 

key = (self.state, current_symbol) 

 

if key not in self.transitions: 

return False # Pas de transition → arrêt 

 

new_symbol, direction, next_state = self.transitions[key] 

 

# Écriture 

self.tape[self.head] = new_symbol 

 

# Déplacement 

if direction == 'R': 

self.head += 1 

if self.head >= len(self.tape): 

self.tape.append(self.blank_symbol) 

elif direction == 'L': 

if self.head > 0: 

self.head -= 1 

 

# Changement d’état 

self.state = next_state 

return True 

 

def run(self, max_steps=100): 

steps = 0 

while self.state not in self.final_states and steps < max_steps: 

self.print_tape() 

if not self.step(): 

break 

steps += 1 

self.print_tape() 

print("Final state:", self.state) 

 

def print_tape(self): 

tape_str = ''.join(self.tape) 

head_str = ' ' * self.head + '^' 

print(tape_str) 

print(head_str) 

 

 

# Exemple : incrémenter un nombre binaire (ex: 111 → 1000) 

initial_tape = list("111") # nombre 7 en binaire 

transitions = { 

('start', '1'): ('1', 'R', 'start'), 

('start', '0'): ('0', 'R', 'start'), 

('start', '□'): ('□', 'L', 'check'), 

 

('check', '1'): ('0', 'L', 'check'), 

('check', '0'): ('1', 'R', 'end'), 

('check', '□'): ('1', 'R', 'end'), # cas où tous les bits sont 1 

} 

final_states = {'end'} 

 

tm = TuringMachine(initial_tape, transitions, initial_state='start', final_states=final_states) 

tm.run() 
