from pathlib import Path

def read_file(filename: str) -> list[str]:
    current_script_path = Path(__file__).resolve()
    combined_path = Path.joinpath(current_script_path.parent,filename)
    file_contents: list[str] = []
    with open(combined_path, 'rt') as FILE:
        file_contents = FILE.readlines()
    return file_contents

def part1():
    pass

def part2():
    pass

def results():
    answer1 = part1()
    answer2 = part2()
    pass