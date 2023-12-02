"""Day2."""


filename = "day2/input.txt"
with open(filename, "r") as f:
    lines = f.readlines()

colors = {"red": 12, "green": 13, "blue": 14}


def part_1():
    sum = 0
    for i in lines:
        impossible = False
        game = i.split(":")
        id = int(game[0][5:])
        sets = game[1].split(";")
        for set in sets:
            cubes = set.split(",")
            if impossible:
                break
            for cube in cubes:
                cube = cube.strip()
                amount = int(cube.split()[0])
                color = cube.split()[1]
                if amount > colors[color]:
                    impossible = True
                    break
        if not impossible:
            sum += id
    return sum


def part_2():
    sum = 0
    for i in lines:
        biggest = {"red": 0, "blue": 0, "green": 0}
        game = i.split(":")
        id = int(game[0][5:])
        sets = game[1].split(";")
        for set in sets:
            cubes = set.split(",")
            for cube in cubes:
                cube = cube.strip()
                amount = int(cube.split()[0])
                color = cube.split()[1]
                if amount > biggest[color]:
                    biggest[color] = amount
        sum += biggest["red"] * biggest["blue"] * biggest["green"]
    return sum


if __name__ == "__main__":
    print(part_1())
    print(part_2())
