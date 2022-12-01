if __name__ == '__main__':
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
    print(f'most calories per elf = [{max(total_calories_per_elf)}]')

