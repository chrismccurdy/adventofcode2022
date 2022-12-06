from io import TextIOWrapper
from queue import Queue
import sys


def find_marker(file: TextIOWrapper, size: int, last_size: list[str] = None) -> tuple[int, list[str]]:
    if last_size is None:
        last_size = []
        for dummy in range(0, size):
            last_size.append(file.read(1))
    index = len(last_size)
    while True:
        if len(set(last_size)) == len(last_size):
            return (index, last_size)
        char = file.read(1)
        last_size.pop(0)
        last_size.append(char)
        index += 1

    
file = open(sys.argv[1], 'r')
index, packet = find_marker(file, 4)
print(f'found start of packet marker {"".join(packet)} ending at {index}')
file = open(sys.argv[1], 'r')
index, packet = find_marker(file, 14)
print(f'found start of message marker {"".join(packet)} ending at {index}')
