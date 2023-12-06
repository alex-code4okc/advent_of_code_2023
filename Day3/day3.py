from pathlib import Path
import re

def read_file(filename: str) -> list[str]:
    current_script_path = Path(__file__).resolve()
    combined_path = Path.joinpath(current_script_path.parent,filename)
    file_contents: list[str] = []
    with open(combined_path, 'rt') as FILE:
        file_contents = FILE.readlines()
    return [line[:-1] for line in file_contents]

def setup_grid():
    lines = read_file('input.txt')
    rows = len(lines)
    cols = len(lines[0])
    # pad left and right of grid
    grid = [ '.'+line+'.' for line in lines]
    # pad top and bottom of grid
    grid.insert(0, '.'*(cols+2))
    grid.append('.'*(cols+2))
    return grid

def matching_items(grid, pattern):
    number_indices_in_grid = []
    # finding part numbers
    row_index = 0
    for row in grid:
        matches = re.finditer(pattern, row)
        for match in matches:
            group = match.group()
            start = match.start()
            end = match.end()
            number_indices_in_grid.append((row_index, f'{start}'+','+f'{end}', group))
        row_index += 1
    return number_indices_in_grid

def part1():
    grid = setup_grid()
    # grid is now padded iterate through index 1 to len + 1 in rows
    number_indices_in_grid = matching_items(grid,r'\d+')
    valid_part_numbers = []
    # testing to see if part number is valid
    for num_point in number_indices_in_grid:
        x = num_point[0] # row
        y = num_point[1] # y range
        start, end = y.split(',')
        # iterate through range
        for i in range(int(start), int(end), 1):
            # check left, right, top, bottom of grid
            left = grid[x-1][i]
            right = grid[x+1][i]
            top = grid[x][i-1]
            bottom = grid[x][i+1]
            tld = grid[x-1][i-1]
            trd = grid[x+1][i-1]
            bld = grid[x-1][i+1]
            brd = grid[x+1][i+1]

            if((not top.isnumeric() and not top =='.')
                or (not bottom.isnumeric() and not bottom =='.')
                or (not left.isnumeric() and not left =='.')
                or (not right.isnumeric() and not right =='.')
                or (not tld.isnumeric() and not tld =='.')
                or (not trd.isnumeric() and not trd =='.')
                or (not bld.isnumeric() and not bld =='.')
                or (not brd.isnumeric() and not brd =='.')
                ):
                valid_part_numbers.append(int(num_point[2]))
                break # no longer need to check the other points
    return sum(valid_part_numbers)

def part2():
    grid = setup_grid()
    stars_in_grid = matching_items(grid,r'[*]')
    numbers_in_grid = matching_items(grid,r'\d+')
    numbers_in_grid_expanded_cols = [(item[0],item[1].split(','),item[2]) for item in numbers_in_grid]
    gears_multiplied = []
    for star_point in stars_in_grid:
        x = star_point[0] # row
        y = star_point[1] # y range
        start, _ = y.split(',')
        adjacent_gears = []
        s = int(start)
        top = grid[x-1][s]
        bottom = grid[x+1][s]
        left = grid[x][s-1]
        right = grid[x][s+1]
        tld = grid[x-1][s-1]
        trd = grid[x+1][s-1]
        bld = grid[x-1][s+1]
        brd = grid[x+1][s+1]
        if top.isnumeric():
            adjacent_gears.append((x-1,s))
        if bottom.isnumeric():
            adjacent_gears.append((x+1,s))
        if left.isnumeric():
            adjacent_gears.append((x,s-1))
        if right.isnumeric():
            adjacent_gears.append((x,s+1))
        if tld.isnumeric():
            adjacent_gears.append((x-1,s-1))
        if trd.isnumeric():
            adjacent_gears.append((x+1,s-1))
        if bld.isnumeric():
            adjacent_gears.append((x-1,s+1))
        if brd.isnumeric():
            adjacent_gears.append((x+1,s+1))

        unique_rows = set([n[0] for n in adjacent_gears])
        gear_numbers = []
        for ur in unique_rows:
            # (row, col)[]
            adjacent_gears_filtered_by_row = [ag for ag in adjacent_gears if ag[0] == ur]
            # (row, [str(col1), str(col2), 'number'])
            filtered_by_row_in_grid = [n for n in numbers_in_grid_expanded_cols if n[0] == ur]
            for fr in filtered_by_row_in_grid:
                for adjacent_gear in adjacent_gears_filtered_by_row:
                    # lists all the cols the filtered numbers occupy
                    number_range = list(range(int(fr[1][0]), int(fr[1][1])))
                    if adjacent_gear[1] in number_range:
                        gear_numbers.append(int(fr[2]))
                        break
        if len(gear_numbers) >1:
            gears_multiplied.append(gear_numbers[0] * gear_numbers[1])
    return sum(gears_multiplied)

def results():
    answer1 = part1()
    answer2 = part2()
    pass

results()