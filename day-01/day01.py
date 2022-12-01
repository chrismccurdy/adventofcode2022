from functools import reduce

def get_total_calories_per_elf() -> dict[int]:
    file = open('input', 'r')
    lines = file.readlines()

    total_calories_per_elf = []
    current_elf = 1
    current_calories = 0
    for line in lines:
        stripped = line.strip()
        if len(stripped) == 0:
            total_calories_per_elf.append(current_calories)
            print(f'elf [{current_elf}] has [{current_calories}] calories')
            current_elf += 1
            current_calories = 0
        else:
            current_calories += int(stripped)
    total_calories_per_elf.append(current_calories)
    print(f'elf [{current_elf}] has [{current_calories}] calories')
    return total_calories_per_elf


if __name__ == '__main__':
    total_calories_per_elf = get_total_calories_per_elf()
    print(f'most calories per elf = [{max(total_calories_per_elf)}]')
    top_three = sorted(total_calories_per_elf)[-3:]
    total_top_three = reduce(lambda x, y: x + y, top_three)
    print(f'top 3 elf calories = [{top_three}]')
    print(f'total of top 3 elves = [{total_top_three}]')

