import random

def monty_hall_trial(switch: bool) -> bool:
    """
    Simulate one round of Monty Hall.
    Returns True if the player wins the car.
    """
    doors = [0, 1, 2]
    car_door = random.choice(doors)          # door with the car
    player_choice = random.choice(doors)     # player's initial pick

    # Host opens a door that is NOT the car and NOT the player's pick
    remaining_doors = [d for d in doors if d != player_choice and d != car_door]
    host_opens = random.choice(remaining_doors)

    if switch:
        # Player switches to the one remaining unopened door
        final_choice = [d for d in doors if d != player_choice and d != host_opens][0]
    else:
        final_choice = player_choice

    return final_choice == car_door


def run_monty_hall(num_trials=10000):
    stay_wins = sum(monty_hall_trial(switch=False) for _ in range(num_trials))
    switch_wins = sum(monty_hall_trial(switch=True) for _ in range(num_trials))

    stay_rate = stay_wins / num_trials
    switch_rate = switch_wins / num_trials

    print("=== Monty Hall Problem ===")
    print(f"Trials: {num_trials}")
    print(f"Win rate if you STAY:   {stay_rate:.4f}  (theory: 0.3333)")
    print(f"Win rate if you SWITCH: {switch_rate:.4f}  (theory: 0.6667)")
    print()

    return stay_rate, switch_rate

run_monty_hall(num_trials=10000)
