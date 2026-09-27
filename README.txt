# Computational Probability

A collection of small Python simulations exploring probability, randomness, and mathematical ideas through computation.

## File Structure

Computational_Probability/
│
├── README.txt
│
├── birthday_paradox/
│   └── simulation.py
│
├── monty_hall/
│   └── simulation.py
│
└── genetic_algorithm/
    └── genetic_algorithm.py


## Simulations

### 1. Birthday Paradox

How does the probability of two people sharing the same birthday change as the group size increases?

**Simulation:**

* Generate random birthdays for a group of people.
* Check whether any birthday occurs more than once.
* Repeat the experiment thousands of times.
* Estimate the probability of at least one shared birthday.
* Test different group sizes.

**Main idea:** Probability estimation using repeated random experiments.

-----------------------------------------------------------------------

### 2. Monty Hall Problem

Is it better to stay with the original choice or switch after the host reveals a losing door?

**Simulation:**

* Create three doors.
* Randomly place the prize behind one door.
* The player chooses a door.
* The host reveals one of the remaining doors containing no prize.
* Simulate both strategies:

  * Always stay
  * Always switch
* Compare their winning probabilities over many trials.

**Main idea:** Experimental verification of a counterintuitive probability result.

---------------------------------------------------------------------------------

### 3. Genetic Algorithm

Can a population of random strings gradually evolve toward a target string?

**Simulation:**

* Generate a population of random strings.
* Calculate the fitness of each string by comparing it with the target.
* Select relatively better individuals as parents.
* Combine parents using crossover.
* Randomly mutate characters.
* Repeat the process over generations.
* Track how the best fitness changes over time.

**Main idea:** Using selection, crossover, and mutation to simulate evolutionary optimisation.

--------------------------------------------------------------------------------

## Common Approach

Each simulation follows the same general pattern:


Mathematical Question
        ↓
Random Experiment
        ↓
Repeat Many Times
        ↓
Collect Results
        ↓
Estimate / Observe Pattern

-> Technologies

* Python
* Randomness and probability
* Basic mathematical modeling
* Simulation and computational experiments

-> Purpose

This repository is for learning how mathematical and probabilistic ideas can be converted into computational experiments and analysed using Python.
