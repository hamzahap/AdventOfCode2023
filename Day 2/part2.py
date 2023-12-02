import numpy as np
import re

def parse_input(input_data):
    games = []
    for line in input_data:
        if not line.strip():
            continue
        game_id = int(line.split(':')[0].split(' ')[1])
        counts = np.array([0, 0, 0]) 
        for match in re.findall(r'(\d+) red|(\d+) green|(\d+) blue', line):
            counts = np.vstack((counts, [int(x) if x else 0 for x in match]))
        max_counts = counts.max(axis=0)
        games.append((game_id, max_counts))
    return games

def calculate_power(games):
    total_power = 0
    for _, counts in games:
        power = np.prod(counts) 
        total_power += power
    return total_power

def main():
    with open('input.txt', 'r') as file:
        input_data = file.readlines()

    games = parse_input(input_data)
    result = calculate_power(games)
    print(result)

if __name__ == "__main__":
    main()
