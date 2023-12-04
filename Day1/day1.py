digits = ['one','two','three','four','five','six','seven','eight','nine']
digits_reversed = [item[::-1] for item in digits]
numbers = ['1','2','3','4','5','6','7','8','9']

translation = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
    'eno': '1',
    'owt': '2',
    'eerht': '3',
    'ruof': '4',
    'evif': '5',
    'xis': '6',
    'neves': '7',
    'thgie': '8',
    'enin': '9'
}

def findFirstNumber(line: [str]):
    for c in line:
        if c.isdigit():
            return c

with open('/Users/alex/Documents/Repositories/advent-of-code-2023/Day1/input.txt', 'rt') as f:
    lines = [l.strip() for l in f.readlines()]



def solution1(lines):
    counts = []
    for line in lines:

        char_list = list(line)
        first_number = findFirstNumber(char_list)
        reverse = char_list[:]
        reverse.reverse()
        last_number = findFirstNumber(reverse)
        composite_number = first_number + last_number
        counts.append(int(composite_number))

    return sum(counts)

def solution2(lines):
    counts = []
    for line in lines:
        found = {}
        found_reverse = {}
        line_reversed = line[::-1]
        for number in numbers:
            index = line.find(number)
            if index > -1:
                found[number] = index
        for digit in digits:
            index = line.find(digit)
            if index > -1:
                found[digit] = index
        for number in numbers:
            index = line_reversed.find(number)
            if index > -1:
                found_reverse[number] = index
        for digit in digits_reversed:
            index = line_reversed.find(digit)
            if index > -1:
                found_reverse[digit] = index

        min_forward_index = len(line) - 1
        min_forward_value = ''
        min_reverse_index = min_forward_index
        min_reverse_value = ''
        for number, index in found.items():
            if index <= min_forward_index:
                min_forward_index = index
                min_forward_value = number
        for number, index in found_reverse.items():
            if index <= min_reverse_index:
                min_reverse_index = index
                min_reverse_value = number
        if not min_forward_value.isdigit():
            min_forward_value = translation[min_forward_value]
        if not min_reverse_value.isdigit():
            min_reverse_value = translation[min_reverse_value]
        counts.append(int(min_forward_value+min_reverse_value))

    return sum(counts)

total1 = solution1(lines)
total2 = solution2(lines)
print(total1)
print(total2)
