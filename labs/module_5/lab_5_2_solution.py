import numpy as np
import random

STATES = ["Recon", "InitialAccess", "PrivEsc", "Exfil", "Done"]
STATE_INDICES = {s: i for i, s in enumerate(STATES)}

# Transition Matrix
# Rows: From [Recon, InitialAccess, PrivEsc, Exfil, Done]
# Cols: To   [Recon, InitialAccess, PrivEsc, Exfil, Done]
TRANSITION_MATRIX = np.array([
    [0.3, 0.7, 0.0, 0.0, 0.0], # Recon: 30% stay, 70% succeed to Access
    [0.1, 0.2, 0.6, 0.1, 0.0], # Access: 10% back to Recon, 20% stay, 60% PrivEsc, 10% fast Exfil
    [0.0, 0.0, 0.2, 0.8, 0.0], # PrivEsc: 20% stay, 80% Exfil
    [0.0, 0.0, 0.0, 0.1, 0.9], # Exfil: 10% stay, 90% Done
    [0.0, 0.0, 0.0, 0.0, 1.0], # Done: Absorbing state
])

def step(current_state):
    curr_idx = STATE_INDICES[current_state]
    probs = TRANSITION_MATRIX[curr_idx]
    
    # Sample next state
    next_state = np.random.choice(STATES, p=probs)
    return next_state

def run_lab_5_2():
    print("### Lab 5.2: Markov Chains (Solution) ###")
    
    print("Simulating 5 Attack Scenarios...")
    for i in range(5):
        path = ["Recon"]
        steps = 0
        while path[-1] != "Done" and steps < 20: # Safety break
            next_s = step(path[-1])
            path.append(next_s)
            steps += 1
        
        print(f"Scenario {i+1}: {' -> '.join(path)}")

if __name__ == "__main__":
    run_lab_5_2()
