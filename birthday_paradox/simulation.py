import random

def birthday_trial(num_people: int) -> bool:
    """
    Simulate one room of `num_people` people with random birthdays
    (1 to 365, ignoring leap years). Returns True if at least two
    people share a birthday.
    """
    birthdays = [random.randint(1, 365) for _ in range(num_people)]
    return len(set(birthdays)) < len(birthdays)  # duplicate found


def estimate_birthday_probability(num_people: int, num_trials=5000) -> float:
    """Estimate P(at least one shared birthday) for a given group size."""
    matches = sum(birthday_trial(num_people) for _ in range(num_trials))
    return matches / num_trials

def run_birthday_paradox():
    print("=== Birthday Paradox ===")
    group_sizes = list(range(1, 61))       # test group sizes 1 to 60
    probabilities = []

    for n in group_sizes:
        p = estimate_birthday_probability(n, num_trials=3000)
        probabilities.append(p)
        if n in (10, 23, 30, 50, 60):       # print a few checkpoints
            print(f"People: {n:2d} | Simulated P(shared birthday): {p:.4f}")

    print()
    return group_sizes, probabilities

sizes,probs = run_birthday_paradox()
