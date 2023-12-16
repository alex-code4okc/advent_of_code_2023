import re
from pathlib import Path

def read_file(filename: str) -> list[str]:
    current_script_path = Path(__file__).resolve()
    combined_path = Path.joinpath(current_script_path.parent,filename)
    file_contents: list[str] = []
    with open(combined_path, 'rt') as FILE:
        file_contents = FILE.readlines()
    return file_contents

def setup1():
    lines = read_file('input.txt')
    times = []
    distances = []
    time_matches = re.findall(r'\d+', lines[0])
    distance_matches = re.findall(r'\d+', lines[1])
    for time in time_matches:
        times.append(int(time))
    for distance in distance_matches:
        distances.append(int(distance))
    time_distance_pairs = []
    for i, time in enumerate(times):
        time_distance_pairs.append((time, distances[i]))
    return time_distance_pairs

def part1():
    time_distance_pairs = setup1()
    records = {}
    for p in time_distance_pairs:
        t = p[0]
        for ht in range(0,t+1,1):
            remaining = t - ht
            distance = remaining * ht
            if remaining > 0 and distance > p[1]:
                if p in records:
                    records[p].append(ht)
                else:
                    records[p] = [ht]
    power = 1
    for k,v in records.items():
        power*=len(v)
    return power

def setup2():
    lines = read_file('input.txt')
    times = ''
    distances = ''
    time_matches = re.findall(r'\d+', lines[0])
    distance_matches = re.findall(r'\d+', lines[1])
    for time in time_matches:
        times += time
    for distance in distance_matches:
        distances += distance
    return [(int(times), int(distances))]
def part2():
    time_distance_pair = setup2()
    records = {}
    for p in time_distance_pair:
        t = p[0]
        for ht in range(0,t+1,1):
            remaining = t - ht
            distance = remaining * ht
            if remaining > 0 and distance > p[1]:
                if p in records:
                    records[p].append(ht)
                else:
                    records[p] = [ht]
    power = 1
    for k,v in records.items():
        power*=len(v)
    return power

def results():
    answer1 = part1()
    answer2 = part2()
    pass

results()