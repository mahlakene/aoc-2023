"""Day 1."""
import string

with open("day1/input.txt", "r") as f:
    lines = f.readlines()


def first_part():
    sum = 0
    for i in lines:
        line = i.strip(string.ascii_lowercase + "\n")
        sum += int(line[0] + line[-1])
    return sum


def second_part():
    numbers = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}
    sum = 0
    for i in lines:
        first, last = None, None
        found = False
        for index, char in enumerate(i):
            if found:
                break
            if char.isdigit():
                first = char
                break
            else:
                for nr in numbers.keys():
                    if nr == i[index: index + len(nr)]:
                        first = numbers[nr]
                        found = True
                        break
        found = False
        for index, char in enumerate(i[::-1]):
            if found:
                break
            if char.isdigit():
                last = char
                break
            else:
                for nr in numbers.keys():
                    if nr == i[::-1][index: index - len(nr): -1]:
                        last = numbers[nr]
                        found = True
                        break
        sum += int(first + last)
        print(int(first + last))
    return sum


if __name__ == "__main__":
    print(first_part())
    print(second_part())
