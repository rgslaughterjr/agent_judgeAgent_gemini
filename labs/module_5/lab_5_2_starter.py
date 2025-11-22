import numpy as np
import random

STATES = ["Recon", "InitialAccess", "PrivEsc", "Exfil", "Done"]

# Transition Matrix (Rows = From, Cols = To)
# TODO: Fill in probabilities
TRANSITION_MATRIX = [
    # Recon -> [Recon, InitialAccess, PrivEsc, Exfil, Done]
    [0.5, 0.5, 0.0, 0.0, 0.0], 
    # InitialAccess -> ...
    [0.0, 0.0, 0.0, 0.0, 0.0],
    # ...
]

def step(current_state):
    """
    TODO: Pick the next state based on probabilities.
    """
    pass

def run_lab_5_2():
    print("### Lab 5.2: Markov Chains ###")
    
    # Simulate
    # path = ["Recon"]
    # while path[-1] != "Done":
    #     path.append(step(path[-1]))
    
    # print(f"Attack Path: {path}")

if __name__ == "__main__":
    run_lab_5_2()
