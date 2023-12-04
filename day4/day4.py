"""Day 4."""


filename = "day4/input.txt"
with open(filename, "r") as f:
    lines = f.readlines()


def part1():
    sum = 0
    for line in lines:
        total_matches = 0
        game = line.split(": ")
        winning_cards = list(map(int, game[1].split(" | ")[0].split()))
        my_cards = list(map(int, game[1].split(" | ")[1].split()))
        for i in my_cards:
            if i in winning_cards:
                total_matches += 1
        if total_matches == 0:
            continue
        sum += 2 ** (total_matches - 1)
    return sum


def part2():
    copies = {}
    for i in range(len(lines)):
        copies[i] = 1
    for index, line in enumerate(lines):
        total_matches = 0
        game = line.split(": ")
        winning_cards = list(map(int, game[1].split(" | ")[0].split()))
        my_cards = list(map(int, game[1].split(" | ")[1].split()))
        for i in my_cards:
            if i in winning_cards:
                total_matches += 1
        if total_matches == 0:
            continue
        for j in range(1, total_matches + 1):
            if j < len(lines):
                copies[index + j] = copies.get(index + j, 0) + copies[index]
    print(copies.values())
    return sum(copies.values())


if __name__ == "__main__":
    print(part1())
    print(part2())
 