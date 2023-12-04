from pathlib import Path
import re

def read_file(filename: str) -> list[str]:
    current_script_path = Path(__file__).resolve()
    combined_path = Path.joinpath(current_script_path.parent,filename)
    file_contents: list[str] = []
    with open(combined_path, 'rt') as FILE:
        file_contents = FILE.readlines()
    return [line[:-1] for line in file_contents]

def part1():
    reds = 12
    greens = 13
    blues = 14
    lines = read_file('input.txt')
    possible_games = []
    for line in lines:
        game, game_tries = line.split(':')
        game_number = re.findall(r'Game (\d+)', game)
        tries = game_tries.strip().split(';')
        game_is_lost = False
        for hand in tries:
            if game_is_lost:
                break
            red = re.findall(r'(\d+) red', hand)
            green = re.findall(r'(\d+) green', hand)
            blue = re.findall(r'(\d+) blue', hand)
            if len(red) == 0:
                red = 0
            else:
                red = int(red[0])
            if len(green) == 0:
                green = 0
            else:
                green = int(green[0])
            if len(blue) == 0:
                blue = 0
            else:
                blue = int(blue[0])
            if red > reds or green > greens or blue > blues:
                # the whole game is lost since it is impossible move on to next game
                game_is_lost = True
                break # does break break out of the inner or outer loop?
        if not game_is_lost:
            possible_games.append(int(game_number[0]))
    return sum(possible_games)


def part2():
    lines = read_file('input.txt')
    powers_of_cubes = []
    for line in lines:
        game, game_tries = line.split(':')
        tries = game_tries.strip().split(';')
        max_red = 0
        max_blue = 0
        max_green = 0
        for hand in tries:
            red = re.findall(r'(\d+) red', hand)
            green = re.findall(r'(\d+) green', hand)
            blue = re.findall(r'(\d+) blue', hand)
            if len(red) == 0:
                red = 0
            else:
                red = int(red[0])
            if len(green) == 0:
                green = 0
            else:
                green = int(green[0])
            if len(blue) == 0:
                blue = 0
            else:
                blue = int(blue[0])
            if red > max_red:
                max_red = red
            if blue > max_blue:
                max_blue = blue
            if green > max_green:
                max_green = green
        # all hands have been played, minimum set has been found
        powers_of_cubes.append(max_red * max_green * max_blue)
    return sum(powers_of_cubes)

def results():
    answer1 = part1()
    answer2 = part2()
    pass

results()