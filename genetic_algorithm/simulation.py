"""
Genetic Algorithm: Evolving a Random String into a Target String

"""
import random
import string

TARGET = "GENETIC ALGORITHM"   # what we want to evolve towards
POPULATION_SIZE = 200
MUTATION_RATE = 0.01            # probability a character mutates
MAX_GENERATIONS = 500
ALLOWED_CHARS = string.ascii_uppercase + " "


def random_individual(length):
    """Create one random string of the given length."""
    return "".join(random.choice(ALLOWED_CHARS) for _ in range(length))


def fitness(individual, target):
    """
    Fitness = number of characters that match the target in the
    correct position. Higher is better. Max fitness = len(target).
    """
    return sum(1 for a, b in zip(individual, target) if a == b)


def crossover(parent1, parent2):
    """
    Combine two parent strings into a child by picking a random
    cut point and taking the first part from parent1, rest from parent2.
    """
    cut = random.randint(0, len(parent1) - 1)
    return parent1[:cut] + parent2[cut:]


def mutate(individual):
    """Randomly change some characters based on MUTATION_RATE."""
    new_individual = list(individual)
    for i in range(len(new_individual)):
        if random.random() < MUTATION_RATE:
            new_individual[i] = random.choice(ALLOWED_CHARS)
    return "".join(new_individual)


def select_parent(population, target):
    """
    Tournament selection: pick 5 random individuals, return the fittest.
    This favors good solutions without always picking only the single best
    (which would reduce genetic diversity too fast).
    """
    contenders = random.sample(population, 5)
    contenders.sort(key=lambda ind: fitness(ind, target), reverse=True)
    return contenders[0]


def run_genetic_algorithm():
    population = [random_individual(len(TARGET)) for _ in range(POPULATION_SIZE)]
    best_fitness_over_time = []

    for generation in range(MAX_GENERATIONS):
        # Sort current population by fitness (best first)
        population.sort(key=lambda ind: fitness(ind, TARGET), reverse=True)
        best = population[0]
        best_fit = fitness(best, TARGET)
        best_fitness_over_time.append(best_fit)

        print(f"Gen {generation:3d} | Best: '{best}' | Fitness: {best_fit}/{len(TARGET)}")

        # Stop early if we've matched the target exactly
        if best_fit == len(TARGET):
            print(f"\nTarget reached in {generation} generations!")
            break

        # Build the next generation
        new_population = population[:10]  # elitism: keep top 10 unchanged
        while len(new_population) < POPULATION_SIZE:
            parent1 = select_parent(population, TARGET)
            parent2 = select_parent(population, TARGET)
            child = mutate(crossover(parent1, parent2))
            new_population.append(child)

        population = new_population

    return best_fitness_over_time



history = run_genetic_algorithm()


