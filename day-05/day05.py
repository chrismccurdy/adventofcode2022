import re
import sys
from typing import Any


mover = 9000


class Move:
    def __init__(self, numToMove: int, source: int, target: int):
        self.numToMove = numToMove
        self.source = source
        self.target = target

    
    def move(self, stacks: dict[int, list[str]]) -> None:
        if mover == 9000:
            self.move_9000(stacks)
        else:
            self.move_9001(stacks)


    def move_9000(self, stacks: dict[int, list[str]]) -> None:
        for iter in range(0, self.numToMove):
            crate = stacks[self.source].pop()
            stacks[self.target].append(crate)


    def move_9001(self, stacks: dict[int, list[str]]) -> None:
        crates = stacks[self.source][-self.numToMove:]
        stacks[self.source] = stacks[self.source][0:-self.numToMove]
        stacks[self.target].extend(crates)


def read_input() -> list[str]:
    file = open(sys.argv[1], 'r')
    return file.read().splitlines()


def parse_line(line: str, stacks: dict[int, list[str]]) -> None:
    if line.startswith('move'):
        move = parse_move(line)
        move.move(stacks)
    else:
        stack_line = []
        for index in range(1, len(line), 4):
            stack_line.append(line[index])
        for index in range(0, len(stack_line)):
            char = stack_line[index]
            key = index + 1
            if key not in stacks:
                stacks[key] = []

            if char.isdigit():
                for stack in stacks.values():
                    stack.reverse()
                return
            elif char != ' ':
                stacks[key].append(char)


def parse_move(line: str) -> Move:
    numbers = re.findall(f'\d+', line)
    return Move(int(numbers[0]), int(numbers[1]), int(numbers[2]))


stacks = {}
tops = ""
for line in read_input():
    parse_line(line, stacks)
for key, stack in stacks.items():
    tops += stack.pop()
print(f'CrateMover 9000: {tops}')

mover = 9001

stacks = {}
tops = ""
for line in read_input():
    parse_line(line, stacks)
for key, stack in stacks.items():
    tops += stack.pop()
print(f'CrateMover 9001: {tops}')
