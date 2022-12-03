from functools import reduce
import sys
import time


def read_input(input: str) -> list[str]:
    file = open(input, 'r')
    return file.read().splitlines()


def priority(item: chr) -> int:
    sub = 38 if item <= 'a' else 96
    return ord(item) - sub


def split_rucksack(rucksack: str) -> tuple[str]:
    compartment_size = int(len(rucksack) / 2)
    return (rucksack[:compartment_size], rucksack[compartment_size:])


def find_duplicate_priority_set(rucksack: str) -> int:
    left, right = split_rucksack(rucksack)
    left_set = set(left)
    for item in right:
        if item in left_set:
            return priority(item)


def calc_badge_priority(func: callable) -> int:
    iset = 0
    sacks = read_input(sys.argv[1])
    sack_size = len(sacks)
    total_priority = 0
    start = time.process_time()
    while (iset + 3) <= sack_size:
        total_priority += func(sacks[iset:iset + 3])
        iset += 3
    end = time.process_time()
    print(f'total priority [{total_priority}]')
    print(f'run time = [{(end - start) * 1000}] ms')


def find_badge_priority_set(sacks: list[str]) -> int:
    set_a = set(sacks[0])
    set_b = set(sacks[1])
    for item in sacks[2]:
        if item in set_a and item in set_b:
            return priority(item)


def calc_priority(func: callable) -> None:
    start = time.process_time()
    total_priority = reduce(
        lambda x, y: x + y,
        map(func, read_input(sys.argv[1]))
    )
    end = time.process_time()
    print(f'total priority [{total_priority}]')
    print(f'run time = [{(end - start) * 1000}] ms')


calc_priority(find_duplicate_priority_set)
calc_badge_priority(find_badge_priority_set)
