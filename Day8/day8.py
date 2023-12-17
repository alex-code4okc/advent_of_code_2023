import re
from pathlib import Path

def read_file(filename: str) -> list[str]:
    current_script_path = Path(__file__).resolve()
    combined_path = Path.joinpath(current_script_path.parent,filename)
    file_contents: list[str] = []
    with open(combined_path, 'rt') as FILE:
        file_contents = FILE.readlines()
    return file_contents

direction_mapping = {
    'R': 1,
    'L': 0,
}

def setup():
    lines = read_file('input.txt')
    directions = lines[0].strip()
    directions_map = {}
    for line in lines[2:]:
        matches = re.findall(r'\w+', line)
        directions_map[matches[0]] = (matches[1],matches[2])
    return (directions, directions_map)

def part1():
    directions, mapping = setup()
    current_node = mapping['AAA']
    # loop
    i = 0
    n = len(directions)
    steps = 0
    while True:
        direction = directions[i]
        index = direction_mapping[direction]
        next_node_key = current_node[index]
        i = (i+1)%n
        steps += 1
        current_node = mapping[next_node_key]
        if next_node_key == 'ZZZ':
            break
    return steps

def part2():
    directions, mapping = setup()
    keys_A = [k for k in mapping.keys() if k[2] == 'A']
    initial_paths_count = len(keys_A)
    current_nodes = [mapping[k] for k in keys_A]
    # loop
    i = 0
    n = len(directions)
    steps = 0
    while True:
        direction = directions[i]
        index = direction_mapping[direction]
        next_node_keys = [cn[index] for cn in current_nodes]
        i = (i+1)%n
        steps += 1
        current_nodes = [mapping[k] for k in next_node_keys]
        all_Z = [k[2] for k in next_node_keys]
        if all_Z.count('Z') == initial_paths_count:
            break
    return steps

def results():
    #answer1 = part1()
    answer2 = part2()
    pass

results()