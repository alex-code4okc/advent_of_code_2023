import re
from pathlib import Path
import math

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

def steps_per_key(key, directions,mapping):
    current_node = mapping[key]
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
        if next_node_key[2] == 'Z':
            break
    return steps

def part2():
    directions, mapping = setup()
    keys_A = [k for k in mapping.keys() if k[2] == 'A']
    steps = []
    for key in keys_A:
        step = steps_per_key(key,directions,mapping)
        steps.append(step)
    return math.lcm(*steps)

def results():
    answer1 = part1()
    answer2 = part2()
    pass

results()