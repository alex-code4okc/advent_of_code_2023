from collections import namedtuple
from pathlib import Path
import re
from typing import Tuple

MapEntry = namedtuple('MapEntry', ['source_start','source_end','destination_start','destination_end','length'])

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

def generate_map(lines) -> list[Tuple]:
    map_entries = []
    for line in lines[1:]: # skip first line
        matches = re.findall(r'\d+', line)
        d_start = int(matches[1])
        s_start = int(matches[0])
        length = int(matches[2])
        map_entries.append((d_start, d_start + length -1, s_start, s_start + length-1, length))
    return map_entries

def find_destination_with_map(source, source_destination_map) -> int:
    for e in source_destination_map:
        if source >= e[0] and source <= e[1]:
            offset = source - e[0]
            return e[2] + offset
            break
    return source

def setup():
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
    return (test_seeds, seed_to_soil, soil_to_fertilizer, fertilizer_to_water, water_to_light,light_to_temperature,temperature_to_humidity,humidity_to_location)

def part1():
    test_seeds, seed_to_soil, soil_to_fertilizer, fertilizer_to_water, water_to_light, light_to_temperature, temperature_to_humidity, humidity_to_location = setup()

    starting_seeds = generate_starting_seeds_list(test_seeds)
    seed_to_soil_map = generate_map(seed_to_soil)
    soil_to_fertilizer_map = generate_map(soil_to_fertilizer)
    fertilizer_to_water_map = generate_map(fertilizer_to_water)
    water_to_light_map = generate_map(water_to_light)
    light_to_temperature_map = generate_map(light_to_temperature)
    temperature_to_humidity_map = generate_map(temperature_to_humidity)
    humidity_to_location_map = generate_map(humidity_to_location)

    seed_to_location_map: list[Tuple] = []

    for seed in starting_seeds:
        soil_destination = find_destination_with_map(seed, seed_to_soil_map)
        fertilizer_destination = find_destination_with_map(soil_destination, soil_to_fertilizer_map)
        water_destination = find_destination_with_map(fertilizer_destination, fertilizer_to_water_map)
        light_destination = find_destination_with_map(water_destination, water_to_light_map)
        temperature_destination = find_destination_with_map(light_destination, light_to_temperature_map)
        humidity_destination = find_destination_with_map(temperature_destination, temperature_to_humidity_map)
        location_destination = find_destination_with_map(humidity_destination, humidity_to_location_map)
        seed_to_location_map.append(location_destination)
    return min(seed_to_location_map)


def part2():
    test_seeds, seed_to_soil, soil_to_fertilizer, fertilizer_to_water, water_to_light, light_to_temperature, temperature_to_humidity, humidity_to_location = setup()
    starting_seeds = generate_starting_seeds_list(test_seeds)
    seed_to_soil_map = generate_map(seed_to_soil)
    soil_to_fertilizer_map = generate_map(soil_to_fertilizer)
    fertilizer_to_water_map = generate_map(fertilizer_to_water)
    water_to_light_map = generate_map(water_to_light)
    light_to_temperature_map = generate_map(light_to_temperature)
    temperature_to_humidity_map = generate_map(temperature_to_humidity)
    humidity_to_location_map = generate_map(humidity_to_location)
    starting_seeds = generate_starting_seeds_list(test_seeds)
    seed_ranges = []
    for i in range(1,len(starting_seeds),2):
        start = starting_seeds[i-1]
        length = starting_seeds[i]
        seed_ranges.append((start, start+length))
    seed_to_location_map = []
    for sr in seed_ranges:
        s = sr[0]
        e = sr[1]
        for elem in range(s, e, 1):
            soil_destination = find_destination_with_map(elem, seed_to_soil_map)
            fertilizer_destination = find_destination_with_map(soil_destination, soil_to_fertilizer_map)
            water_destination = find_destination_with_map(fertilizer_destination, fertilizer_to_water_map)
            light_destination = find_destination_with_map(water_destination, water_to_light_map)
            temperature_destination = find_destination_with_map(light_destination, light_to_temperature_map)
            humidity_destination = find_destination_with_map(temperature_destination, temperature_to_humidity_map)
            location_destination = find_destination_with_map(humidity_destination, humidity_to_location_map)
            seed_to_location_map.append(location_destination)
    return min(seed_to_location_map)

def results():
    answer1 = part1()
    answer2 = part2()
    pass

results()