from functools import reduce
from io import TextIOWrapper
import sys
from typing import Any


total_disk_space = 70000000
minimum_required_space = 30000000
max_size = 100000
total_size = 0


def add_to_total_size(size: int) -> None:
    global total_size
    total_size += size


class Directory:
    def __init__(self, name, parent = None):
        self.name = name
        self.parent: Directory = parent
        self.files: dict[str, int] = {}
        self.directories: dict[str, Directory] = {}
        self.total_size = 0


    def get_total_size(self) -> int:
        file_size = reduce(
            lambda x, y: x + y,
            self.files.values(),
            0
        )
        directory_size = reduce(
            lambda x, y: x + y,
            map(lambda x: x.get_total_size(), self.directories.values()),
            0
        )
        total = file_size + directory_size
        self.total_size = total
        if total <= max_size:
            add_to_total_size(total)
        return total


    def get_directory_sizes(self):
        sizes = {}
        sizes[self.name] = self.total_size
        for child in self.directories.values():
            sizes.update(child.get_directory_sizes())
        return sizes


def parse_line(line: str, cwd: Directory) -> Directory:
    line = line.strip()
    if line == '':
        return cwd

    if line.startswith('$'):
        cmd = line[2:]
        if cmd.startswith('cd'):
            target = cmd[3:]
            if target == '..':
                cwd = cwd.parent
            elif target == '/':
                cwd = Directory(target)
            else:
                cwd = cwd.directories[target]
        else:
            # do nothing for ls
            pass
    elif line.startswith('dir'):
        dummy, name = line.split(' ')
        cwd.directories[name] = Directory(name, cwd)
    else:
        size, name = line.split(' ')
        cwd.files[name] = int(size)

    return cwd


lines = open(sys.argv[1], 'r').readlines()
cwd: Directory = None
for line in lines:
    cwd = parse_line(line, cwd)
while cwd.parent is not None:
    cwd = cwd.parent
root = cwd
total_disk_used = root.get_total_size()
print(f'total size under  [{max_size}]: [{total_size}]')

disk_unused = total_disk_space - total_disk_used
print(f'total disk space  [{total_disk_space:>12}]')
print(f'total disk used   [{total_disk_used:>12}]')
print(f'total disk unused [{disk_unused:>12}]')
print(f'disk req update   [{minimum_required_space:>12}]')
minimum_to_delete = minimum_required_space - disk_unused
print(f'size to delete    [{minimum_to_delete:>12}]')

to_delete = sorted(filter(
    lambda size: size >= minimum_to_delete,
    root.get_directory_sizes().values()
))[0]
print(f'deleting [{to_delete}] bytes')
