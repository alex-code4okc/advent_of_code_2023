from pathlib import Path

def read_file(filename: str) -> list[str]:
    current_script_path = Path(__file__).resolve()
    combined_path = Path.joinpath(current_script_path.parent,filename)
    file_contents: list[str] = []
    with open(combined_path, 'rt') as FILE:
        file_contents = FILE.readlines()
    return [line[:-1] for line in file_contents]

def part1():
    pass

def part2():
    pass

def results():
    part1()
    part2()

results()