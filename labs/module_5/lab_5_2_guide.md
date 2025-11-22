# Lab 5.2: Probabilistic Threat Modeling (Markov Chains)

## Goal

Learn how to use **Markov Chains** to simulate attack scenarios. This allows your agent to predict "What is the most likely next step for an attacker?" based on probabilities.

## Concepts

### 1. States and Transitions

* **States**: Stages of an attack (e.g., "Recon", "Access", "Exfiltration").
* **Transition Matrix**: A grid of probabilities defining the chance of moving from State A to State B.

### 2. Simulation

By running the chain multiple times (Monte Carlo simulation), you can generate thousands of potential attack paths and identify the most dangerous ones.

## Instructions

1. **Open `lab_5_2_starter.py`**.
2. **Step 1**: Define the states (`["Recon", "InitialAccess", "PrivEsc", "Exfil", "Cleanup"]`).
3. **Step 2**: Define the Transition Matrix (numpy array).
4. **Step 3**: Write a function `simulate_attack(start_state)` that steps through the chain until it hits a terminal state.

## Resources

* [Markov Chains Explained](https://setosa.io/ev/markov-chains/)
