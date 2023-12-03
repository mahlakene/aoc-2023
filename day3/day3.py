"""Day 3."""

filename = "day3/input.txt"
with open(filename, "r") as f:
    lines = f.readlines()


def find_numbers(line):
    numbers = []
    current_nr = None
    current_index = []
    for i, char in enumerate(line):
        if char.isdigit() and not current_nr:
            current_nr = char
            current_index = [i]
        elif char.isdigit() and current_nr:
            current_nr += char
        elif current_nr:
            current_index.append(i)
            numbers.append([int(current_nr), current_index])
            current_nr = None
            current_index = []
    return numbers
    

def check_all_sides(v, i):
    line = lines[i]
    if v[0] != 0 and line[v[0] - 1] not in "." or len(line) > v[1] + 1 and line[v[1]] not in ".\n":
        return True
    start = v[0] - 1
    if start < 0:
        start = 0
    if i == 0:
        previous_line = None
    else:
        previous_line = lines[i - 1]
    if len(lines) <= i + 1:
        next_line = None
    else:
        next_line = lines[i + 1]
    for j in range(start, v[1] + 1):
        if previous_line and previous_line[j] not in ".\n":
            return True
        if next_line and next_line[j] not in ".\n":
            return True
    return False


def part1():
    sum = 0
    for i, line in enumerate(lines):
        numbers = find_numbers(line)
        for j in numbers:
            adjacent = check_all_sides(j[1], i)
            if adjacent:
                sum += j[0]
    return sum


def part2():
    sum = 0
    for i, line in enumerate(lines):
        for k, char in enumerate(line):
            if char == "*":
                top_row, bottom_row = [], []
                if i > 0:
                    top_row = find_numbers(lines[i - 1])
                if i < len(lines) - 1:
                    bottom_row = find_numbers(lines[i + 1])
                current_row = find_numbers(line)
                adjacent_numbers = []
                for j in top_row + current_row + bottom_row:
                    if k in range(j[1][0] - 1, j[1][1] + 1):
                        adjacent_numbers.append(j[0])
                print(adjacent_numbers)
                if len(adjacent_numbers) == 2:
                    sum += adjacent_numbers[0] * adjacent_numbers[1]
    return sum


if __name__ == "__main__":
    print(part1())
    print(part2())            
