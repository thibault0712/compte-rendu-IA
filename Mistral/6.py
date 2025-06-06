class TuringMachine: 

def __init__(self, tape, initial_state, final_states, transition_function): 

self.tape = list(tape) 

self.head_position = 0 

self.current_state = initial_state 

self.final_states = final_states 

self.transition_function = transition_function 

 

def step(self): 

if self.current_state in self.final_states: 

return False 

 

current_symbol = self.tape[self.head_position] 

action = self.transition_function.get((self.current_state, current_symbol)) 

 

if action is None: 

return False 

 

new_state, new_symbol, direction = action 

 

self.tape[self.head_position] = new_symbol 

self.current_state = new_state 

 

if direction == 'R': 

self.head_position += 1 

elif direction == 'L': 

self.head_position -= 1 

 

if self.head_position < 0: 

self.tape.insert(0, '_') 

self.head_position = 0 

elif self.head_position >= len(self.tape): 

self.tape.append('_') 

 

return True 

 

def run(self): 

while self.step(): 

pass 

return ''.join(self.tape) 

 

# Exemple d'utilisation 

tape = "1011_" 

initial_state = "q0" 

final_states = {"q3"} 

 

transition_function = { 

("q0", "1"): ("q0", "1", "R"), 

("q0", "0"): ("q0", "0", "R"), 

("q0", "_"): ("q1", "_", "L"), 

("q1", "1"): ("q2", "0", "L"), 

("q1", "0"): ("q2", "1", "L"), 

("q1", "_"): ("q3", "_", "R"), 

("q2", "1"): ("q2", "1", "L"), 

("q2", "0"): ("q2", "0", "L"), 

("q2", "_"): ("q3", "_", "R"), 

} 

 

tm = TuringMachine(tape, initial_state, final_states, transition_function) 

result = tm.run() 

print("Résultat:", result) 

 