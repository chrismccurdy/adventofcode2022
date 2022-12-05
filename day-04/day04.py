from enum import Enum
import sys


class overlap(Enum):
    Some = 1
    All = 2

def read_input(input: str) -> list[str]:
    file = open(input, 'r')
    return file.read().splitlines()


def parse_pairs(pair: str) -> list[set]:
    return map(
        create_set_from_section_assignment,
        pair.split(',')
    )


def create_set_from_section_assignment(assignment: str) -> set[int]:
    start, end = assignment.split('-')
    return set(range(int(start), int(end) + 1))


def has_overlap(elf_one: set[int], elf_two: set[int]) -> overlap:
    intersection = elf_one.intersection(elf_two)
    is_sz = len(intersection)
    if is_sz == 0:
        return None
    elif is_sz != len(elf_one) and is_sz != len(elf_two):
        return overlap.Some
    else:
        return overlap.All


def count_overlapping_pairs(pairs: list[str]) -> tuple[int, int]:
    fully_contained = 0
    some_overlap = 0
    for pair in pairs:
        elf_one, elf_two = parse_pairs(pair)
        ol = has_overlap(elf_one, elf_two)
        if ol != None:
            some_overlap += 1
            if ol == overlap.All:
                fully_contained += 1
    return (some_overlap, fully_contained)


so, fc = count_overlapping_pairs(read_input(sys.argv[1]))
print(f'fully contained pairs [{fc}]')
print(f'some overlap [{so}]')
