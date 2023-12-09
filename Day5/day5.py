from collections import namedtuple
from pathlib import Path
import re

def read_file(filename: str) -> list[str]:
    current_script_path = Path(__file__).resolve()
    combined_path = Path.joinpath(current_script_path.parent,filename)
    file_contents: list[str] = []
    with open(combined_path, 'rt') as FILE:
        file_contents = FILE.readlines()
    return file_contents

def generate_starting_seeds_list(test_seeds):
    for seed in test_seeds:
        matches = re.findall(r'\d+', seed)
        return [int(match) for match in matches]

def generate_seed_to_soil_map(lines):
    seed_to_soil_map = {}
    source = []
    destination = []
    length = []
    for line in lines[1:]: # skip first line
        matches = re.findall(r'\d+', line)
        destination.append(int(matches[0]))
        source.append(int(matches[1]))
        length.append(int(matches[2]))
    max_destination = max(destination)
    min_destination = min(destination)
    max_source = max(source)
    min_source = min(source)

    max_compared = max(max_destination, max_source)
    min_compared = min(min_destination, min_source)
    


def part1():
    test_seeds = []
    seed_to_soil = []
    soil_to_fertilizer = []
    fertilizer_to_water = []
    water_to_light = []
    light_to_temperature = []
    temperature_to_humidity = []
    humidity_to_location = []
    lines = read_file('input.txt')
    new_line_count = 0
    for line in lines:
        if line == '\n':
            new_line_count+=1
            continue
        if new_line_count == 0:
            test_seeds.append(line)
            continue
        if new_line_count == 1:
            seed_to_soil.append(line)
            continue
        if new_line_count == 2:
            soil_to_fertilizer.append(line)
            continue
        if new_line_count == 3:
            fertilizer_to_water.append(line)
            continue
        if new_line_count == 4:
            water_to_light.append(line)
            continue
        if new_line_count == 5:
            light_to_temperature.append(line)
            continue
        if new_line_count == 6:
            temperature_to_humidity.append(line)
            continue
        if new_line_count == 7:
            humidity_to_location.append(line)
            continue

    starting_seeds = generate_starting_seeds_list(test_seeds)
    seed_to_soil_map = generate_seed_to_soil_map(seed_to_soil)


def part2():
    pass

def results():
    answer1 = part1()
    answer2 = part2()
    pass

results()